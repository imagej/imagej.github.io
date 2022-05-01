---
mediawiki: DokuWiki_Migration
title: Migrating from DokuWiki
section: Help
nav-links: true
nav-title: DokuWiki Migration
---

{% include warning/outdated %}

These instructions will be updated very soon so that ImageJ Documentation Wiki pages can be migrated to the new ImageJ wiki.

**Legacy Text Follows**

The ImageJ Documentation Wiki will no longer be available at location &lt;https://imagejdocu.list.lu&gt;, as the CRP Henri Tudor has merged to become the Luxembourg Institute of Science and Technology five years ago and the old domain will be discontinued. We want to take this as an opportunity to merge the resources on &lt;https://imagejdocu.list.lu&gt; with those here at &lt;https://imagej.net&gt;.

This guide covers the process of migrating a page from the ImageJ Documentation Wiki ([DocuWiki](https://www.dokuwiki.org/dokuwiki)) to this ImageJ wiki ([GitHub Pages with Jekyll](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)).

1.  <b>Create an ImageJ wiki account</b> if you do not already have one, by visiting the [Special:CreateAccount](Special_CreateAccount) page.
2.  <b>Identify the ImageJ Documentation Wiki page you are migrating.</b> For this walkthrough, we'll choose the [Colocalization Finder](https://imagejdocu.list.lu/plugin/analysis/colocalizationfinder/start) page.
3.  <b>Grab the path to the page</b> by selecting it in the address bar and copying it to the clipboard. Here, this is `plugin/analysis/colocalizationfinder/start`.
4.  <b>Grab the converted MediaWiki markup.</b> We have done a preliminary conversion of the wiki markup from DocuWiki format to MediaWiki format, and placed it online for you. Find your converted page at `https://raw.githubusercontent.com/imagej/imagejdocu/master/[your-page].wiki`, replacing `[your-page]` with the snippet from the previous step. For Colocalization Finder, the URL will be [`https://raw.githubusercontent.com/imagej/imagejdocu/master/plugin/analysis/colocalizationfinder/start.wiki`](https://raw.githubusercontent.com/imagej/imagejdocu/master/plugin/analysis/colocalizationfinder/start.wiki). Copy the entire markup code to your clipboard.
5.  <b>Navigate to the destination ImageJ wiki page.</b> On the ImageJ wiki, page names are capitalized with underscores. (Underscores become spaces in the page title.) For our migrated Colocalization Finder page, we'll use [`https://imagej.net/plugins/colocalization-finder`]((http://punias.free.fr/ImageJ/colocalization-finder.html). You should see a message like this:
    <a href=""><img src="/media/discuss/creating-a-new-page.png" width="500px"/></a>
    Click "edit this page" to continue.
6.  <b>Paste the converted wiki markup into the empty text area:</b>  
    <a href=""><img src="/media/discuss/add-wiki-markup.png" width="500px"/></a>
7.  <b>Preview the results.</b> Scroll down below the text field, and click the "Show preview" button (in between "Save page" and "Show changes").
8.  <b>Migrate needed images:</b>
    1.  Right-click and "Save Image As..." the images from your page on the ImageJ Documentation Wiki. For Colocalization Finder, there are two images: `cf_images.png` and `cf_table.png`.
    2.  In a separate browser tab, open the [Special:Upload](Special_Upload) page and upload the images one by one. The Colocalization Finder images will become available from URLs [`https://imagej.net/media/cf-images.png`](/media/cf-images.png) and [`https://imagej.net/media/cf-table.png`](/media/cf-table.png). Notice that MediaWiki always capitalizes the first letter of resources, including image files.
    3.  Back in our new Colocalization Finder page, we now replace the DocuWiki image link syntax with MediaWiki's syntax: e.g. {% raw %}`{{:plugin:analysis:colocalizationfinder:cf_images.png?nolink&400|}}`{% endraw %} becomes `<a href=""><img src="/media/cf-images.png" width="400px"/></a>`. See MediaWiki's [Help:Images](https://www.mediawiki.org/wiki/Help:Images) page for further details on formatting your images.
9.  <b>Add categories to your page</b> so that it is classified correctly. The Colocalization Finder page is in the `plugins/analysis` subtree, so we will add `[[Category:Analysis]]` and `[[Category:Plugins]]`. These tags go at the very bottom of the wiki markup, each one on its own line. See [Special:Categories](Special_Categories) for a complete list of available categories on imagej.net.
10. <b>Fix any remaining errors and imperfections.</b> Inspect the rendered page, noting any problems. Then scroll down below the page to find the text box containing the wiki markup code.
    -   The `<note warning>...</note>` block can become a {% raw %}`{{Warning | ...}}`{% endraw %} block. (See liquid section of [editing](/editing/#adding-and-editing-page-content), and includes: [warn](https://github.com/imagej/imagej.github.io/tree/main/_includes/warning), [notice](https://github.com/imagej/imagej.github.io/blob/main/_includes/notice), [info-box](https://github.com/imagej/imagej.github.io/blob/main/_includes/info-box), and [tooltip](https://github.com/imagej/imagej.github.io/blob/main/_includes/tooltip).)
    -   The red underlined words often highlight misspellings, and can be corrected now, since we have the opportunity.
    -   See the [MediaWiki formatting guide](https://www.mediawiki.org/wiki/Help:Formatting) for additional information on MediaWiki syntax.
11. <b>Click "Show preview" again</b>, as many times as needed, until everything looks good.
12. <b>Save the page when finished.</b> The "Save page" button locks in your new page!
