{{DevelopMenu | tools}}This article explains how to install and configure command line tools for use with [[ImageJ]] development.

== Install and configure command line tools ==

<div style="overflow: hidden">
<tabs>
<tab name="Windows">
[[File:Win.png | x32px]] '''Windows'''

Install [[Git]], [[Maven]], and Java SE using [https://chocolatey.org/ Chocolatey]:
<source lang="bash">
choco install -y git maven jdk8
</source>
We also heartily recommend installing [https://www.cygwin.com/ Cygwin]:
<source lang="bash">
choco install -y cyg-get
</source>
</tab>
<tab name="OS X">
[[File:Osx.png | x32px]] '''OS X'''

Install [[Git]] and [[Maven]] using [http://brew.sh/ Homebrew]:
<source lang="bash">
brew install git maven bash-completion
</source>
Download and install [http://www.oracle.com/technetwork/java/javase/downloads/ Java SE] from Oracle.
</tab>
<tab name="Linux">
[[File:Tux.png | x32px]] '''Linux'''

<source lang="bash">
sudo apt-get install default-jdk git maven
</source>
</tab>
</tabs>
</div>

== Download the source ==
<source lang="bash">
git clone git://github.com/imagej/imagej
</source>
See the [[Source Code]] page for further details.

== Build the source ==
<source lang="bash">
cd imagej
mvn
</source>

== Launch the program ==
<source lang="bash">
mvn -Pexec
</source>

=== Launching alternative user interfaces ===
{{Warning | Alternative UIs are experimental and still at "proof of concept" stage. The <code>swing</code> UI is semi-functional, but the other two (<code>swing-mdi</code> and <code>awt</code>) are largely non-functional, mentioned here solely for completeness.}}
<source lang="bash">
mvn -Dscijava.ui=swing -Pexec
mvn -Dscijava.ui=swing-mdi -Pexec
mvn -Dscijava.ui=awt -Pexec
</source>

== See also ==
* [[Dotfiles]] if you want to twink out your shell

[[Category:Development]]
[[Category:IDEs]]
