In order to start using Kotlin to develop plugins we need to ensure that the Annotation are pre processed so that ImageJ can display the shortcuts in the menu's

To accomplish that the following code need to be added to your pom:

<sub>

<execution>
    <id>kapt</id>
    <goals>
        <goal>kapt</goal>
    </goals>
    <configuration>
        <sourceDirs>
            <sourceDir>src/main/kotlin</sourceDir>
            <sourceDir>src/main/java</sourceDir>
        </sourceDirs>
        <annotationProcessorPaths>
            <annotationProcessorPath>
                <groupId>net.imagej</groupId>
                <artifactId>imagej</artifactId>
                <version>2.0.0-rc-68</version>
            </annotationProcessorPath>
        </annotationProcessorPaths>
    </configuration>
</execution>

</sub>

and example can also be found in https://github.com/imagej/example-imagej-command-kotlin/pom.xml

If gradle is your built system of choice, then the following code need to be added to your build.gradle:

<sub>

plugins {
    id "org.jetbrains.kotlin.kapt" version "1.3.10"
}

dependencies {
    kapt 'net.imagej:imagej:2.0.0-rc-68'
}

</sub>

and example can also be found in https://github.com/imagej/example-imagej-command-kotlin/build.gradle
