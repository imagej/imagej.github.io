---
title: Migrating from DokuWiki
nav-links: true
nav-title: DokuWiki Migration
---

The ImageJ Documentation Wiki is no longer available at location &lt;https://imagejdocu.tudor.lu&gt;, as the CRP Henri Tudor has merged to become the Luxembourg Institute of Science and Technology five years ago and the old domain will be discontinued. We want to take this as an opportunity to merge the resources on &lt;https://imagejdocu.list.lu&gt; with those here at &lt;https://imagej.net&gt;.

This guide covers the process of migrating a page from the ImageJ Documentation Wiki ([DokuWiki](https://www.dokuwiki.org/dokuwiki)) to this ImageJ wiki ([GitHub Pages+Jekyll+Markdown+Liquid](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/about-github-pages-and-jekyll)).

1.  **Create a GitHub account** if you do not already have one, by visiting the [signup page](https://github.com/signup).

2.  **Identify the ImageJ Documentation Wiki page you are migrating.** For this walkthrough, we'll choose the [Colocalization Finder](https://imagejdocu.list.lu/plugin/analysis/colocalizationfinder/start) page.

3.  **Grab the path to the page** by selecting it in the address bar and copying it to the clipboard. Here, this is `plugin/analysis/colocalizationfinder/start`.

4.  **Grab the converted Markdown text.** We have done a preliminary conversion of the wiki markup from DokuWiki format to Markdown format, and placed it online for you. Find your converted page at `https://raw.githubusercontent.com/imagej/imagejdocu/master/[your-page].md`, replacing `[your-page]` with the snippet from the previous step. For Colocalization Finder, the URL will be [`https://raw.githubusercontent.com/imagej/imagejdocu/master/plugin/analysis/colocalizationfinder/start.md`](https://raw.githubusercontent.com/imagej/imagejdocu/master/plugin/analysis/colocalizationfinder/start.md). Copy the entire markup code to your clipboard.

5.  **On GitHub, create the destination ImageJ wiki page.** On the ImageJ wiki, page names are lower-web-case with dash separators. As such, for our migrated Colocalization Finder page, we want it to appear at `https://imagej.net/plugins/colocalization-finder`. Therefore:

    * Navigate to [https://github.com/imagej/imagej.github.io/](https://github.com/imagej/imagej.github.io/) in your web browser.
    * Click into the `media` folder, then (scrolling down the page) `plugins`.
    * On the top right side, click the {% include button label="Add file &#9662;" %} button, then "Create new file":
      {% include img src="imagejdocu-create-page" %}
    * For "Name your file...", type `colocalization-finder.md`.

6.  **Paste the converted Markdown code into the "Edit new file" tab's empty text area:**
    {% include img src="imagejdocu-paste-content" %}

7.  **Preview the results.** Click over to the "Preview" tab to see a preview of how the page will look.

8.  **Migrate needed images:**
    1.  Right-click and "Save Image As..." the images from your page on the ImageJ Documentation Wiki. For Colocalization Finder, there are two images: `cf_images.png` and `cf_table.png`.
    2. Rename the images to use dashes instead of underscores, as per the wiki's lower-web-case naming convention. For the Colocalization Finder images, their new names will be `cf-images.png` and `cf-table.png`.
    3.  In a separate browser tab:
        * Go to [https://github.com/imagej/imagej.github.io](https://github.com/imagej/imagej.github.io) again.
        * Click into `media` then `plugins` again.
        * Click the {% include button label="Add file &#9662;" %} button, then "Upload files":
          {% include img src="imagejdocu-upload-images" %}
        * Drag `cf-images.png` and `cf-table.png` onto the "Drag files here" area. Then scroll down to the "Commit changes" box below, type a message like "Add Colocalization Finder images", then click the {% include button label="Commit changes" %} button. This will stage the images for availability from URLs `https://imagej.net/media/plugins/cf-images.png` and `https://imagej.net/media/plugins/cf-table.png` respectively.
    4.  Back in our new Colocalization Finder page, we fix the image link paths; e.g.:
        ```markdown
        ![](/plugin/analysis/colocalizationfinder/cf_images.png)
        ```
        becomes
        ```markdown
        ![](/media/plugins/cf-images.png)
        ```
        See the wiki editing guide's [images](https://imagej.net/editing/images) page for details on formatting your images.
    5.  If you are new to GitHub and not yet approved as an imagej.net editor, you will need to file a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests), which is just a term meaning your changes will be posted as a suggestion (i.e. a "request") for the wiki editors to review, approve, and merge (i.e. "pull in") to the main wiki contents. When you commit your changes as described in step 8.3 above, GitHub will walk you through this procedure. Once your first pull request is merged, you will be granted direct edit access to simplify future edits.

9.  **Add categories to your page** so that it is classified correctly. The Colocalization Finder page is in the `plugins/analysis` subtree, so we will add `category: [Colocalization, Analysis]` to the front matter (i.e. as a key/value pair between the `---` lines at the top). See the [List of Extensions](/list-of-extensions) page, expanding the Categories filter, for a complete list of in-use categories on imagej.net.

10. **Fix any remaining errors and imperfections.** Inspect the rendered page, noting any problems. Then scroll down below the page to find the text box containing the wiki markup code.
    -   For example, the Colocalization Finder auto-converted markup has a spurious `<!-- -->` block surrounded by code fences, which should be deleted.
    -   Test every hyperlink, and update the ones that don't work. Old `http:` links should be converted to `https:` when possible.
    -   You may wish to add a statbox for your plugin:
        - If your plugin is published to maven.scijava.org, you can add an `artifact:` to the front matter, and the statbox will be autopopulated. ([Example](https://imagej.net/plugins/trackmate))
        - If not, but you use Maven to build and have a `pom.xml`, you can link to the raw POM with `pom-url:` in the front matter, and the statbox will be autopopulated. ([Example](https://imagej.net/libs/imagescience))
        - Or if not, you can enter your plugin statistics manually field by field. ([Example](https://imagej.net/plugins/3d-imagej-suite))
        See the [statbox](/editing/statbox) guide for details.
    -   See the [wiki editing guide](/editing) for additional information on wiki syntax.

11. **Preview your page again**, as many times as needed, until everything looks good. Some features, including Liquid {% raw %}`{% ... %}`{% endraw %} tags and front matter values, are not previewable, but will take effect when the page is actually rendered on imagej.net.

12. **Commit your changes when finished.** As we did with the images, scroll down to the "Commit new file" area, type a commit message in imperative tense like "Add Colocalization Finder plugin", and click "Commit new file" to proceed. If you have edit rights, your changes will be merged immediately, and appear on imagej.net within 10 minutes. Or if you are new, you will be walked through filing a pull request for the update.

Please write to the [Image.sc Forum](https://forum.image.sc/) with any questions! We are happy to help.
