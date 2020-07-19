<includeonly>[http://maven.imagej.net/index.html#nexus-search;gav~{{{g|}}}~{{{a|}}}~{{{v|}}}~{{{p|}}}~{{{c|}}}~kw,versionexpand {{{label|{{#if:{{{g|}}}|{{{g|}}}|}}{{#if:{{{a|}}}|&#58;{{{a|}}}|}}{{#if:{{{v|}}}|&#58;{{{v|}}}|}}{{#if:{{{p|}}}|&#58;{{{p|}}}|}}{{#if:{{{c|}}}|&#58;{{{c|}}}|}}}}}]<nowiki />
</includeonly><noinclude>
==Usage==
<pre>
{{Maven
| g     =
| a     =
| v     =
| p     =
| c     =
| label =
}}
</pre>

==Examples==

Link to all versions of a particular artifact by specifying <code>g</code> (i.e., <code>groupId</code>) and <code>a</code> (i.e., <code>artifactId</code>):
<pre>
{{Maven | g=net.imagej | a=imagej}}
</pre>
{{Maven | g=net.imagej | a=imagej}}

Link to a specific version by also specifying <code>v</code> (i.e., <code>version</code>):
<pre>
{{Maven | g=net.imagej | a=imagej | v=2.0.0-rc-30}}
</pre>
{{Maven | g=net.imagej | a=imagej | v=2.0.0-rc-30}}

You can also specify <code>p</code> for packaging, and <code>c</code> for classifier, if you need those options:
<pre>
{{Maven | g=net.imagej | a=imagej-launcher | p=nar | c=amd64-Linux-gcc-executable}}
</pre>
{{Maven | g=net.imagej | a=imagej-launcher | p=nar | c=amd64-Linux-gcc-executable}}
</noinclude>
