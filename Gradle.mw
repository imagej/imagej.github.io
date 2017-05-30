[http://gradle.org/getting-started-gradle-java/ Gradle] is an open-source build system using a Groovy-based script syntax as a succinct alternative to the XML of [http://ant.apache.org/ Ant] or [[Maven]].

The ImageJ core artifacts are built with Maven, but can also be consumed in a Gradle build script.

==Sample ImageJ build.gradle==

Contributed<sup>[https://github.com/imagej/tutorials/issues/24 1]</sup> by {{Person|reckbo}}

<source lang="groovy">
buildscript {
    repositories {
        maven {
            url "https://plugins.gradle.org/m2/"
        }
    }
    dependencies {
        classpath "io.spring.gradle:dependency-management-plugin:0.5.4.RELEASE"
    }
}
apply plugin: "io.spring.dependency-management"

repositories {
    jcenter()
    maven {
          url "http://maven.imagej.net/content/groups/public/"
    }
}
dependencyManagement {
    imports {
        mavenBom 'net.imagej:pom-imagej:14.1.0'
    }
}

dependencies {
    compile 'net.imagej:imagej'
}

</source>
