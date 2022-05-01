---
section: Extend:Development:Tools:IDEs
title: Developing ImageJ2 on the command line
project: /software/imagej2
---

This article explains how to install and configure command line tools for use with [ImageJ2](/software/imagej2) development.

## Install and configure command line tools

<div class="tab">
  <button class="tablinks" onclick="openTab(event, 'windows')">Windows</button>
  <button class="tablinks" onclick="openTab(event, 'macos')">MacOS</button>
  <button class="tablinks" onclick="openTab(event, 'linux')">Linux</button>
</div>

<div id="windows" class="tabcontent" markdown="1">
{%- include icon name='Windows' size='32px' -%}
<br/>

Install [Git](/develop/git), [Maven](/develop/maven), and Java SE using [Chocolatey](https://chocolatey.org/):

    choco install -y git maven jdk8

We also heartily recommend installing [Cygwin](https://www.cygwin.com/):

    choco install -y cyg-get

</div>
<div id="macos" class="tabcontent" markdown="1">
{%- include icon name='MacOS' size='32px' -%}
<br/>

Install [Git](/develop/git) and [Maven](/develop/maven) using [Homebrew](http://brew.sh/):

    brew install git maven bash-completion

Download and install [OpenJDK](https://www.azul.com/downloads/?package=jdk).

</div>
<div id="linux" class="tabcontent" markdown="1">
{%- include icon name='Linux' width='32px' -%}
<br/>

    sudo apt-get install default-jdk git maven

</div>


## Download the source

    git clone git://github.com/imagej/imagej2

See the [Source Code](/develop/source) page for further details.

## Build the source

    cd imagej2
    mvn

## Launch the program

    mvn -Pexec

### Launching alternative user interfaces

{% include notice icon="warning" content='Alternative UIs are experimental and still at "proof of concept" stage. The `swing` UI is semi-functional, but the other two (`swing-mdi` and `awt`) are largely non-functional, mentioned here solely for completeness.' %}

    mvn -Dscijava.ui=swing -Pexec
    mvn -Dscijava.ui=swing-mdi -Pexec
    mvn -Dscijava.ui=awt -Pexec

## See also

-   [Dotfiles](/develop/dotfiles) if you want to twink out your shell
