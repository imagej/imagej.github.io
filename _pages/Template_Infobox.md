<includeonly>{| class="infobox" cellspacing="5" style="max-width: 31em; font-size: 90%; text-align: left; float: right; border: 1px solid #a0a0a0;"
! colspan="2" style="text-align: center; font-size: 130%;" | <div style="float: left">{{{logo|}}}</div>{{{title|{{{name|{{PAGENAME}}}}}}}} ({{{software|}}})<div style="clear: left;"></div>
|-
{{#if:{{{author|}}}|
! Author
{{!}} {{{author|}}}
{{!}}-
}}
{{#if:{{{update site|}}}|
! Update site
{{!}} [[Following_an_update_site|{{{update site|}}}]]
{{!}}-
}}
{{#if:{{{screenshot|}}}|
! Screenshot
{{!}} {{{screenshot|}}}
{{!}}-
}}


! Maintainer
{{!}} {{{maintainer|}}}
{{!}}-

{{#if:{{{filename|}}}|
! File
{{!}} {{{filename|}}}
{{!}}-
}}
{{#if:{{{source|}}}|
! Source
{{!}} {{{source|}}}
{{!}}-
}}
{{#if:{{{released|}}}|
! Initial release
{{!}} {{{released|}}}
{{!}}-
}}
{{#if:{{{latest version|}}}|
! Latest version
{{!}} {{{latest version|}}}
{{!}}-
}}
{{#if:{{{status|}}}|
! Development status
{{!}} {{{status|}}}
{{!}}-
}}
{{#if:{{{category|}}}|
! Category
{{!}} {{{category|}}}
{{!}}-
}}
{{#if:{{{website|}}}|
! Website
{{!}} {{{website|}}}
{{!}}-
}}
|}</includeonly>

<noinclude>This template is a sidebar for displaying key statistics about a plugin.

==Usage==

<pre>
{{Infobox
| name                   =
| software               =
| update site            =
| author                 =
| maintainer             = 
| filename               =
| source                 =
| released               =
| latest version         =
| status                 =
| category               =
| website                =
| tutorials              =
}}
</pre>

==Example==
{{Infobox
| name                   = My plugin
| software               = Software name
| update site            = Java-8
| author                 = John Smith ([mailto:john@smith.org john@smith.org])
| logo                   = [[Image:fiji-icon.png|96px]]
| screenshot             = A screenshot of typical usage
| maintainer             = Bob Doe ([mailto:bob@doe.org bob@dod.org])
| filename               = [http://example.org/some.class some.class] (xx,xxx Bytes)
| source                 = [http://example.org/some.java some.java] (xx,xxx Bytes)
| released               = 01 January 1900
| latest version         = 31 December 1999
| status                 = stable, not active
| category               = fancy examples
| website                = [http://example.org]
| tutorials              = Mr Smith
}}
<pre style="overflow:auto">
{{Infobox
| name                   = My plugin
| software               = Software name
| update site            = Java-8
| author                 = John Smith ([mailto:john@smith.org john@smith.org])
| logo                   = [[Image:fiji-icon.png|96px]]
| maintainer             = Bob Doe ([mailto:bob@doe.org bob@dod.org])
| filename               = [http://example.org/some.class some.class] (xx,xxx Bytes)
| source                 = [http://example.org/some.java some.java] (xx,xxx Bytes)
| released               = 01 January 1900
| latest version         = 31 December 1999
| status                 = stable, not active
| category               = fancy examples
| website                = [http://example.org]
| tutorials              = Mr Smith
}}
</pre>

{{Clear}}
[[Category:Boxes]]
</noinclude>
