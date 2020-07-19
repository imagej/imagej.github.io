<includeonly><table style="text-align: center;"  {{#ifeq: {{{float}}} | right | align="right" | }}>{{#if: {{{1|}}} | <tr><td>{{{1}}}</td></tr> | }}{{#if: {{{2|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{2}}}</td></tr> | }}{{#if: {{{3|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{3}}}</td></tr> | }}{{#if: {{{4|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{4}}}</td></tr> | }}{{#if: {{{5|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{5}}}</td></tr> | }}{{#if: {{{6|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{6}}}</td></tr> | }}{{#if: {{{7|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{7}}}</td></tr> | }}{{#if: {{{8|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{8}}}</td></tr> | }}{{#if: {{{9|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{9}}}</td></tr> | }}{{#if: {{{10|}}} | <tr><td>{{downarrow | {{{color|}}}}}</td></tr> <tr><td>{{{10}}}</td></tr> | }}</table></includeonly><noinclude>This template provides a BreadCrumb trail through menu paths and similar hierarchical structures.
==Usage==
For example, typing:
<pre>The {{key|L}} key is the shortcut for {{bcvert|Plugins|Utilities|Find Commands}}.</pre>
will be rendered as:
The {{key|L}} key is the shortcut for {{bcvert|Plugins|Utilities|Find Commands}}

Up to 10 menu elements can be used:
<pre>{{bcvert|Menu1|Menu2|Menu3|(...)|Menu9|Command}}</pre>
will be rendered as:
{{bcvert|Menu1|Menu2|Menu3|(...)|Menu9|Command}}

If the parameter '''color''' is set to white, arrows will be displayed white otherwise the default arrow is displayed filled with black for better visibility.
<pre>{{bcvert|color=white|Menu1|Menu2|Menu3|(...)|Menu9|Command}}</pre>
will be rendered as:
{{bcvert|color=white|Menu1|Menu2|Menu3|(...)|Menu9|Command}}

If the parameter '''float''' is set to right, the table will float right, as though [http://www.w3schools.com/tags/att_table_align.asp align: right] was set:
<pre>{{bcvert|float=right|Menu1|Menu2|Menu3|(...)|Menu9|Command}}</pre>
will be rendered (inline) as:
{{bcvert|float=right|Menu1|Menu2|Menu3|(...)|Menu9|Command}}






















==Attribution==
This template is inspired by the [https://wiki.documentfoundation.org/Template:Breadcrumb https://wiki.documentfoundation.org], released under the [http://creativecommons.org/licenses/by-sa/3.0/ Creative Commons Attribution-ShareAlike 3.0 Unported License], adjusted to match the style used in the [http://imagej.nih.gov/ij/docs/guide/ ImageJ User Guide].
</noinclude>
