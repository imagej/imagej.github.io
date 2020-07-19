<includeonly><div style="overflow:hidden"><table class="metadata plainlinks ambox {{#switch:{{{type|}}}
| serious        = ambox-serious
| content        = ambox-content
| maintenance    = ambox-style
| notice         = ambox-notice
| #default       = ambox-notice
}}">
<tr>
<td class="ambox-image">
{{#ifeq:{{{image}}}|none
|<!-- no image cell -->
| {{#switch:{{{image|{{{type|}}}}}}
| serious        = [[Image:Stop-sign.png|40px]]
| content        = [[Image:Important-sign.png|40px]]
| maintenance    = [[Image:Maintenance-sign.png|40px]]
| notice         = [[Image:Warning-sign.png|40px]]
| blank          = <!-- empty image cell -->
| #default       = {{{image|[[Image:Information-sign.png|40px]]}}}
}}
}}
</td>
<td> {{{text}}} </td>
{{#if:{{{imageright|}}}
  <td class="ambox-imageright"> {{{imageright}}} </td>
}}

</tr>
</table></div></includeonly>
<noinclude>


----

'''Notwithstanding any statement on this page, Template:Ambox is from [http://en.wikipedia.org/wiki/Template:Ambox Wikipedia] and as such is licensed under the [http://www.gnu.org/licenses/fdl.txt GNU Free Documentation License].'''


This is the '''ambox''' or '''article message box''' meta template.

It is used to create ''article message box'' templates. It offers several different colours, uses default images if no image parameter is given and it has some other features.

=== Usage ===

Simple usage example:

<pre>
{{ambox | text = Some text.}}
</pre>

{{ambox | text = Some text.}}


Complex example:

<pre>
{{ambox
| image = [[Image:Fiji-logo-1.0-256x256.png|38px]]
| text  = The message body text.
}}
</pre>

{{ambox
| image = [[Image:Fiji-logo-1.0-256x256.png|38px]]
| text  = The message body text.
}}

==== Default images ====

The following examples use different '''type''' parameters but use no image parameters thus they use the default images for each type.

{{ambox
| type  = serious
| text  = type=<u>serious</u> – Serious issues
}}
{{ambox
| type  = content
| text  = type=<u>content</u> – Content issues
}}
{{ambox
| type  = maintenance
| text  = type=<u>maintenance</u> – Style issues
}}
{{ambox
| type  = notice
| text  = type=<u>notice</u> – Article notices
}}

=== Parameters ===

List of all parameters:

<pre>
{{ambox
| type  = serious / content / maintenance / notice
| image = none / blank / [[Image:Some image.svg|40px]]
| imageright = [[Image:Some image.svg|40px]]
| text  = The message body text. 
}}
</pre>

'''type'''
:If no '''type''' parameter is given the template defaults to type '''notice''' which is used for "article notices". That means it gets a blue side bar like in the simple usage example above.

'''image'''
:'''No parameter''' = If no '''image''' parameter is given the template uses a default image. Which default image it uses depends on the '''type''' parameter. 
:'''An image''' = Should be an image with usual wiki notation. 40px - 50px width are usually about right depending on the image height to width ratio. For example: 
::<code><nowiki>[[Image:Unbalanced scales.svg|40px]]</nowiki></code>
:'''none''' = Means that no image is used.
:'''blank''' = Means that no image is used but an empty area the same size as a default image is used, which means that text in the message box gets aligned well with other article message boxes. (See the "special" examples above.)

'''imageright'''
:'''No parameter''' = If no '''imageright''' parameter is given then no image is shown on the right side.
:'''An image''' = Should be an image with usual wiki notation. 40px - 50px width are usually about right depending on the image height to width ratio. For example: 
::<code><nowiki>[[Image:Nuvola apps bookcase.png|40px]]</nowiki></code>
:'''Anything''' = Any other object that you want to show on the right side.

'''text'''
:The message body text.

=== Technical details ===

If you need to use special characters in the text parameter then you need to escape them like this: 

<pre>
{{ambox
| text  = <div>
Equal sign = and a start and end brace { } works fine as they are. 
But here is a pipe {{!}} and two end braces &lt;nowiki>}}&lt;/nowiki>. 
And now a pipe and end braces &lt;nowiki>|}}&lt;/nowiki>.
</div>
}}
</pre>

{{ambox
| text  = <div>
Equal sign = and a start and end brace { } works fine as they are. 
But here is a pipe {{!}} and two end braces <nowiki>}}</nowiki>. 
And now a pipe and end braces <nowiki>|}}</nowiki>.
</div>
}}


This template uses CSS classes for most of its looks, thus it is fully "skinnable".

The CSS classes can also be used directly in a wikitable. Like this:

<pre>
{| class="ambox ambox-content"
|-
| class="ambox-image" | [[Image:Emblem-important.svg|40px]]
| Some text.
|}
</pre>

{| class="ambox ambox-content"
|-
| class="ambox-image" | [[Image:Emblem-important.svg|40px]]
| Some text.
|}


Internally this meta template uses HTML markup instead of wiki markup for the table code. That is the usual way we make meta templates since wiki markup has several drawbacks. For instance it makes it harder to use [[m:Help:ParserFunctions|parser functions]] and special characters in parameters. 

For more technical details see the [[{{TALKPAGENAME}}|talk page]] and the "See also" links below.

</noinclude>
