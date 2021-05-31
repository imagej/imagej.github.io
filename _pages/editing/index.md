---
mediawiki: Help:Contents
title: Editing the Wiki
section: Contribute:Editing the Wiki
nav-links: true
nav-title: Introduction
---

This page explains how to write and edit wiki pages. The simplest way to create
or modify a page is using GitHub's online file editor. Each page has an "Edit
page" link at the top right with a direct link to this interface.

{% include notice icon="tech" content="Advanced users can make edits via a local clone of the site repository; see the [advanced editing guide](/editing/advanced) for setup instructions." %}

# Creating a new page

Let's dive in to how to create a new page on the site.
If you are looking to edit an existing page, skip to
[adding and editing page content](#adding-and-editing-page-content) below.

1.  Navigate to an appropriate sub-directory of the
    [pages section](https://github.com/imagej/imagej.github.io/tree/main/_pages)
    of the repository. For example, if you are creating a page about a plugin, you would go to [_pages/plugins/](https://github.com/imagej/imagej.github.io/tree/main/_pages).

2.  Click {% include button label="Add file" %} then
    {% include button label="Create new file" %} from the drop-down:

    {% include img align="center" src="editing/create-page-etw" %}

3.  Add a name for your file. **Note: this is not the page title;** the page
    title will be applied in the next section, front matter. File names should
    be:
    * all lower case
    * use the file extension `.md`
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
|  **categories** | Comma-separated list of categories to which the page belongs, enclosed in square brackets (`[` and `]`). Pages in the `/plugins/` directory are browsable by category in the [Plugin index](/plugin-index). For example, `[Filtering, Help]` would put your page in the [filtering](/plugin-index#filtering) and [help](/plugin-index#help) sections. |
|       **statbox** | The "Vital statistics" sidebar supports quite a few fields; see [this comment](https://github.com/imagej/imagej.github.io/blob/main/_includes/layout/statbox#L30-L72) for a list. Including at least one of these fields will cause the statbox to appear; otherwise, there will be no statbox for the page. |

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
[Kramdown](https://kramdown.gettalong.org/syntax.html). A quick-reference can be found [here](https://kramdown.gettalong.org/quickref.html), and a general Jekyll support reference [here](https://www.markdownguide.org/tools/jekyll/). Also helpful is GitHub Flavored Markdown (GFM) guide found [here](https://guides.github.com/features/mastering-markdown/).

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

Note that the last example includes inline styling, which is Kramdown-specific.

Certain kinds of structures have dedicated pages of this guide:

* [Tables](tables)
* [Math expressions](math)
* [Source code and syntax highlighting](code)
* [Images](images) ([Liquid](#liquid), not markdown, facilitating complex image needs such as galleries, figures, etc...)

## Liquid

On top of Markdown, the site uses a templating language called
[Liquid](https://jekyllrb.com/docs/liquid/) to make page editing
more convenient than with Markdown alone. Liquid tags look
like {% raw %}`{% ... %}` or `{{ ... }}`{% endraw %}. Many pages
on this site use Liquid to invoke functions called *includes*,
which enable insertion of images, figures, notices, and more.
(Think of this as: "I would like to *include* an image".)
Here are a couple of examples:

<table><tbody>
<tr>
  <th>Markup</th>
  <th>Result</th>
</tr>
<tr>
  <td><code>{% raw %}{% include icon name="imagej" %}{% endraw %}</code></td>
  <td>{% include icon name="imagej" %}</td>
</tr>
<tr>
  <td><code>{% raw %}{% include person id="rasband" %}{% endraw %}</code></td>
  <td>{% include person id="rasband" %}</td>
</tr>
</tbody></table>

### Available includes

The following tables list all of this site's general-purpose includes:

#### Citations and footnotes

| Include                                      | Purpose                 |
|----------------------------------------------|-------------------------|
| [citation](citations#include-citations)      | Insert a citation       |
| [testimonial](citations#include-testimonial) | Insert a personal quote |

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

#### Symbols

| Include                           | Purpose                    |
|-----------------------------------|----------------------------|
| [bc](menu-paths)                  | Insert a menu breadcrumb   |
| [button](buttons)                 | Insert a button            |
| [key](keys)                       | Insert a keyboard shortcut |
| [icon](icons)                     | Insert an icon             |

#### Media

| Include                           | Purpose                    |
|-----------------------------------|----------------------------|
| [img](images#images)              | Insert an image            |
| [gallery](images#image-galleries) | Insert an image gallery    |
| [video](videos)                   | Embed a video              |

#### Notices

| Include           | Purpose                               |
|-------------------|---------------------------------------|
| [notice](notices) | Insert an informational notice banner |
| [aside](TODO)     | Float a right sidebar with commentary |

#### Source code

| Include      | Purpose                          |
|--------------|----------------------------------|
| [code](TODO) | Embed a code snippet from GitHub |

#### Miscellaneous

| Include                              | Purpose                              |
|--------------------------------------|--------------------------------------|
| [quiz](TODO)                         | Insert a Q&A with hidden answer      |
| [timeline](TODO)                     | Insert a horizontal timeline         |
| [tooltip](TODO)                      | Add a tooltip appearing on mouseover |
| [echo](TODO)                         | For debugging                        |

#### MARKED FOR REMOVAL

| Include                                      | What needs to happen               |
|----------------------------------------------|------------------------------------|
| thumbnail                                    | Merge with img include             |
| [info-box](notices#info-box)                 | Delete after migrating to statbox  |
| clear                                        | Delete after purging all floats    |
| project                                      | Delete after improving statbox     |
