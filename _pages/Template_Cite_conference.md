<includeonly><cite style="font-style:normal">{{#if: {{{author|}}}{{{last|}}}
  |{{#if: {{{authorlink|}}}
    |[[{{{authorlink}}}|{{#if: {{{last|}}}
      |{{{last}}}{{#if: {{{first|}}}
        |, {{{first}}}
      }}
      |{{{author}}}
    }}]]
    |{{#if: {{{last|}}}
      |{{{last}}}{{#if: {{{first|}}}
        |, {{{first}}}
      }}
      |{{{author}}}
    }}
  }}
}}{{#if: {{{author|}}}{{{last|}}}
  |{{#if: {{{coauthors|}}}
    |<nowiki>;</nowiki>&#32;{{{coauthors}}}
  }}
}}{{#if: {{{date|}}}
  |&#32;({{{date}}})
  |{{#if: {{{year|}}}
    |{{#if: {{{month|}}}
      |&#32;({{{month}}} {{{year}}})
      |&#32;({{{year}}})
    }}
  }}
}}{{#if: {{{author|}}}{{{last|}}}
  |.
}} "{{#if: {{{url|}}}
  |[{{{url}}} {{{title}}}]
  |{{{title}}}
}}"{{#if: {{{format|}}}
  | &#32;({{{format|}}})
}}{{#if: {{{conference|}}}
  | &#32;in {{#if: {{{conferenceurl|}}}
  |[{{{conferenceurl}}} ''{{{conference}}}'']
  |''{{{conference}}}''
}}
}}.{{#if: {{{editor|}}}
  |&#32;{{{editor}}}
}}{{#if: {{{others|}}}
  |, {{{others}}}
}}{{#if: {{{booktitle|}}}
  |&#32;''{{{booktitle}}}''
}}{{#if: {{{volume|}}}
  | &#32;'''{{{volume}}}'''
}}{{#if: {{{pages|}}}
  |<nowiki>:</nowiki> {{{pages}}}
}}{{#if: {{{edition|}}}
  |, {{{edition}}}
}}{{#if: {{{publisher|}}}
  |, {{#if: {{{location|}}}
    |{{{location}}}:&#32;
  }}{{{publisher}}}
}}{{#if: {{{doi|}}} | . doi:[http://dx.doi.org/{{{doi}}} {{{doi}}}]
}}{{#if: {{{id|}}}
  |. {{{id}}}
}}{{#if: {{{oclc|}}} | . [[OCLC]] [http://worldcat.org/oclc/{{urlencode:{{{oclc}}}}} {{{oclc}}}]
}}{{#if: {{{accessdate|}}}
  |.<span class="reference-accessdate"> Retrieved on [[{{{accessdate}}}]]</span>
}}.{{#if:{{{quote|}}}
  | &#32;"{{{quote}}}"
}}</cite><!--

This is a COinS tag (http://ocoins.info), which allows automated tools to parse the citation information:
  --><span class="Z3988" title="ctx_ver=Z39.88-2004<!--
  -->&rft_val_fmt=info%3Aofi%2Ffmt%3Akev%3Amtx%3Abook<!-- Field descriptions: http://www.openurl.info/registry/docs/mtx/info:ofi/fmt:kev:mtx:book
  -->&rft.genre=proceeding<!--
  -->&rft.btitle={{urlencode:{{{booktitle|}}}}}<!--
  -->&rft.atitle={{urlencode:{{{title|}}}}}<!--
  -->{{#if: {{{last|}}}      | &rft.aulast={{urlencode:{{{last}}}}}      }}<!--
  -->{{#if: {{{first|}}}     | &rft.aufirst={{urlencode:{{{first}}}}}    }}<!--
  -->{{#if: {{{author|}}}    | &rft.au={{urlencode:{{{author}}}}}        }}<!--
  -->{{#if: {{{date|}}} 
       | &rft.date={{urlencode:{{{date}}}}}
       | {{#if: {{{year|}}}  | &rft.date={{urlencode:{{{year}}}}} }}     }}<!--
  -->{{#if: {{{edition|}}}   | &rft.edition={{urlencode:{{{edition}}}}}  }}<!--
  -->{{#if: {{{publisher|}}} | &rft.pub={{urlencode:{{{publisher}}}}}    }}<!--
  -->{{#if: {{{location|}}}  | &rft.place={{urlencode:{{{location}}}}}   }}<!--
  -->{{#if: {{{pages|}}}     | &rft.pages={{urlencode:{{{pages}}}}}      }}<!--
  -->{{#if: {{{volume|}}}    | &rft.series={{urlencode:{{{volume}}}}}    }}<!--
  -->{{#if: {{{doi|}}}       | &rft_id=info:doi/{{urlencode:{{{doi}}}}}  }}<!--
  -->{{#if: {{{url|}}}       | &rft_id={{urlencode:{{{url}}}}}           }}<!--
  -->"><span style="display: none;">&nbsp;</span></span></includeonly><noinclude>
{{documentation}}{{pp-template|small=yes}}
</noinclude>
