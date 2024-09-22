---
title: Set up IDE for Groovy
section: Extend:Scripting:Languages
project: /software/fiji
nav-links: true
---

## Introduction

As Groovy builds upon [Java](/develop/plugins), it can be used in a full fledged [IDE](/develop/ides) to have autocompletion and a more powerful environment than the [script editor](/scripting/script-editor).

## Set up the IDE

### Requisites

In order to set up this whole guide, you will need 4 parts:

-   [Fiji](/downloads)
-   An [IDE](/develop/ides). This guide will use [IntelliJ IDEA Community](/develop/intellij), but it should also be possible using [Eclipse](/develop/eclipse).
-   [Groovy](https://groovy.apache.org/download.html) will need to be installed as well. For installation on Linux, please follow [this guide](https://groovy-lang.org/install.html)
-   [Java](https://www.azul.com/downloads/?package=jdk)

{% include notice icon="info" content='If you want to run the scripts directly in Fiji, you will have to install the same Groovy version that Fiji does. This can be found by looking at the groovy file in your Fiji installation's jars folder.' %}

### Configure the project

When first starting the IDE, select "Create New Project" and configure it correctly.

In case the **Project SDK** is not automatically set, select the Java version installed previously. The **Groovy library** will have to be set up and pointed to the version you just downloaded by clicking on {% include button label="Create" %}.

{% include img src="configured_project" width="550px" %}

You can then select your project name and location and then click on {% include button label="Finish" %} which will create the project and folder.

### Add Fiji dependencies

You are now presented with your newly created project in the main editor window of your IDE. However, Fiji is not yet imported in your project and won't have autocompletion. To do so, go to {% include bc path="File | Project Structure | Modules | Dependencies" %} and click on the {% include button label="+" %} button and add JAR dependencies. Then select the JAR and the plugin folder of your Fiji.

{% include img src="add_jar_dependencies" width="550px" %}

### Create new script

Now click on {% include bc path="File | New | Groovy Script" %} to create a new script and you can start typing
```groovy
import ij.
```

and you should start seeing autocompletion. If it doesn't work, check again the previous steps.

### Run the script in Fiji

#### With the same groovy version than Fiji

If you have installed and configured your IDE with the same Groovy version that Fiji has, you should be able to run your script directly through IntelliJ.

#### With any groovy version

Another solution to run the script in Fiji is to open the same groovy script in the script editor. If you modify the file in the IDE, save it and then select back the script editor, the file will detect that it has been modified and will ask for refresh. You can then run the script by clicking on the {% include button label="Run" %} button.
