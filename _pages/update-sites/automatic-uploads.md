---
mediawiki: Automatic_Update_Site_Uploads
title: Automatic Update Site Uploads
section: Extend:Update Sites
project: /software/imagej2
nav-links: true
nav-title: Automatic Uploads
---

{% include notice icon="info" content='This guide is intended for maintaining non-core update sites by automating builds with [GitHub Actions](https://docs.github.com/en/actions).
- The [core update sites](/update-sites/core-uploads) are updated manually or automatically. Automated update is performed with [GitHub Actions](https://docs.github.com/en/actions).
- GitHub Actions is useful because it can freely build any open source project with minimal effort.' %}

## Requirements

-   An open-source project hosted on [GitHub](/develop/github)
-   An [initialized upload password](/update-sites/setup#creating-a-hosted-update-site).

## Additional resources

-   [SciJava Github Actions setup instructions](https://imagej.net/develop/github-actions) or the general [GitHub Actions user guide](https://docs.github.com/en/actions/quickstart)

## Automatic Uploads via GitHub Actions

GitHub Actions can be used to automatically build a repository in response to code changes. To ease the maintenance of ImageJ update sites, we can use GitHub Actions to automatically upload the latest version of a site. This is done by creating a `.github/workflows/release.yml` file in your update site's GitHub repository that does the following:

1.  Create a fresh ImageJ2.app
2.  Build the update site's repository and move the required artifacts (e.g. `.jars`) to their intended locations in the ImageJ2.app
3.  Upload the local update site state to your Wiki update site

As a starting point you can copy the following `.github/workflows/release.yml` :

```yml
name: Release to Update Site

on:
  push:
    branches: [master]  # Trigger the workflow on push to the master branch

jobs:
  build_release:
    runs-on: ubuntu-latest
    env:
      IJ_DOWNLOAD_URL: https://downloads.imagej.net/fiji/latest/fiji-linux64.zip
      WIKI_USER: YOUR_USER_NAME
      UPDATE_PASS: ${{ secrets.UPDATE_PASS }}  # DO NOT WRITE your password here
      UPDATE_SITE: YOUR_UPDATE_SITE_NAME
    steps:
      - name: Checkout
        uses: actions/checkout@v2
      - name: Build with Maven
        run: mvn -B package
      - name: Install ImageJ/Fiji
        run: |
          curl --silent -O ${IJ_DOWNLOAD_URL}
          unzip fiji-linux64.zip
          ./Fiji.app/ImageJ-linux64 --headless --update edit-update-site ${UPDATE_SITE} https://sites.imagej.net/${UPDATE_SITE}/ "webdav:${WIKI_USER}:${UPDATE_PASS}" .
      - name: Install in ImageJ/Fiji (with Maven)
        run: mvn -B install -Dscijava.app.directory=./Fiji.app -Ddelete.other.versions=true -Dscijava.ignoreDependencies=true
      - name: Release to ImageJ update site
        run: |
          ./Fiji.app/ImageJ-linux64 --headless --update upload-complete-site --force ${UPDATE_SITE}
```

Don't forget to replace the `WIKI_USER` and `UPDATE_SITE` variables by your informations.

### Encrypting your password

To upload to your wiki update site, you will need to provide GitHub Actions with a `UPDATE_PASS` environment variable, which should evaluate to the [upload password](/update-sites/setup#creating-a-hosted-update-site) of the Wiki account performing the upload. To do so securely, follow the instructions on [creating encrypted secrets for a repository](https://docs.github.com/en/actions/reference/encrypted-secrets#creating-encrypted-secrets-for-a-repository).

### Non-Mavenized Files

GitHub Actions is capable of building many languages besides Java. If you cannot use Maven with a `scijava.app.directory` then you need to replace the following line of your `.github/workflows/release.yml`:

```shell
mvn -B install -Dscijava.app.directory=./Fiji.app -Ddelete.other.versions=true -Dscijava.ignoreDependencies=true
```

with a sequence of commands that will move your build artifacts to the appropriate `./Fiji.app/jars` or `./Fiji.app/plugins` directory, as appropriate for your update site.

This is also true if you have custom scripts, macros, etc... if these files are not present in the correct locations of the local ImageJ2.app, they will appear to have been deleted.

## Caveats

{% include notice icon="warning" content="**USE CAUTION HERE**

1.  You are configuring GitHub Actions to upload the state of an ImageJ installation to your update site. The ImageJ2.app that will be uploaded is located at `./Fiji.app` with respect to the current working directory of the virtual machine GitHub Actions is running on. If your build artifacts are not located in the `./Fiji.app/jars` or `./Fiji.app/plugins` directory, or you don't manually copy scripts to the correct location, ImageJ will see these items as having been deleted—**effectively removing all content from your update site.** You can mitigate this danger by customizing your `release.yml` to download your own update site into the base ImageJ2.app; only changes to the update site state will be uploaded.
2.  By default—building the master branch of your repository—your update site will be updated with **every change** to the source code. Although we encourage the master branch to be \"[release ready](/develop/releasing#phase-2-on-master)\", a safer practice would be to configure GitHub Actions to [only build specific events](https://docs.github.com/en/actions/reference/events-that-trigger-workflows)—and set it to build [release versions](/develop/architecture#reproducible-builds) only—e.g. with a release version integration branch.
3.  Using the Maven-based `release.yml` as suggested implies that you are conforming to the managed dependencies of the parent pom.xml. If you are not staying up-to-date with the ImageJ and Fiji update sites (by using the latest ImageJ or Fiji [bill of materials](/develop/architecture#bill-of-materials)) then this automation may break your own update site." %}
