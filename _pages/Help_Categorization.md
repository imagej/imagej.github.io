Categorization is one of MediaWiki's features to organize content and is described in detail e.g. in  [[wikipedia:Wikipedia:Categorization|Wikipedia]] or [http://meta.wikimedia.org/wiki/Help:Category Meta-Wiki]. If you want to use categories in this wiki, please read at least the [[Help:Categorization#Guidelines|Guidelines]].

==Basic concepts==

* Every page (article, help page, category page, ...) can be in an arbitrary number of categories. E.g. ''Black plastic pen'' could belong to ''Made of plastic'', ''Black'' '''and''' ''Writing utensil''. Imagine it just like tagging something. The categories to which an article belongs are listed at the bottom of the article page.
* Categories themselves can be in other categories. E.g. ''Black plastic pen'' (article page) is in ''Black'' and ''Black'' (as a category) is in ''Color''. ''Black'' therefore becomes a '''subcategory''' of ''Color''.
* Every category has its page, prefixed by '''Category:''' where the categories (refered to as subcategories) and articles which belong to it are listed. However, a category has no page unless it's created. For a more detailed explanation see [[Help:Categorization#Usage|below]].
* Categories form (with the system of subcategorization) '''trees''' and therefore have some kind of hierarchy. E.g. there can be a category ''Property'' with several subcategories like ''Color'', ''Size'' or ''Material'' and each of them has other subcategories e.g.  ''Black'', ''Red'', ''Blue'' for ''Color''. At the end of the branches are article pages like ''Pen'' for instance. But since one article can be in more than one category there are many overlapping or crossing trees, i.e. there are several ways to reach a certain article from the "top" of the category tree.

==Usage==

* To categorize an article ''Black plastic pen'' into ''Made of plastic'' simply put '''<nowiki>[[Category:Made of plastic]]</nowiki>''' at the bottom of the article page. The same goes for Subcategorization: To make ''Made of Plastic'' a subcategory of ''Material'' put '''<nowiki>[[Category:Material]]</nowiki>''' at the bottom of the page. You see, it's exactly the same syntax.

* For the example given above the category ''Material'' would contain one subcategory ''Made of Plastic'' which will be shown in the ''Material'' category page in alphabetical order, i.e. "M" in this case. If you have other subcategories like ''Made of wood'', ''Made of paper'', ''Made of steel'' and so on, they all would be sorted under "M", which is inconvenient. Therefore the '''sort key''' feature exists, which allows you to overwrite the default alphabetical sorting (by article name) by providing a sort key which is used for the sorting instead. It is used like a piped link, e.g. '''<nowiki>[[Category:Material|Plastic]]</nowiki>''' puts the article ''Made of plastic'' under "P" in the list shown on the category page ''Material''.

* If you want to put a link to the category page somewhere use '''<nowiki>[[:Category:category name]]</nowiki>''' (note the colon at the beginning) to avoid the wiki software recognizing it as a categorization tag.

* As you see, it's not necessary to create a category explicitly. It will be created automatically if at least one article or category has the respective category tag. On the other hand you can create a category by creating a page in the category namespace (which is denoted by the prefix ''Category:''). That's why there are three '''kinds of categories''':

# Those with at least one member (article or subcategory), but without an own page. If you go to such a page there will be a message that the page does not exist, nevertheless the list of subcategories and articles belonging to this category will be shown. This happens if you create a category by adding the appropriate tag at the bottom of an article or category page, ''without'' creating a category page.
# Categories without any members but an existing category page. These categories can be created in the category namespace in the same way as articles. E.g. if you want to instantiate a category ''Material'' simply create a page named '''Category:Material'' with some content.
# Categories with both members and an existing category page.

* There are several ways to '''access a category''' depending on its type (for the types see above):

# If you go to '''[[Special:Categories]]''' every category with at least one member (which means that there is a respective category tag on at least one page) will be listed. Some of them can lack an own page and will be shown <FONT COLOR="red">red</FONT>. Click on the link to create a category page.
# If you go to '''[[Special:Allpages]]''' and then choose the category namespace (or follow [https://wiki.mpi-cbg.de/wiki/imagepro/index.php?title=Special%3AAllpages&from=&namespace=14 this link] as a shortcut) you see categories with an existing category page, which means that a category page must already be created (in fact not the categories are shown here but pages). This means you won't see a category (regardless of the number of its members) there, if no category page was created.
# '''[[:Category:Fundamental]]''' is supposed to be the topmost category from which you can start exploration.

==Guidelines==

* Before starting to use categories '''make yourself familiar''' with the concept of categorization, for example by exploring the [[wikipedia:Wikipedia:Categorization#See_also|categories of Wikipedia]].
* Every article should belong to at least one category and every category should be reachable from [[:Category:Fundamental]]. If you write a new article '''try to categorize''' it within the existing categories (for how to find categories see above). If there is no appropriate category or you're not sure, use the talk page of the newly created article.
* Follow the usual '''naming conventions'''. In this wiki we try to establish [[wikipedia:Wikipedia:Categorization#Category_naming|Wikipedia's ones]].
* Categorization of an article of category can '''simply be revoked''' by deleting or changing the respective category tag on the article or category page before you change anything.
* Deleting or moving a category is '''not as easy''' as for normal articles, though. Therefore care has to be taken upon creation of categories and '''should not''' be done randomly.
* If you're unsure what category you should use, make a comment on the article's '''talk page'''. For creation or changes of categories start a discussion on the appropriate talk pages.

[[Category:Help|{{PAGENAME}}]]
