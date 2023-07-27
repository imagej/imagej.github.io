---
title: Editing the Wiki
section: Contribute:Editing the Wiki
nav-links: true
nav-title: Introduction
---

This page explains how to write and edit wiki pages. The simplest way to create
or modify a page is using GitHub's online file editor. Each page has an "Edit
page" link at the top right with a direct link to this interface.

{% include notice icon="tech" content="Advanced users can make edits via a local clone of the site repository; see the [advanced editing guide](/editing/advanced) for setup instructions." %}

# Requirements

As this wiki is completely hosted on GitHub, you will need to be logged into a GitHub account to make edits (this replaces the old system of registering for an ImageJ-wiki-specific account). If you don't have an account yet, you can [create one freely](https://github.com/signup).

For the smoothest editing experience you will want [collaborator access](https://github.com/imagej/imagej.github.io/settings/access). To be added as a collaborator, just [get in touch](/discuss#ways-to-get-help) and let us know your GitHub account name and we'll be happy to add you.

Non-collaborators have to [fork this repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo), edit that fork as described below, and then [create a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork).

# Creating a new page

Let's dive in to how to create a new page on the site.
If you are looking to edit an existing page, skip to
[adding and editing page content](#adding-editing-page-content) below. See also the general GitHub [guide to editing files](https://docs.github.com/en/repositories/working-with-files/managing-files/editing-files).

1.  Navigate to an appropriate sub-directory of the
    [pages section](https://github.com/imagej/imagej.github.io/tree/main/_pages)
    of the repository. For example, if you are creating a page about a plugin, you would go to [_pages/plugins/](https://github.com/imagej/imagej.github.io/tree/main/_pages).
    **Note:** if you need to create a new sub-directory, it can be specified in the file name below.

2.  Click {% include button label="Add file" %} then
    {% include button label="Create new file" %} from the drop-down:

    {% include img align="center" src="editing/create-page-etw" %}

3.  Add a name for your file. **Note: this is not the page title;** the page
    title will be applied in the next section, front matter. File names should
    be:
    * all lower case
    * use the file extension `.md`
    * optionally prefixed with new sub-directory name(s), separated with `/`
    * avoid symbols and spaces, and separate words using dashes (`-`):

    {% include img align="center" src="editing/name-your-file" style="border: 1px solid #aaa" %}

## Front matter

Every page begins with a block of *front matter*: a sequence of parameters that
configure your page. Without the front matter, your page will not render
correctly. The following table lists front matter fields you can use:

|       **Field** | **Purpose** |
|----------------:|:------------|
|       **title** | The title of your page. (**Required**) |
| **description** | A short description of your page. Also used for the site's search engine. When omitted, the first sentence of the page content is used. |
|     **section** | Main menu section that should be open when this page first loads, if any. Nested sections to expand should be separated by colons (`:`). For example, this page's section is `Contribute:Editing the Wiki`. |
|  **categories** | For pages describing extensions (e.g. a plugin, script, or update site) of ImageJ: a comma-separated list of categories, enclosed in square brackets (`[` and `]`). Pages with categories appear in the [List of extensions](/list-of-extensions). For example, `[Segmentation, Registration]` would put your page in the Segmentation and Registration categories. |
| **statbox\*** | A collection of individual fields that are used to populate the "Vital statistics" sidebar; see [this comment](https://github.com/imagej/imagej.github.io/blob/main/_includes/layout/statbox#L30-L85) for a list. Including at least one of these fields will cause the statbox to appear; otherwise, there will be no statbox for the page.<br> (***\***note there is no field called "statbox"*) |
|        **icon** | A link (internal or external) to an icon that will be used for the page across the wiki, e.g. in the [list of extensions](/list-of-extensions) or search bar results. |
|     **project** | Used to identify project affiliation. See the list of {% include github org='imagej' repo='imagej.github.io' branch='master' path='_config.yml#L15-L33' label='available projects' %} |
|   **nav-links** | Adds a top navigation bar for related pages. See the [Navigation](/editing/navigation#nav-links) guide for examples. |

Below is a minimal example front matter block. You can copy and paste this code into the editor of a new page (see above).

Replace `My Awesome Page` with the title for the new page.

```
---
title: My Awesome Page
---
```

# Adding +&nbsp;editing page content

This section covers how to populate the *content* of your page.

## Markdown

{% include wikipedia title="Markdown" %} is plain-text syntax formatting,
allowing you to easily and cleanly modify text with italics, bold, ordered
or bulleted lists, etc. This wiki, as a Jekyll site, uses
[kramdown](https://kramdown.gettalong.org/syntax.html). A quick-reference can be found [here](https://kramdown.gettalong.org/quickref.html), and a general Jekyll support reference [here](https://www.markdownguide.org/tools/jekyll/). Also helpful is GitHub Flavored Markdown (GFM) guide found [here](https://guides.github.com/features/mastering-markdown/).

Here are some common kinds of text formatting:

| Formatting                               | Markup                                     |
|------------------------------------------|--------------------------------------------|
| *italic text*                            | `*italic text*`                            |
| **bold text**                            | `**bold text**`                            |
| ***bold and italic text***               | `***bold and italic text***`               |
| `fixed width text/code`                  | <code>`fixed width text/code`</code>       |
| ~~struck-out text~~                      | `~~struck-out text~~`                      |
| [Hyperlink](https://example.com/)        | `[Hyperlink](https://example.com/)`        |
| <span style="color: red">red text</span> | `<span style="color: red">red text</span>` |

Note that the last example, colored text, is not really Markdown, but rather
plain {% include wikipedia title="HTML" %}. However, Markdown does not have a
syntax for changing text color, and it supports mixing in HTML, so you can use
the technique above if you need text in different colors.

Here are some common image uses:

| Image                                    | Markup                                     |
|------------------------------------------|--------------------------------------------|
| ![Alt text](/media/icons/fiji.svg) | `![Alt text](/media/icons/fiji.svg)` |
| ![External image](https://fiji.sc/site/logo.png){:width="64px"} | `![External image](https://fiji.sc/site/logo.png){:width="64px"}` |

Note that the last example includes inline styling, which is kramdown-specific.

Certain kinds of structures have dedicated pages of this guide:

* [Images](images) (using [Liquid](#liquid), not Markdown,
  for more complex image needs such as galleries, figures, etc...)
* [Tables](tables)
* [Math expressions](math)
* [Source code and syntax highlighting](code)
* [Footnotes](citations#footnotes)

## Liquid

On top of Markdown, the site uses a templating language called
[Liquid](https://jekyllrb.com/docs/liquid/) to make page editing
more convenient than with Markdown alone. Liquid tags look
like {% raw %}`{% ... %}` or `{{ ... }}`{% endraw %}. Many pages
on this site use Liquid to invoke functions called *includes*,
which enable insertion of images, figures, notices, and more.
(Think of this as: "I would like to *include* an image".)
Here are a couple of examples:

<style>
.skinny {
  margin-left: 0;
  max-width: 30em;
}
.skinny td:first-child {
  width: 8em;
}
</style>

| Markup | Result |
|--------|--------|
| `{% raw %}{% include icon name="imagej" %}{% endraw %}`  | {% include icon name="imagej" %} |
| `{% raw %}{% include person id="rasband" %}{% endraw %}` | {% include person id="rasband" %} |
{:style="margin-left: 0; max-width: 30em"}

### Available includes

The following tables list all of this site's general-purpose includes:

#### Citations and footnotes

| Include                                      | Purpose                 |
|----------------------------------------------|-------------------------|
| [citation](citations#citing-publications)    | Insert a citation       |
| [testimonial](citations#testimonials)        | Insert a personal quote |
{:.skinny}

#### Linking

| Include                           | Purpose                              |
|-----------------------------------|--------------------------------------|
| [link-banner](linking#banner)     | Insert a large, obvious link         |
| [github](linking#github)          | Link to a resource on GitHub         |
| [javadoc](linking#javadoc)        | Link to a javadoc resource           |
| [matlab](linking#matlab)          | Link to MATLAB documentation         |
| [maven](linking#maven)            | Link to Maven artifacts              |
| [person](people)                  | Link to a person's user page         |
| [person-list](people#lists)       | Link to a list of user pages         |
| [scholar](linking#scholar)        | Link to an article on Google Scholar |
| [wikipedia](linking#wikipedia)    | Link to a Wikipedia page             |
{:.skinny}

#### Symbols

| Include                           | Purpose                    |
|-----------------------------------|----------------------------|
| [bc](menu-paths)                  | Insert a menu breadcrumb   |
| [button](buttons)                 | Insert a button            |
| [key](keys)                       | Insert a keyboard shortcut |
| [icon](icons)                     | Insert an icon             |
{:.skinny}

#### Media

| Include                            | Purpose                    |
|------------------------------------|----------------------------|
| [img](images#images)               | Insert an image            |
| [gallery](images#image-galleries)  | Insert an image gallery    |
| [video](videos)                    | Embed a video              |
| [spreadsheet](tables#spreadsheets) | Embed a spreadsheet        |
{:.skinny}

#### Notices

| Include                     | Purpose                               |
|-----------------------------|---------------------------------------|
| [notice](notices)           | Insert an informational notice banner |
| [aside](notices#asides)     | Float a right sidebar with commentary |
{:.skinny}

#### Source code

| Include      | Purpose                          |
|--------------|----------------------------------|
| [code](code) | Embed a code snippet from GitHub |
{:.skinny}

#### Miscellaneous

| Include                              | Purpose                              |
|--------------------------------------|--------------------------------------|
| [quiz](quizzes)                      | Insert a Q&A with hidden answer      |
| [timeline](timelines)                | Insert a horizontal timeline         |
| [tooltip](tooltips)                  | Add a tooltip appearing on mouseover |
| [echo](debugging)                    | For debugging                        |
{:.skinny}

#### MARKED FOR REMOVAL

| Include                                      | What needs to happen               |
|----------------------------------------------|------------------------------------|
| thumbnail                                    | Merge with img include             |
| [info-box](notices#info-box)                 | Delete after migrating to statbox  |
| clear                                        | Delete after purging all floats    |
{:.skinny}

# Finalizing your edits

Once you're happy with your new page, click on the "Commit changes" button to save your work:

 {% include img align="center" src="editing/committing-changes" style="border: 1px solid #aaa" %}

This will bring up a dialog where you can set the summary commit message, a more in-depth description
of the changes, and verify the account used to make the changes.

 {% include img align="center" src="editing/commit-dialog" style="border: 1px solid #aaa" %}

For most edits it makes sense to simply commit to the `main` branch directly. Just adding pages won't break
anything. But if you are concerned you can always use the "branch and pull request" option. Just make sure to
assign or mention someone in the PR (pull request)! Otherwise we may not see it to merge it in a timely manner.
Good options for reviewer are {% include person id="hinerm" %} and {% include person id="ctrueden" %}.

If you aren't sure what to write in your commit message, there are many guides out on the internet. You can even
ask ChatGPT! Just don't do this:

  {% include img align="center" src="https://imgs.xkcd.com/comics/git_commit.png" style="border: 1px solid #aaa" %}

Once you are sufficiently happy with your message and click the "Commit changes" button, your edits will go onto the
history of the site. This will trigger [a rebuild of the site](https://github.com/imagej/imagej.github.io/actions). Once
that completes, your changes will show up on the live site! Thank you for your contribution!

# Adding non-page files

If you need to add other types of files, you can use the "Upload files" option in the "Add files" button:

  {% include img align="center" src="editing/uploading-files" style="border: 1px solid #aaa" %}

This will bring you to a drag-and-drop interface that allows you to create a new commit directly after you've uploaded your desired files.

If you want more control over the structure of the files you're adding, it may be easier to go the [Advanced Editing](/editing/advanced) route.
This also allows you to preview your changes before committing them.

# FAQ

## Why do I need to fork this repository to edit it?

If you go to edit a page and see this message, it means you are not listed as a [collaborator](https://github.com/imagej/imagej.github.io/settings/access)
in this repository.

  {% include img align="center" src="editing/forking" style="border: 1px solid #aaa" %}

To be added as a collaborator, just [get in touch](/discuss#ways-to-get-help) and let us know your GitHub account name; we'll be happy to add you!
