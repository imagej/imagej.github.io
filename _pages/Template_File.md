<includeonly>{{#if: {{{1|}}}
|{{#if: {{{3|}}}
 |{{ContentBox|File|{{{3}}}|subtitle={{{1}}}|description={{{2}}}|lang={{{lang|text}}}|color=#204A87|color2=#729fcf}}
 |{{Error|File|3. unnamed}}
 }}
|{{Error|File|1. unnamed}}
}}</includeonly>
<noinclude>
Use this template to show a file box with some content.

== Parameters ==

;1. unnamed: Add the filename.
;2. unnamed (optional): Add some description (optional as can be blank).
;3. unnamed: Add the code/file content.

== Usage ==

The following:

 <nowiki>{{File|filename||<pre>
file content
  this
    that
</pre>}}</nowiki>

generates:

{{File|filename||<pre>
file content
  this
    that
</pre>}}


</noinclude>
