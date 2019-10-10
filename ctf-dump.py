#!/usr/bin/env python3
# Based on: https://github.com/ichinano/CTFdScraper

### requirements
# pip3 install unidecode

from requests import session
from bs4 import BeautifulSoup
import unidecode
import json
import os
import requests
import re
import sys

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

    def parseSolves(self, id):
        resp = self.ses.get('{}/{}/solves'.format(self.ch_url, id),
                            headers=self.headers).json()
        return resp['data'] if self.version == 'v.1.2.0' else resp

    def parseAll(self):
        print('[+] Finding challs')
        if self.version == 'v.1.0':
            self.ch_url = self.url + '/chals'
            self.keys = 'game'
        html = sorted(self.ses.get(self.ch_url,
                                   headers=self.headers).json()[self.keys],
                      key=lambda x: sorted(x.keys()))
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

    def createArchive(self,with_solves=True):
        print('\n[+] Downloading assets . . .')
        if not os.path.exists(self.title):
            os.makedirs(self.title)

        os.chdir(self.title)
        with open('challs.json', 'w') as f:
            f.write(json.dumps(self.entry, sort_keys=True, indent=4))

        r = re.compile("[^A-Za-z0-9 .\'_-]")
        for key, val in self.entry.items():
            key = unidecode.unidecode(key)
            for keys, vals in val.items():
                keys = r.sub('', unidecode.unidecode(keys).strip())
                directory = '{}/{} [{} pts]'.format(key, keys, vals['Points'])
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
                            map(lambda f: '[{}](./{})'.format(f, f),
                                map(lambda f: f.split('/')[-1].split('?')[0], files)))))
                    f.write(md_appendix)

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
                if with_solves:
                    solves_data = self.parseSolves(vals['ID'])
                    with open('{}/solves.json'.format(directory), 'w') as sf:
                        sf.write(json.dumps(solves_data, sort_keys=True, indent=4))




def main():
    url = input('CTFd URL : ')
    user = input('Username : ')
    passwd = input('Password : ')
    ctf = CTFdCrawl(user, passwd, url)
    ctf.parseAll()
    ctf.createArchive()


if __name__ == '__main__':
    main()
