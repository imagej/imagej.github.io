---
title: Set up IDE for Groovy
section: Extend:Scripting:Languages
---

## Introduction

As Groovy builds upon [Java](/develop/plugins), it can be used in a full fledged IDE with Fiji to have autocompletion and a more powerful environment than the script editor.

## Set up the IDE

### Requisites

In order to set up this whole guide, you will need 4 parts :

-   [Fiji](https://fiji.sc)
-   An IDE, this guide will use [IntelliJ Community](https://www.jetbrains.com/idea/download/), but it should also be possible using Eclipse
-   [Groovy](https://groovy.apache.org/download.html) will need to be installed as well. For installation on Linux, please follow [this guide](https://groovy-lang.org/install.html)
-   [Java](https://www.azul.com/downloads/?package=jdk)

{% include notice icon="info" content='If you want to run the scripts directly in Fiji, you will have to install the same Groovy version than Fiji. At the moment, that version is 3.0.4.' %}

### Configure the project

When first starting the IDE, select Create New Project and configure it correctly.
In case the **Project SDK** is not automatically set, select the Java version installed previously. The **Groovy library** will have to be set up and pointed to the version you just downloaded by clicking on *Create*.

<img src="/media/scripting/groovy/configured_project.png" alt="fig:configured_project.png" width="550"/>

You can then select your project name and location and then click on Finish which will create the project and folder.

### Add Fiji dependencies

You are now presented with your newly created project in the main editor window of your IDE. However, Fiji is not yet imported in your project and won't have autocompletion. To do so, go to **File > Project Structure > Modules > Dependencies** and click on the **+** icon and add JAR dependencies. Then select the JAR and the plugin folder of your Fiji.

<img src="/media/scripting/groovy/add_jar_dependencies.png" alt="fig:add_jar_dependencies.png" width="550"/>

### Create new script

Now click on **File > New > Groovy Script** to create a new script and you can start typing
```groovy
import ij.
```

and you should start seeing autocompletion. If it doesn't work, check again the previous steps.

### Run the script in Fiji

#### With the same groovy version than Fiji

If you have installed and configured your IDE with the same Groovy version than Fiji, you should be able to run your script directly through IntelliJ.

#### With any groovy version

Another solution to run the script in Fiji is to open the same groovy script in the script editor. If you modify the file in the IDE, save it and then select back the script editor, the file will detect that it has been modified and will ask for refresh. You can then run the script by clicking on the **run** button