#!/usr/bin/env python3
# Based on: https://github.com/ichinano/CTFdScraper

# NOTE: install requirements
# pip3 install -r requirements.txt

from requests import session
from bs4 import BeautifulSoup
import unidecode
import json
import os
import requests
import re
import sys
import argparse


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
    def __init__(self, team, passwd, url):
        self.auth = dict(name=team, password=passwd)
        self.ses = session()
        self.entry = dict()
        self.keys = 'data'
        self.url = url
        self.ch_url = self.url + '/api/v1/challenges'
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
        }

        if not self.login():
            raise Exception('Login Failed')
        print('\n[+] Collecting resources')
        self.checkVersion()

    def login(self):
        resp = self.ses.get(self.url + '/login', headers=self.headers)
        soup = BeautifulSoup(resp.text, 'lxml')
        nonce = soup.find('input', {'name': 'nonce'})

        if not nonce:
            return False
        nonce = nonce.get('value')

        self.auth['nonce'] = nonce
        self.title = soup.title.string.replace(' ', '_')

        resp = self.ses.post(self.url + '/login', data=self.auth)
        return 'incorrect' not in resp.text

    def checkVersion(self):
        resp = self.ses.get(self.ch_url, headers=self.headers)
        self.version = 'v.1.2.0' if '404' not in resp.text else 'v.1.0'

    def parseChall(self, id):
        resp = self.ses.get('{}/{}'.format(self.ch_url, id),
                            headers=self.headers).json()
        return resp['data'] if self.version == 'v.1.2.0' else resp

    def parseAll(self):
        print('[+] Finding challs')
        if self.version == 'v.1.0':
            self.ch_url = self.url + '/chals'
            self.keys = 'game'
        html = sorted(self.ses.get(self.ch_url, headers=self.headers).json()[
                      self.keys], key=lambda x: sorted(x.keys()))
        ids = [i['id'] for i in html]

        for id in ids:
            data = self.parseChall(id)
            ch_name = data['name']
            ch_cat = data['category'] if data['category'] else 'Uncategorized'

            if not self.entry.get(ch_cat):
                self.entry[ch_cat] = {}
                count = 1
                print('\n [v]', ch_cat)
            print('  {}. {}'.format(count, ch_name))

            entries = {
                ch_name: {
                    'ID': data['id'],
                    'Points': data['value'],
                    'Description': data['description'],
                    'Files': data['files'],
                    'Hint': data['hints']
                }
            }

            self.entry[ch_cat].update(entries)
            count += 1

    def createArchive(self):
        print('\n[+] Downloading assets . . .')
        if not os.path.exists(self.title):
            os.makedirs(self.title)
        os.chdir(self.title)

        r = re.compile("[^A-Za-z0-9 .\'_-]")
        for key, val in self.entry.items():
            key = unidecode.unidecode(key)
            for keys, vals in val.items():
                keys = r.sub('', unidecode.unidecode(keys).strip())
                directory = '{}/{}'.format(key, keys)
                directory = directory.replace(' / ', '-').replace(' ', '_')
                print('Directory', directory, 'has been created')
                if not os.path.exists(directory):
                    os.makedirs(directory)

                files = vals['Files']
                hint = [h for h in vals['Hint'] if isinstance(h, str)]

                with open('{}/README.md'.format(directory), 'w') as f:
                    f.write('#### Challenge:\n\n')
                    f.write(vals['Description'].strip())
                    if len(hint) > 0:
                        f.write('\n\n##### Hints:\n{}'.format(', '.join(hint)))
                    if len(files) > 0:
                        f.write('\n\n##### Files:\n{}'.format(", ".join(
                            map(lambda f: '[{}](./{} ":ignore")'.format(f, f),
                                map(lambda f: f.split('/')[-1].split('?')[0], files)))))
                    f.write(md_appendix)
                    print('%s/README.md has been created' % (directory))

                if files:
                    for i in files:
                        filename = i.split('/')[-1].split('?')[0]
                        print(filename, i)
                        if not os.path.exists(directory + '/' + filename):
                            resp = self.ses.get(self.url + i,
                                                stream=False,
                                                headers=self.headers)
                            with open(directory + '/' + filename, 'wb') as f:
                                f.write(resp.content)
                                f.close()


def main():
    parser = argparse.ArgumentParser(
        description='This program dumps CTFd challenges via it\'s REST API.')
    parser.add_argument('-c', '--ctfd_url', nargs='?',
                        help='https://noob-ctfd.com')
    parser.add_argument('-u', '--username', nargs='?', help='SuperHacka')
    parser.add_argument('-p', '--password', nargs='?', help='LabMem#003')

    args = parser.parse_args()

    ctf = CTFdCrawl(args.username, args.password, args.ctfd_url)
    ctf.parseAll()
    ctf.createArchive()


if __name__ == '__main__':
    main()
