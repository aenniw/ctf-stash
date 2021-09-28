#!/usr/bin/env python3
# Based on: https://github.com/ichinano/CTFdScraper

# NOTE: install requirements
# pip3 install -r requirements.txt

import requests
from requests import session
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from bs4 import BeautifulSoup
import unidecode
import json
import os
import requests
import re
import sys
import argparse
import ssl

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

md_appendix = '''

---

#### Solution:

```bash
```

---

<details><summary>FLAG:</summary>

```

```

</details>
<br/>
'''


class CTFdCrawl:
    def __init__(self, team, passwd, url, overwrite, solved):
        self.auth = dict(name=team, password=passwd)
        self.ses = session()
        self.entry = dict()
        self.keys = 'data'
        self.url = url
        self.overwrite = overwrite
        self.solved = solved
        self.ch_url = self.url + '/api/v1/challenges'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        }

        if not self.login():
            raise Exception('Login Failed')
        print('\n[+] Collecting resources')
        self.checkVersion()

    def login(self):
        resp = self.ses.get(self.url + '/login',
                            headers=self.headers, verify=False)
        soup = BeautifulSoup(resp.text, 'lxml')
        nonce = soup.find('input', {'name': 'nonce'})

        if not nonce:
            return False
        nonce = nonce.get('value')

        self.auth['nonce'] = nonce
        self.title = soup.title.string.replace(' ', '_')

        resp = self.ses.post(self.url + '/login', data=self.auth, verify=False)
        return 'incorrect' not in resp.text

    def checkVersion(self):
        resp = self.ses.get(self.ch_url, headers=self.headers, verify=False)
        self.version = 'v.1.2.0' if '404' not in resp.text else 'v.1.0'

    def parseChall(self, id):
        resp = self.ses.get('{}/{}'.format(self.ch_url, id),
                            headers=self.headers, verify=False).json()
        return resp['data'] if self.version == 'v.1.2.0' else resp

    def parseAll(self):
        print('[+] Finding challs')
        if self.version == 'v.1.0':
            self.ch_url = self.url + '/chals'
            self.keys = 'game'
        html = sorted(
            self.ses.get(self.ch_url, headers=self.headers, verify=False)
            .json()[self.keys], key=lambda x: sorted(x.keys()))
        ids = [i['id'] for i in html]

        for id in ids:
            data = self.parseChall(id)
            ch_name = data['name']
            ch_cat = data['category'] if data['category'] else 'Uncategorized'

            if not self.entry.get(ch_cat):
                self.entry[ch_cat] = {}
            print(' [c] {} - {}'.format(ch_cat, ch_name))

            entries = {
                ch_name: {
                    'ID': data['id'],
                    'Points': data['value'],
                    'Description': data['description'],
                    'Solved': data['solved_by_me'] if 'solved_by_me' in data else False,
                    'Connections': data['connection_info'] if 'connection_info' in data else None,
                    'Files': data['files'],
                    'Hint': data['hints']
                }
            }

            self.entry[ch_cat].update(entries)

    def createArchive(self):
        print('\n[+] Downloading assets . . .')
        if not os.path.exists(self.title):
            os.makedirs(self.title)
        os.chdir(self.title)

        r = re.compile("[^A-Za-z0-9 .\'_-]")
        for key, val in self.entry.items():
            key = unidecode.unidecode(key)
            for keys, vals in val.items():
                if self.solved and not vals['Solved']:
                    print(keys, 'Skipping - Not solved')
                    continue

                keys = r.sub('', unidecode.unidecode(keys).strip())
                directory = '{}/{}'.format(key, keys)
                directory = directory.replace(' / ', '-').replace(' ', '_')

                if not os.path.exists(directory):
                    os.makedirs(directory)
                    print('Directory', directory, 'has been created')

                files = vals['Files'] or []
                hint = [h for h in vals['Hint'] if isinstance(h, str)]

                reamde_path = '{}/README.md'.format(directory)
                if not self.overwrite and os.path.exists(reamde_path):
                    print(keys, 'Skipping - README.md')
                    continue

                with open(reamde_path, 'w') as f:
                    f.write('#### Challenge:\n\n')
                    f.write(re.sub(
                        r'\s*Author:\s.*(\s)*', '', vals['Description'].strip()
                    ))

                    if len(files) > 0:
                        f.write(' {}'.format(", ".join(
                            map(lambda f: '[{}](./{} ":ignore")'.format(f, f),
                                map(lambda f: f.split('/')[-1].split('?')[0], files)))))

                    if vals['Connections']:
                        f.write('\n\n`{}`'.format(vals['Connections'].strip()))

                    if len(hint) > 0:
                        f.write('\n\n##### Hints:\n{}'.format(', '.join(hint)))
                    f.write(md_appendix)

                    print('%s/README.md has been created' % (directory))

                for i in files:
                    filename = i.split('/')[-1].split('?')[0]
                    print(filename, i)
                    if not os.path.exists(directory + '/' + filename):
                        resp = self.ses.get(self.url + i,
                                            stream=False,
                                            headers=self.headers,
                                            verify=False)
                        with open(directory + '/' + filename, 'wb') as f:
                            f.write(resp.content)
                            f.close()


def main():
    parser = argparse.ArgumentParser(
        description='This program dumps CTFd challenges via it\'s REST API.')
    parser.add_argument('-c', '--ctfd_url', nargs='?', required=True,
                        help='https://noob-ctfd.com')
    parser.add_argument('-u', '--username', nargs='?', required=True,
                        help='SuperHacka')
    parser.add_argument('-p', '--password', nargs='?', required=True,
                        help='LabMem#003')
    parser.add_argument('-o', '--overwrite', dest='overwrite',
                        action='store_true')
    parser.set_defaults(overwrite=False)
    parser.add_argument('-s', '--solved', dest='solved',
                        action='store_true')
    parser.set_defaults(solved=False)

    args = parser.parse_args()

    ctf = CTFdCrawl(args.username, args.password, args.ctfd_url,
                    args.overwrite, args.solved)
    ctf.parseAll()
    ctf.createArchive()


if __name__ == '__main__':
    main()
