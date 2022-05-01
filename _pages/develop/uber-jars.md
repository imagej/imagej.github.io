---
title: Uber-JAR
section: Extend:Development:Guides
---
{% include notice icon="warning" content='We recommend *against* using uber-JARs. They introduce many problems for downstream consumers.' %}

An **uber-JAR**—also known as a **fat JAR** or **JAR with dependencies**—is a JAR file that contains not only a Java program, but embeds its dependencies as well. This means that the JAR functions as an "all-in-one" distribution of the software, without needing any other Java code. (You still need a Java runtime, and an underlying operating system, of course.)



## Approaches

There are three common methods for constructing an uber-JAR:

-   **Unshaded.** Unpack all JAR files, then repack them into a single JAR.
    -   **Pro:** Works with Java's default class loader.
    -   **Con:** Files present in multiple JAR files with the same path (e.g., `META-INF/services/javax.script.ScriptEngineFactory`) will overwrite one another, resulting in faulty behavior.
    -   **Tools:** [Maven Assembly Plugin](http://maven.apache.org/plugins/maven-assembly-plugin/), [Classworlds Uberjar](http://classworlds.codehaus.org/uberjar.html)
-   **Shaded.** Same as unshaded, but rename (i.e., "shade") all packages of all dependencies.
    -   **Pro:** Works with Java's default class loader. Avoids some (not all) dependency version clashes.
    -   **Con:** Files present in multiple JAR files with the same path (e.g., `META-INF/services/javax.script.ScriptEngineFactory`) will overwrite one another, resulting in faulty behavior. As a workaround, if you use [Maven](/develop/maven), you can add the following lines to the shade plugin section of the POM to apply the appending tranform to multiple resources with the same name (e.g. `META-INF/json/org.scijava.plugin.Plugin` or `META-INF/json/mpicbg.spim.data.generic.sequence.ImgLoaderIo`). Both are annotations necessary to find interface or abstract class implementation during runtime across JARs:
            <transformers combine.children="append">
              <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                <resource>META-INF/json/org.scijava.plugin.Plugin</resource>
              </transformer>
            </transformers>

        If you need to append more than one file, you unfortunately need to list multiple **transformer implementations** as wildcards are not allowed. For appending two files, the entry would look like this:

            <transformers combine.children="append">
                <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                    <resource>META-INF/json/org.scijava.plugin.Plugin</resource>
                </transformer>
                <transformer implementation="org.apache.maven.plugins.shade.resource.AppendingTransformer">
                    <resource>META-INF/json/mpicbg.spim.data.generic.sequence.ImgLoaderIo</resource>
                </transformer>
            </transformers>

        An example of a full maven-shade-plugin can be found [here](https://github.com/PreibischLab/multiview-reconstruction/blob/96d0f417638dab108f942e49ffa26024b48053f0/pom.xml#L271) (single entry) and [here](https://github.com/PreibischLab/BigStitcher/blob/eb1cc4af404ae83715135894920ed9c3b5e42385/pom.xml#L208) (multiple entries).
    -   **Tools:** [Maven Shade Plugin](http://maven.apache.org/plugins/maven-shade-plugin/)
-   **JAR of JARs**. The final JAR file contains the other JAR files embedded within.
    -   **Pro:** Avoids dependency version clashes. All resource files are preserved.
    -   **Con:** Needs to bundle a special "bootstrap" classloader to enable Java to load classes from the wrapped JAR files. Debugging class loader issues becomes more complex. Using getResource() calls when there are MANY contained jars can be problematic, due to locking inside misc.sun.URLClassPath.
    -   **Tools:** [Eclipse JAR File Exporter](http://help.eclipse.org/luna/index.jsp?topic=%2Forg.eclipse.jdt.doc.user%2Freference%2Fref-export-jar.htm), [One-JAR](http://one-jar.sourceforge.net/).

## Discussion

**Advantages:** A single JAR file is simpler to deploy. There is no chance of mismatched versions of multiple JAR files. It is easier to construct a Java classpath, since only a single JAR needs to be included.

**Disadvantages:**

-   Every time you need to update the version of the software, you must redeploy the entire uber-JAR (e.g., [ImageJ2](/software/imagej2) is \~68 MB as of May 2015). If you bundle individual JAR components, you need only update those that changed. This issue is of particular relevance to Java applications deployed via Java Web Start, since it automatically downloads the latest available version of each JAR dependency; in that case, your application startup time will suffer if you use the uber-JAR.
-   You cannot cherry-pick only the JARs containing the functionality you need, so your application's footprint may suffer from bloat.
-   If downstream code relies on any of the same dependencies which are embedded in an unshaded uber-jar, you may run into trouble (e.g., [`NoSuchMethodError`](/learn/troubleshooting#nosuchmethoderror-or-noclassdeffounderror) for unshaded uber-JARs) with multiple copies of those dependencies on your classpath, especially if you need to use a different version of that dependency than is bundled with the uber-JAR.

As you can see, it is important to understand how use of the uber-JAR will affect your application. In particular, Java applications will likely be better served using the individual component JARs, ideally managed using a dependency management platform such as [Maven](http://maven.apache.org/) or [Ivy](http://ant.apache.org/ivy/). But for non-Java applications, the uber-JAR may be sufficient to your needs.

## See also

-   [What is an uber-jar?](http://stackoverflow.com/q/11947037) on Stack Overflow
-   [The Elusive Uber Jar](http://dig.floatingsun.net/the-elusive-uber-jar/)
