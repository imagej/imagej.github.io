= Updater V1 technical details =

I'll use this page to document the changes made to the ImageJ Updater in the about to be released version called V1.

== What's different ==
* Added a check whether Java version supports the HTTPS certificates.
* Depending on what's supported, the updater will use HTTPS or HTTP links for the update sites on imagej.net (and throw a warning in case HTTPS is not supported)
* Uploading via HTTPS is working now, both basic and digest authentication supported
* The updater is smarter about updating URLs of official sites (= listed on the list of available update sites) in case they change remotely
** It shows a approval dialog for activated update sites, when the URL changed in the official list of update sites.
** Supports migration from http to https for sites.imagej.net.

== Previous version ==
[[http://www.plantuml.com/plantuml/uml/fLDDZnCn3BtFh_1nLvfMg-K41xJLIaYBu092ukh6xjIGEAF4qsdvzSm7gcYcG2MEjfxVUtbsdh9XiYxuoiGymql0Xjz_QGcD4yXOVLjriigzQ0CFwyV7zKDzxi-meVrw_GhkieJMoqwOxgjBdjNRWlWDv1WOsiGjk3sxxxbgCPauQL4DDWSKZrlFdyKuLoun6iCxyPoVe_ViJA8kDGh0e39FBf25m00K5HFqyeCtIXkYMHW7dWCQbuQAyRyJ_ZVLh-S758KvSiXYVCjemrRe9ROkAUIfy36s40-SVhDBaFzWR1clx42vhm69vd17RCLAiynDAwBOguz8Bqfy7C9_diwX2-V45dilwf7swySFO_SJ8qtNbHYfkcnU4xyq3dS1pUrXUmB5mFMKJ1BYyPteHyuJy56oYJRtfOth0WtRlBDpzF_-6djKyWmz9Xs4SWqkwiwBirmziL8N_4y0 src]]
[[File:UpdaterV0.png]]

Issues:
* locally saved update sites will just override the ones coming from the list of available update sites (matching by name), therefore remotely changed URLs will not reach the user
* always using HTTP by default
* no check if HTTPS is supported, adding an HTTPS address will throw error

== New version ==
 [[http://www.plantuml.com/plantuml/uml/pPHDRzim38Rl_XKyjaLIhDkj68O67VOnf4FHDC2khCGuN6L9e-Yqtg-VFzOQSGmukmtmHQ_9H-Gha5T9KRGiNAQiZk1hWJbzMqUBIWBSd7xEIvwd9_Ovl3b_--xyOlQgTs6rV55_S9AuY8utJFOqsmVDFmp8bv12GH258fWjcSUKHHHbmn6zmcA7xF31qOgLqY7i4pjAry4vCih1mzbPJJH2g3GTV0agrJAWPP_tSZOCgpD_t2mRzOxGjZKBeStsn74-MjlTl-AnWhxStz-krieEBhlcMs5LnXX4fvrxGl706_2X8q4wDbDe8vIsVMqfGwEyGnsy_05gy28rYpqhe-FVjF1sOMs76uID9QfKdqbx-TYyA1HHw5KVxM8Ak-VzXf__zfb8ceXR2HfCS9cGbk87wHCst23xlgPZSWkId9R1e6iixFwI-p_wAl2HLgNGTomeBOJMdd-Lz0y5zMtKj4JQWE24FHXC1BuvSG8V5CeMFGEq5amelPASlbJgGeWGTYITMHRI-7LJGmWd1QhPmaFLNZrhcSAMca529uIs0dhcfEppquoy7Op0-_dyq2IpHP-FxQSxsZ4zDM7hksNwoEX2_hgX0Bq5ooawh8uOD8pHLJMcYqalpXonveHSGDjB2s-lsrrR5lr33jA6Qt2Sd9D2EQndOldKNbb7xVPYdwSPcE0tZescx8gyBGlt1m00 src]]
[[File:UpdaterV1.png]]

== Update Check on Startup ==
* this is the `onEvent` Method of the `DefaultUpdateService` which is called when the ImageJ UI is shown. It now includes a check for changed URLs of active update sites. 
[[http://www.plantuml.com/plantuml/uml/bPDXZfim48N_Smeka0jKLRKK76rKBo0mhVeBkMPMiTQnqNYWrw-9qwYaHNH_yjwRZtco_UH98aqNav0c0sat3f8WpS-Wtb9dq_PgZqa1ht8o5EqMSDOAqiEd63mwZ8PFFwGusUHH3S5k5Au87o6X5ZUHYlGSXBkJt2Fhk8KPi86BjiDVu8-7mv_H_9dbNthHDIKh-kfut4BwivlC49ayIBW7RjZBgInwdWdMR46LjDzG4-opih1SoRzlWRIlqH4eWe4x9KaxkyUicqgmN8JMlCepSQhARNW1CnWtxfSks5V6gtgxyLdEK0BzTFYMEsj1_S-guLZugMI9GbY4epRWSsTCd5xzwi4Bmt5e9nGomohoB4JTTgJDxyjt5Tff71tIAfdDKXlvmq2husq-InzxB4BNy5kflP9TNMI2PPyvM-7lg7WIN7fwSOD-rJ2yWuX04zgWzABg5_LVxwr6Tncfyu32HVdsDX-CrMROdMwf9x33T36_0000 src]]
[[File:UpdateCheckStartupSequence.png]]

== Command line usage ==
<source>ImageJ --update refresh-update-sites --simulate</source>
<source>ImageJ --update refresh-update-sites</source>
<source>ImageJ --update refresh-update-sites --updateall</source>

== Relevant PRs ==
# [https://github.com/imagej/imagej-updater/pull/71 V1 imagej-updater PR]
# [https://github.com/imagej/imagej-ui-swing/pull/81 V1 imagej-swing-ui PR]
# [https://github.com/imagej/imagej-plugins-uploader-webdav/pull/3 V1 imagej-plugins-uploader-webdav PR]

== Relevant Issues ==
* [https://github.com/imagej/imagej-updater/issues/70 Issue for new updater]
* [https://github.com/imagej/imagej-updater/issues/66 Update cached update site links issue]
