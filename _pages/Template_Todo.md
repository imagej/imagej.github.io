<table class="{{Talk other|demospace={{{demospace|}}}|tmbox tmbox-notice|ombox ombox-notice}} {{#ifeq:{{{small|}}}|yes|mbox-small}} {{#ifeq:{{{collapsed|}}}|yes|collapsible collapsed}} t-todo" style="border-collapse: separate; border-spacing: 4px; {{{style|}}}">
<tr><th class="mbox-text" style="text-align: left; padding: 1px;">{{
  #if: {{{inner|}}}
  | <!--nothing-->
  | <span class="noprint plainlinks" style="float: right; text-align: right; font-size: {{#ifeq:{{{small|}}}|yes|100|88}}%; font-weight: normal;">[{{fullurl:{{#rel2abs:{{{list|./to do}}}|{{{target|}}}}}|action=edit{{
    #ifeq: {{{nopreload}}} | yes | | &preload=Template:Tasks/Preload}}
  }} {{
    #ifeq: {{{small|}}} | yes | e | edit
  }}]&thinsp;'''&middot;'''&thinsp;[{{fullurl:{{#rel2abs:{{{list|./to do}}}|{{{target|}}}}}|action=history}} {{
    #ifeq: {{{small|}}} | yes | h | history
  }}]&thinsp;'''&middot;'''&thinsp;[{{fullurl:{{#rel2abs:{{{list|./to do}}}|{{{target|}}}}}|action=watch}} {{
    #ifeq: {{{small|}}} | yes | w | watch
  }}]&thinsp;'''&middot;'''&thinsp;[{{fullurl:{{#rel2abs:.}}|action=purge}} {{
    #ifeq: {{{small|}}} | yes | r&#160; | refresh&#160;
  }}]</span>
}}{{
  #ifeq: {{{image|}}} | none
  | <!--nothing-->
  | [[File:{{{image|Stock post message.svg}}}|{{#ifeq:{{{small|}}}|yes|20|25}}px]]
}} [[Wikipedia:To-do list|To-do{{#ifeq:{{{small|}}}|yes||&#32;list}}]]{{
  #ifeq: {{#ifeq:{{{smallfor|}}}|yes|no|{{{small|}}}}}|yes||&#32;for {{{for|[[:{{{target|{{SUBJECTPAGENAME}}}}}]]}}}
}}:</th><td class="mbox-empty-cell"></td></tr>{{
  #if: {{{above|}}} | <tr class="todo-abovebelow"><td colspan="2">{{{above}}}</td></tr>
}}
<tr><td class="todo-box" colspan="2" style="{{Talk other|demospace={{{demospace|}}}|background: #FFFAEF;}} border:1px dotted gray; padding: 2px 4px;" >{{#if:{{{maxheight|}}}|<div style="max-height: {{{maxheight}}}; overflow: auto;">}}
{{{inner|{{
  #ifexist: {{ #rel2abs: {{{list|./to do}}} | {{{target|}}} }}
  | <!--/to do exists, show it-->&#x20;
{{ {{ #rel2abs: {{{list|./to do}}} | {{{target|}}} }} }}
  | <!--it doesn't--> ''To-do list is empty: remove <nowiki>{{To do}}</nowiki> tag or click on edit to add an item.''
}}}}}{{#if:{{{maxheight|}}}|</div>}}
</td></tr>
{{
  #if: {{{below|}}} | <tr class="todo-abovebelow"><td colspan="2">{{{below}}}</td></tr>
}}{{
  #if: {{{1|}}} | <tr class="todo-priority"><td colspan="2" style="text-align: right; font-size: smaller;">'''Priority {{{1}}} {{ #ifeq: {{{1}}} | 1 | (top) }}'''</td></tr>
}}
</table><includeonly>{{
  #ifeq: {{{nocats}}} | yes | | {{{category|[[Category:Wikipedia pages with to-do lists|{{PAGENAME}}]]}}}{{
    #if: {{{inner|}}} | | {{
      #ifexist: {{#rel2abs:{{{list|./to do}}}|{{{target|}}}}} | | {{#switch:{{NAMESPACE}}
       |{{ns:2}}
       |{{ns:3}}=
       |#default=[[Category:Wikipedia pages with to-do lists, unused]]
       }}
    }}
  }}
}}</includeonly><noinclude>
This template is a copy of [http://en.wikipedia.org/wiki/Template:Todo Template:Todo] on Wikipedia. Please go there for further information.
</noinclude>
