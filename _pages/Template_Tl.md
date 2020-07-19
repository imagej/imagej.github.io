<includeonly><nowiki>{{</nowiki>[[Template:{{{1}}}|{{{1}}}]]{{#if:{{{2|}}}|&#124;{{{2}}}}}{{#if:{{{3|}}}|&#124;{{{3}}}}}{{#if:{{{4|}}}|&#124;{{{4}}}''...''}}<nowiki>}}</nowiki></includeonly><noinclude>
This template displays a link to a template, with its corresponding <nowiki>{{</nowiki> and <nowiki>}}</nowiki> brackets, for easy display, and for copying and pasting.

== Examples ==
;Templates without parameters
* &#123;{tl|sources}} would generate {{tl|sources}}
;Templates with unnamed parameters
* &#123;{tl|date|{{#time:F j, Y}}}} would generate {{tl|date|{{#time:F j, Y}}}}
;Templates with named parameters, or an equals sign (=) in the text
* &#123;{tl|press release|2=url=http://en.wikinews.org/}} would generate {{tl|press release|2=url=http://en.wikinews.org/}}

== Notes ==
* You can include up to 5 extra parameters (not including the template name)
* If an extra parameter has text with an equals sign on it, you need to add "2=", "3=", etc. before the text and after the "|"
