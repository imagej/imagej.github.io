The Fiji/ImageJ2 teams are pretty busy these days to finalize the first non-beta version of ImageJ2. Quite a few things have changed in Fiji itself as a consequence, most of them behind the scenes (our apologies when things break, and our heartfelt thanks for all your help to stabilize this project).

In this context, as of today, Fiji switches its editor to the ImageJ2 script editor. A lot of effort has gone into improving the Fiji Script Editor in the ImageJ2 context, most of it behind the scenes: there is [http://jenkins.imagej.net/job/SciJava-common-javadoc/javadoc/org/scijava/script/package-frame.html a consistent, elegant and powerful scripting framework] now, forming the basis of all of ImageJ2's scripting capability, including the support for the legacy ImageJ 1.x macro language.

The main benefit is that the script editor is now fully plug 'n play: adding the .jar file implementing a new scripting language will automatically add it to the script editor language menu; even custom syntax highlighting can be added that way.

The biggest bonus for users, however, is that you can use the ''@Parameter'' framework for painless user interaction, even from ImageJ 1.x macros! Example:

<source lang="java">
// @String(label = "What is your first name?") name
print("Hello, " + name + "!");
</source>

Enjoy!

[[Category:News]]
[[Category:ImageJ2]]
