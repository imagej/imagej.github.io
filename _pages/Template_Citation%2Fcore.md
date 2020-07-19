<span
<!-- This is a COinS tag (http://ocoins.info), which allows automated tools to parse the citation information: -->
    class="Z3988"
    title="ctx_ver=Z39.88-2004&rft_val_fmt={{urlencode:info:ofi/fmt:kev:mtx:}}book{{
      #if: {{{Journal|}}}
      |&rft.genre=article&rft.atitle={{urlencode:{{{Title|}}}}}&rft.title={{urlencode:{{{Periodical|}}}}}
      |{{
         #if: {{{IncludedWorkTitle|}}}
         |&rft.genre=bookitem&rft.atitle={{urlencode:{{{IncludedWorkTitle|}}}}}
         |&rft.genre=book
       }}&rft.title={{urlencode:{{{Title|}}}}}
    }}{{
      #if: {{{Surname1|}}} |&rft.aulast={{urlencode:{{{Surname1}}}}}
    }}{{
      #if: {{{Given1|}}} |&rft.aufirst={{urlencode:{{{Given1}}}}}
    }}{{
      #if: {{{Date|}}} |&rft.date={{urlencode:{{{Date}}}}}
    }}{{
      #if: {{{Volume|}}} |&rft.volume={{urlencode:{{{Volume}}}}}
    }}{{
      #if: {{{Issue|}}} |&rft.issue={{urlencode:{{{Issue}}}}}
    }}{{
      #if: {{{At|}}} |&rft.pages={{urlencode:{{{At}}}}}
    }}{{
      #if: {{{Edition|}}} |&rft.edition={{urlencode:{{{Edition}}}}}
    }}{{
      #if: {{{Place|}}} |&rft.place={{urlencode:{{{Place}}}}}
    }}{{
      #if: {{{PublicationPlace|}}} |&rft.place={{urlencode:{{{PublicationPlace}}}}}
    }}{{
      #if: {{{Publisher|}}} |&rft.pub={{urlencode:{{{Publisher}}}}}
    }}{{
      #if: {{{DOI|}}} |&rft_id=info:doi/{{urlencode:{{{DOI}}}}}
    }}{{
      #if: {{{PMID|}}} |&rft_id=info:pmid/{{urlencode:{{{PMID}}}}} 
    }}{{ 
      #if: {{{ISBN|}}} |&rft.isbn={{urlencode:{{{ISBN}}}}}
    }}{{
      #if: {{{ISSN|}}} |&rft.issn={{urlencode:{{{ISSN}}}}}
    }}{{
      #if: {{{URL|{{{IncludedWorkURL|}}}}}} |&rft_id={{urlencode:{{{URL|{{{IncludedWorkURL|}}}}}}}}
    }}"
><cite 
{{
  #if:{{{Ref|}}}
  |{{#ifeq:{{{Ref|}}}|none||id="{{anchorencode:{{{Ref|}}}}}"}}
  |id="CITEREF{{anchorencode:{{#if:{{{Surname1|}}}
     |{{{Surname1}}}{{{Surname2|}}}{{{Surname3|}}}{{{Surname4|}}}
     |{{{EditorSurname1|}}}{{{EditorSurname2|}}}{{{EditorSurname3|}}}{{{EditorSurname4|}}}
   }}{{{Year|{{{Date|}}}}}}}}"
}}>{{
<!--============  Author or editor and date  ============-->
  #if:{{{Surname1|}}}
  |{{
     #if: {{{Authorlink1|}}}
     |[[{{{Authorlink1}}} |{{{Surname1}}}{{
        #if: {{{Given1|}}}
        |, {{{Given1}}}
      }}]]
     |{{{Surname1}}}{{
        #if: {{{Given1|}}}
        |, {{{Given1}}}
      }}
   }}{{
     #if: {{{Surname2|}}}
     |{{
        #if: {{{Surname3|}}}
        |<nowiki>; </nowiki>
        |&#32;&amp;&#32;
      }}{{
        #if: {{{Authorlink2|}}}
        |[[{{{Authorlink2}}} |{{{Surname2}}}{{
           #if: {{{Given2|}}}
           |, {{{Given2}}}
         }}]]
        |{{{Surname2}}}{{
           #if: {{{Given2|}}}
           |, {{{Given2}}}
         }}
      }}{{
        #if: {{{Surname3|}}}
        |&#32;&amp; {{
           #if: {{{Authorlink3|}}}
           |[[{{{Authorlink3}}} |{{{Surname3}}}{{
              #if: {{{Given3|}}}
              |, {{{Given3}}}
            }}]]
           |{{{Surname3}}}{{
              #if: {{{Given3|}}}
              |, {{{Given3}}}
            }}
         }}{{
           #if:{{{Surname4|}}}
           |&#32;et al.
         }}
      }}
   }}{{
     #if: {{{Date|}}}
     |&#32;({{{Date}}})
   }}
  |{{
     #if: {{{EditorSurname1|}}}
     |{{
        #if: {{{Editorlink1|}}}
        |[[{{{Editorlink1}}} |{{{EditorSurname1}}}{{
           #if: {{{EditorGiven1|}}}
           |, {{{EditorGiven1}}}
         }}]]
        |{{{EditorSurname1}}}{{
           #if: {{{EditorGiven1|}}}
           |, {{{EditorGiven1}}}
         }}
      }}{{
        #if: {{{EditorSurname2|}}}
        |{{
           #if: {{{EditorSurname3|}}}
           |<nowiki>; </nowiki>
           |&#32;&amp;&#32;
         }}{{
           #if: {{{Editorlink2|}}}
           |[[{{{Editorlink2}}} |{{{EditorSurname2}}}{{
              #if: {{{EditorGiven2|}}}
              |, {{{EditorGiven2}}}
            }}]]
           |{{{EditorSurname2}}}{{
              #if: {{{EditorGiven2|}}}
              |, {{{EditorGiven2}}}
            }}
         }}{{
           #if: {{{EditorSurname3|}}}
           |&#32;&amp; {{
              #if: {{{Editorlink3|}}}
              |[[{{{Editorlink3}}} |{{{EditorSurname3}}}{{
                 #if: {{{EditorGiven3|}}}
                 |, {{{EditorGiven3}}}
               }}]]
              |{{{EditorSurname3}}}{{
                 #if: {{{EditorGiven3|}}}
                 |, {{{EditorGiven3}}}
               }}
            }}{{
              #if:{{{EditorSurname4|}}}
              |&#32;et al.
            }}
         }}
      }}, ed{{#if:{{{EditorSurname2|}}}|s}}.{{
        #if: {{{Date|}}}
        |&#32;({{{Date}}})
      }}
   }}
}}{{
<!--============  Title of included work  ============-->
  #if: {{{IncludedWorkTitle|}}}
  |{{
     #if:{{{Surname1|}}}{{{EditorSurname1|}}} 
     |,&#32; 
   }}{{Link
     | 1={{
           #if: {{{IncludedWorkURL|}}}
           |{{{IncludedWorkURL}}}
           |{{
              #if: {{{URL|}}}
              |{{{URL}}}
              |{{
                 #if: {{{DOI|}}}
                 |http://dx.doi.org/{{urlencode:{{{DOI}}}}}
                  |{{ 
                    #if: {{{PMID|}}} 
                    | http://www.ncbi.nlm.nih.gov/pubmed/{{urlencode:{{{PMID}}}}} 
                   }} 
               }}
            }} 
         }}
     | 2={{
           #if: {{{Periodical|}}}
           |''{{{IncludedWorkTitle}}}''
           |"{{{IncludedWorkTitle}}}"
         }}
   }}
}}{{
<!--============  Place (if different than PublicationPlace) ============-->
  #if: {{{Place|}}}
  |{{
     #ifeq: {{{Place|}}} | {{{PublicationPlace|}}}
     |
     |{{
        #if: {{{Surname1|}}}{{{EditorSurname1|}}}{{{IncludedWorkTitle|}}}{{{Periodical|}}}
        |, written at {{{Place}}}
      }}
   }}
}}{{
<!--============  Editor of compilation  ============-->
  #if: {{{EditorSurname1|}}}
  |{{
     #if: {{{Surname1|}}}
     |, {{
        #if: {{{IncludedWorkTitle|}}}
        |in&#32;
      }}{{
        #if: {{{Editorlink1|}}}
        |[[{{{Editorlink1}}} |{{{EditorSurname1}}}{{
           #if: {{{EditorGiven1|}}}
           |, {{{EditorGiven1}}}
         }}]]
        |{{{EditorSurname1}}}{{
           #if: {{{EditorGiven1|}}}
           |, {{{EditorGiven1}}}
         }}
      }}{{
        #if: {{{EditorSurname2|}}}
        |{{
           #if: {{{EditorSurname3|}}}
           |<nowiki>; </nowiki>
           |&#32;&amp;&#32;
         }}{{
           #if: {{{Editorlink2|}}}
           |[[{{{Editorlink2}}} |{{{EditorSurname2}}}{{
              #if: {{{EditorGiven2|}}}
              |, {{{EditorGiven2}}}
            }}]]
           |{{{EditorSurname2}}}{{
              #if: {{{EditorGiven2|}}}
              |, {{{EditorGiven2}}}
            }}
         }}{{
           #if: {{{EditorSurname3|}}}
           |&#32;&amp; {{
              #if: {{{Editorlink3|}}}
              |[[{{{Editorlink3}}} |{{{EditorSurname3}}}{{
                 #if: {{{EditorGiven3|}}}
                 |, {{{EditorGiven3}}}
               }}]]
              |{{{EditorSurname3}}}{{
                 #if: {{{EditorGiven3|}}}
                 |, {{{EditorGiven3}}}
               }}
            }}{{
              #if:{{{EditorSurname4|}}}
              |&#32;et al.
            }}
         }}
      }}{{
        #if: {{{IncludedWorkTitle|}}}
        |
        |, ed{{#if:{{{EditorSurname2|}}}|s}}.
      }}
   }}
}}{{
  <!--============  Periodicals  ============-->
  #if: {{{Periodical|}}}
  |{{
     #if: {{{Surname1|}}}{{{EditorSurname1|}}}
     |,&#32;
   }}{{
     #if: {{{Title|}}}
     |"{{Link
        | 1={{
              #if: {{{IncludedWorkTitle|}}}
              |{{
                 #if: {{{IncludedWorkURL|}}}
                 |{{
                    #if: {{{URL|}}}
                    |{{{URL}}}
                    |{{
                       #if: {{{DOI|}}}
                       |http://dx.doi.org/{{urlencode:{{{DOI}}}}}
                  |{{ 
                    #if: {{{PMID|}}} 
                    | http://www.ncbi.nlm.nih.gov/pubmed/{{urlencode:{{{PMID}}}}} 
                   }} 
                     }}
                  }}
               }}
              |{{
                 #if: {{{URL|}}}
                 |{{{URL}}}
                 |{{
                    #if: {{{DOI|}}}
                    |http://dx.doi.org/{{urlencode:{{{DOI}}}}}
                  |{{ 
                    #if: {{{PMID|}}} 
                    | http://www.ncbi.nlm.nih.gov/pubmed/{{urlencode:{{{PMID}}}}} 
                   }} 
                  }}
               }}
            }}
        | 2={{{Title}}}
      }}",&#32;
   }}''{{{Periodical}}}''{{
     #if: {{{Series|}}}
     |, {{{Series}}}
   }}{{
     #if: {{{PublicationPlace|}}}
     |{{
        #if: {{{Publisher|}}}
        |&#32;({{{PublicationPlace}}}<nowiki>: </nowiki>{{{Publisher}}})
        |&#32;({{{PublicationPlace}}})
      }}
     |{{
        #if: {{{Publisher|}}}
        |&#32;({{{Publisher}}})
      }}
   }}{{
     #if: {{{Volume|}}}
     |&#32;'''{{{Volume}}}'''{{
        #if: {{{Issue|}}}
        |&#x00a0;({{{Issue}}})
      }}
     |{{
        #if: {{{Issue|}}}
        |&#32;(no. {{{Issue}}})
      }}
   }}{{
     #if: {{{At|}}}
     |<nowiki>: </nowiki> {{{At}}}
   }}
  |{{
     <!--============ Anything else with a title, including books ============-->
     #if: {{{Title|}}}
     |{{
        #if: {{{Surname1|}}}{{{EditorSurname1|}}}{{{IncludedWorkTitle|}}}{{{Periodical|}}}
        |,&#32;
      }}''{{Link
        | 1={{
              #if: {{{IncludedWorkTitle|}}}
              |{{
                 #if: {{{IncludedWorkURL|}}}
                 |{{
                    #if: {{{URL|}}}
                    |{{{URL}}}
                    |{{
                       #if: {{{DOI|}}}
                       |http://dx.doi.org/{{urlencode:{{{DOI}}}}}
                  |{{ 
                    #if: {{{PMID|}}} 
                    | http://www.ncbi.nlm.nih.gov/pubmed/{{urlencode:{{{PMID}}}}} 
                   }} 
                     }}
                  }}
               }}
              |{{
                 #if: {{{URL|}}}
                 |{{{URL}}}
                 |{{
                    #if: {{{DOI|}}}
                    |http://dx.doi.org/{{urlencode:{{{DOI}}}}}
                  |{{ 
                    #if: {{{PMID|}}} 
                    | http://www.ncbi.nlm.nih.gov/pubmed/{{urlencode:{{{PMID}}}}} 
                   }} 
                  }}
               }}
            }}
        | 2={{{Title}}}
      }}''{{
        #if: {{{Volume|}}}
        |, vol. {{{Volume}}}
      }}{{
        #if: {{{Edition|}}}
        |&#32;({{{Edition}}} ed.)
      }}{{
        #if: {{{Series|}}}
        |, {{{Series}}}
      }}{{
        #if: {{{PublicationPlace|}}}
        |, {{{PublicationPlace}}}
      }}{{
        #if: {{{Publisher|}}}
        |{{
           #if: {{{PublicationPlace|}}}
           |<nowiki>:</nowiki>
           |,
         }} {{{Publisher}}}
      }}
   }}
}}{{
<!--============ Date (if no author/editor) ============-->
  #if: {{{Surname1|}}}{{{EditorSurname1|}}}
  |
  |{{
     #if: {{{Date|}}}
     |, {{{Date}}}
   }}
}}{{
<!--============ Publication date ============-->
  #if: {{{PublicationDate|}}}
  |{{
     #ifeq: {{{PublicationDate|}}} | {{{Date|}}}
     |
     |{{
        #if: {{{EditorSurname1|}}}
        |{{
           #if: {{{Surname1|}}}
           |, {{{PublicationDate}}}
           |&#32;(published {{{PublicationDate}}})
         }}
        |{{
           #if: {{{Periodical|}}}
           |, {{{PublicationDate}}}
           |&#32;(published {{{PublicationDate}}})
         }}
      }}
   }}
}}{{
<!--============ Page within included work ============-->
  #if: {{{Periodical|}}}
  |
  |{{
     #if: {{{At|}}}
     |, {{{At}}}
   }}
}}{{
<!--============ Misc. Identifier ============-->
  #if: {{{ID|}}}
  |, {{{ID}}}
}}{{
<!--============ ISBN ============-->
  #if: {{{ISBN|}}}
  |, ISBN {{{ISBN}}}
}}{{
<!--============ ISSN ============-->
  #if: {{{ISSN|}}}
  <!--  |, [[International Standard Serial Number|ISSN]] [http://worldcat.org/issn/{{{ISSN}}} {{{ISSN}}}]-->
  |, ISSN [http://worldcat.org/issn/{{{ISSN}}} {{{ISSN}}}]
}}{{
<!--============ OCLC ============-->
  #if: {{{OCLC|}}}
  <!--  |, [[OCLC]] [http://worldcat.org/oclc/{{urlencode:{{{OCLC}}}}} {{{OCLC}}}]-->
  |, OCLC [http://worldcat.org/oclc/{{urlencode:{{{OCLC}}}}} {{{OCLC}}}]
}}{{
<!--============ PMID ============--> 
  #if: {{{PMID|}}} 
  |, PMID {{{PMID}}} 
}}{{ 
<!--============ DOI ============-->
  #if: {{{DOI|}}}
  |{{
     #if: {{{URL|}}}{{{IncludedWorkURL|}}}
     <!--     |, [[Digital object identifier|doi]]:[http://dx.doi.org/{{urlencode:{{{DOI}}}}} {{{DOI}}}]-->
     |, doi:[http://dx.doi.org/{{urlencode:{{{DOI}}}}} {{{DOI}}}]
     |<span class="printonly">, DOI {{{DOI}}}</span>
   }}
}}{{
<!--============ URL and AccessDate ============-->
  #if: {{{URL|}}}
  |{{
     #if: {{{Title|}}}{{{IncludedWorkTitle|}}}
     |<span class="printonly">, &lt;{{
                                      #if: {{{IncludedWorkURL|}}}
                                      |{{{IncludedWorkURL}}}
                                      |{{{URL}}}
                                    }}&gt;</span>
     |, &lt;{{
              #if: {{{IncludedWorkURL|}}}
              |{{{IncludedWorkURL}}}
              |{{{URL}}}
            }}&gt;
   }}{{
     #if: {{{AccessDate|}}}
     | .&#32;Retrieved on {{date|{{{AccessDate}}}}}
   }}
}}</cite></span>
<noinclude></noinclude>
