<includeonly>{{#ifeq:{{{support|}}}|yes|{{#ifeq:{{{debugger|}}}|yes|Active|Partial}}|{{#ifeq:{{{debugger|}}}|yes|Minimal|{{#ifeq:{{{reviewer|}}}|yes|Minimal|None}}}}}}</includeonly><noinclude>
Intended for use with [[Template:Component]]. See also {{GitHub | org=scijava | repo=mediawiki-maven-info | label=scijava/mediawiki-maven-info}}.

==Examples==
<pre style="overflow:auto">
{{SupportStatus | support=yes | debugger=yes}}
</pre>
{{SupportStatus | support=yes | debugger=yes}}

<pre style="overflow:auto">
{{SupportStatus | support=yes}}
</pre>
{{SupportStatus | support=yes}}

<pre style="overflow:auto">
{{SupportStatus | debugger=yes}}
</pre>
{{SupportStatus | debugger=yes}}

<pre style="overflow:auto">
{{SupportStatus | reviewer=yes}}
</pre>
{{SupportStatus | reviewer=yes}}

<pre style="overflow:auto">
{{SupportStatus | support=no}}
</pre>
{{SupportStatus | support=no}}
</noinclude>
