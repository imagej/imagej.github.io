---
mediawiki: Unit_tests_for_ImageJ1
title: Unit tests for ImageJ
project: /software/imagej
---

There are a [substantial number of unit tests](/news/2011-10-07-unit-tests-for-imagej-1-45) to exercise [ImageJ](/software/imagej) functionality. You can find them in the {% include github org='imagej' repo='ij1-tests' label='ij1-tests repository' %}:

```shell
git clone git://github.com/imagej/ij1-tests
```

There is a [Travis](/develop/travis) job [here](https://travis-ci.com/imagej/ij1-tests) that automatically runs the tests with each new version of ImageJ.

### Running the tests

If you wish to run the unit tests manually, you can do so from the command line:

```shell
cd ij1-tests
mvn clean test
```

Or from Eclipse:

1.  Import the `ij1-tests` project using {% include bc path='File | Import Existing Maven Projects'%} and choosing the `ij1-tests/pom.xml` file.
2.  Right-click the `ij1-tests` project, {% include bc path='Run As | JUnit Test'%}.

### Using a different version of ImageJ

You can change which version of ImageJ is tested by overriding the `imagej1.version` property:

```shell
mvn -Dimagej1.version=1.48a clean test
```

Or whichever version you wish to use (of [those listed here](https://maven.scijava.org/content/groups/public/net/imagej/ij/)). The unit tests were created circa 1.44, and do not compile correctly with earlier versions of ImageJ.
