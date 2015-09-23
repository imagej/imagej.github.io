{{db-g7}}

{{Documentation subpage}} __NOTOC__
== Usage ==
: {{tlx|Documentation subpage}}
: or
: {{tlx|Documentation subpage |&#91;&#91;{{var|Page where the documentation [[Wikipedia:Transclusion|transcluded]]}}&#93;&#93;}}

===Userbox documentation===
To set this template to use "userbox" and "userbox page" rather than "{{lc:{{ns:Template}}}}" and "{{lc:{{ns:Template}}}} page" or "{{lc:{{ns:User}}}} template" and "{{lc:{{ns:User}}}} template page", use:
: {{tlx|Userbox documentation subpage}}
: or
: {{tlx|Userbox documentation subpage |&#91;&#91;{{var|userbox page}}&#93;&#93;}}

===Text customization===
The parameters {{para|text1}} and/or {{para|text2}} can be used to set the text of, respectively, the template's first and second lines. If ''text1'' is set but not ''text2'', both lines' text will derive from ''text1'':
{{Hidden begin |showhide=left |title=With ''text1'' and ''text2''}}
<code><nowiki>{{Documentation subpage |text1='''''text1 appears here''''' |text2='''''text2 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text1='''''text1 appears here''''' |text2='''''text2 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}
{{Hidden end}}
{{Hidden begin |showhide=left |title=With ''text2'' only}}
<code><nowiki>{{Documentation subpage |text2='''''text2 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text2='''''text2 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}
{{Hidden end}}
{{Hidden begin |showhide=left |title=With ''text1'' only}}
<code><nowiki>{{Documentation subpage |text1='''''text1 appears here'''''}}</nowiki></code>
{{Documentation subpage |[''page''] |text1='''''text1 appears here''''' |override={{lc:{{SUBPAGENAME}}<!-- Hack to allow example to appear, even when viewed from [[Template:Documentation subpage]] -->}}}}
{{Hidden end}}

== Display ==
This template should normally be placed at the top of /doc pages. It changes output depending on where it is viewed:
* On a /doc page, it displays a box explaining template documentation and links to the template page.
* On other pages&nbsp;– i.e. pages transcluding the /doc page&nbsp;– the template will not show. The template page itself (which contains <code>{{tl|Documentation}}</code>) will automatically note that the documentation is [[Wikipedia:Transclusion|transcluded]] from a subpage.

== Functions ==
In addition to its message, the template adds pages to [[:Category:Template documentation pages]], [[:Category:User documentation pages]], or similar (named after the subject space), but only for documentation pages in namespaces with the subpage feature. It defaults the [[m:Help:Categories#Sort order|sort key]] to the page name without namespace: Template:Foo, for example, would be sorted as "Foo", i.e. under "F".

== See also ==
{{Documentation/see also}}

<includeonly>{{#ifeq:{{SUBPAGENAME}}|sandbox |
| <!--Categories below here, please; interwikis to Wikidata.-->
[[Category:Template documentation| ]]
[[Category:Template namespace templates]]

[[tn:Template:Documentation subpage]]
}}</includeonly>
