---
title: Maven - Frequently Asked Questions
---

# What does the POM version mean?

The {% include github org='imagej' repo='example-legacy-plugin' branch='master' path='pom.xml' label='pom.xml' %} of [example-legacy-plugin](https://github.com/imagej/example-legacy-plugin/) inherits from a parent called {% include github org='scijava' repo='pom-scijava' branch='master' path='pom.xml' label='pom-scijava' %}. This parent POM defines and configures many things so that the POMs of individual plugin projects are shorter (i.e., so they don't have to repeat things) and more consistent (i.e., so they do not forget to define crucial metadata).

The version of `pom-scijava` (`14.0.0` as of this writing) indicates the version of that parent POM. We occasionally improve the parent POM, adding and tweaking it. When we do so, its version increases. It is suggested to leave the version that same as what's in `example-legacy-plugin`, since that refers to the latest version. Future `1.x` versions of ImageJ will be backwards compatible, so if you later notice that we have updated `example-legacy-plugin` to e.g. `15.0.0`, you can (optionally) update your plugin to that version as well.

The version of `example-legacy-plugin` itself (`0.1.0-SNAPSHOT` as of this writing) is the version of your plugin. This string is appended to the JAR file name (e.g., example-legacy-plugin-0.1.0-SNAPSHOT.jar), so that you can differentiate between multiple versions of your plugin. Use whatever versioning scheme you want.

However, once you become more comfortable with Maven, we suggest using [a SNAPSHOT version during development](http://stackoverflow.com/questions/5901378/what-exactly-is-a-maven-snapshot-and-why-do-we-need-it), and a release (i.e., non-SNAPSHOT) version when distributing your plugin. The reason is to avoid two different JAR files both called `my-plugin-1.2.3` but with different contents. (This is part of what Maven calls [reproducible builds](/develop/architecture#reproducible-builds).)

For example, while you develop your plugin, you might use the version `1.0.0-SNAPSHOT` to indicate that this is not the final `1.0.0` version but leads up to it. Once you are happy with the plugin in its current form, switch to `1.0.0`. Note, however, that you will cause problems if you later change the sources of the final `1.0.0` version (i.e., without first advancing the version in the `pom.xml` file).

# How are dependency versions determined?

In many `pom.xml` files which extend `pom-scijava`, you can see that the dependency versions are omitted. The versions are defined (or "managed") by the pom-scijava parent configuration as part of its [Bill of Materials](/develop/architecture#bill-of-materials)—e.g., {% include github org='scijava' repo='pom-scijava' tag='pom-scijava-14.0.0' path='pom.xml\#L218-L219' label='here' %} is where the ImageJ version is defined.

-   Browse the latest `pom-scijava` {% include github org='scijava' repo='pom-scijava' branch='master' path='pom.xml' label='here' %}.
-   Browse the available versions of ImageJ [here](https://maven.scijava.org/content/groups/public/net/imagej/ij/).

# How do I determine which Maven projects (i.e., dependencies) I actually need?

One way to check is using the dependency plugin like so:

```shell
mvn dependency:analyze
```

This will tell you:

1.  Dependencies you declared but do not actually use; and
2.  Dependencies you did not declare directly, but actually need.

Note that this will only work if your project compiles successfully. In other words, it is easier to start with "too many" dependencies and pare down, rather than trying to "build up" from zero.

# What's this: *Property 'scijava.app.directory' unset; Skipping copy-jars*

This is part of the {% include github org='scijava' repo='scijava-maven-plugin' label='scijava-maven-plugin' %} (enabled for you by pom-scijava). As you suspected, it copies your plugin's `.jar` file together with its dependencies to an application `jars` or `plugins` folder. To do so, you have to provide the path to your application (e.g. `Fiji.app`) as an additional argument to Maven:

```shell
mvn -Dscijava.app.directory=YourPath/Fiji.app
```

You can cause this to happen automatically by creating a file `$HOME/.m2/settings.xml` where `$HOME` is your home directory, with the following contents:

```xml
<settings>
		<profiles>
				<profile>
						<id>imagej</id>
						<activation>
								<file>
										<exists>${env.HOME}/Desktop/Fiji.app</exists>
								</file>
						</activation>
						<properties>
								<scijava.app.directory>${env.HOME}/Desktop/Fiji.app</scijava.app.directory>
						</properties>
				</profile>
		</profiles>
</settings>
```

With such user-wide settings in place, all your Maven builds will automatically copy the build artifacts into your Fiji installation in `$HOME/Desktop/Fiji.app`. Of course, you can change this path to whatever you like.

# My software depends on a `.jar` file that is not available via Maven!

Write to the [Image.sc Forum](http://forum.image.sc/) seeking assistance. The best solution is to get your dependency deployed to the [SciJava Maven repository](/develop/project-management#maven).

See [Playing Tradeoffs with Maven](https://www.cloudbees.com/blog/playing-trade-offs-maven) for an in-depth discussion of various solutions to this issue.

# Can I call *svnversion* via Maven?

Typically you want to do that to put the current revision into an About box or something similar.

In general, you can call any needed Ant functionality using the [maven-antrun-plugin](http://maven.apache.org/plugins/maven-antrun-plugin/). However, for the About box, there is a much better solution:

The pom-scijava parent uses the buildnumber-maven-plugin to embed the SCM revision and date in the JAR manifest.

Your About dialog box can access the information by adding a dependency on *scijava-common* like this:

    <dependencies>
      <dependency>
        <groupId>org.scijava</groupId>
        <artifactId>scijava-common</artifactId>
      </dependency>
    </dependencies>

and then using code like this:
```java
import org.scijava.util.VersionUtils;

...
	String version = VersionUtils.getVersion(MyBeautifulPlugin.class);
```

# How do I make my modified project available to a depending project using Maven?

See [Using snapshot couplings during development](/develop/architecture#using-snapshot-couplings-during-development).

# How can I run individual tests with Maven?

As described [here](http://maven.apache.org/surefire/maven-surefire-plugin/examples/single-test.html):

```shell
mvn -Dtest='TestCircle#mytest' test
```

# Where can I find more information about Maven?

See the [Maven](/develop/maven) page!
