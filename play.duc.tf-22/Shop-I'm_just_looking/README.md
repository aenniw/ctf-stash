#### Challenge:

We've seen some vulnerability scanning activity against us!

What was the name of the tool used?

Flag format: Name of the tool used, case insensitive

---

#### Solution:

Looking at the provided [JSON](../Shop-SetupDisclaimer/DownUnderShop.JSON), I noticed a lot of records having `"referer": "null",` with timestamps exactly one second apart.

After filtering out their URLs I got:

```
/wp-content/uploads/simple-file-list/nuclei.php
/CFIDE/administrator/enter.cfm
/cgi-bin/test/test.cgi
/favicon.ico
/nuclei.txt
/wp-content/plugins/elementor/
/zp-core/setup/index.php
/wp-content/plugins/gtranslate/
/include/nuclei.txt
/pandora_console/mobile/
/install.php
/api/v4/projects
/signup
/metrics
/MyErrors.log
/error.log
/npm-debug.log
/production.log
/plugin/build-metrics/getBuildStats?label=%22%3E%3Csvg%2Fonload%3Dalert(1337)%3E&range=2&rangeUnits=Weeks&jobFilteringType=ALL&jobFilter=&nodeFilteringType=ALL&nodeFilter=&launcherFilteringType=ALL&launcherFilter=&causeFilteringType=ALL&causeFilter=&Jenkins-Crumb=4412200a345e2a8cad31f07e8a09e18be6b7ee12b1b6b917bc01a334e0f20a96&json=%7B%22label%22%3A+%22Search+Results%22%2C+%22range%22%3A+%222%22%2C+%22rangeUnits%22%3A+%22Weeks%22%2C+%22jobFilteringType%22%3A+%22ALL%22%2C+%22jobNameRegex%22%3A+%22%22%2C+%22jobFilter%22%3A+%22%22%2C+%22nodeFilteringType%22%3A+%22ALL%22%2C+%22nodeNameRegex%22%3A+%22%22%2C+%22nodeFilter%22%3A+%22%22%2C+%22launcherFilteringType%22%3A+%22ALL%22%2C+%22launcherNameRegex%22%3A+%22%22%2C+%22launcherFilter%22%3A+%22%22%2C+%22causeFilteringType%22%3A+%22ALL%22%2C+%22causeNameRegex%22%3A+%22%22%2C+%22causeFilter%22%3A+%22%22%2C+%22Jenkins-Crumb%22%3A+%224412200a345e2a8cad31f07e8a09e18be6b7ee12b1b6b917bc01a334e0f20a96%22%7D&Submit=Search
/LetsEncrypt/Index?fileName=/etc/passwd
/phpmyadmin/
```

`Aenniw` noticed that the list contained `nuclei` several times. Quick Google search led to [https://github.com/projectdiscovery/nuclei-templates](https://github.com/projectdiscovery/nuclei-templates), hence `nuclei` was actually the flag.

---

<details><summary>FLAG:</summary>

```
nuclei
```

</details>
<br/>
