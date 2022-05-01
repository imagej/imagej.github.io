---
mediawiki: Unit_tests_for_ImageJ1
title: Unit tests for ImageJ
project: /software/imagej
---

There are a [substantial number of unit tests](/news/2011-10-07-unit-tests-for-imagej-1-45) to exercise [ImageJ](/software/imagej) functionality. You can find them in the {% include github org='imagej' repo='ImageJ' label='ImageJ repository' %} in the `tests` directory.

### Running the tests

If you wish to run the unit tests manually, you can do so from the command line:

```shell
git clone https://github.com/imagej/ImageJ
cd ImageJ
mvn test
```

Or from Eclipse:

1.  Import the `ImageJ` project using {% include bc path='File | Import Existing Maven Projects' %} and choosing the `ImageJ/pom.xml` file.
2.  Right-click the `ImageJ` project, {% include bc path='Run As | JUnit Test' %}.
