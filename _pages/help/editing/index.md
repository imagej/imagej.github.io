---
title: Editing the Wiki
section: Help
categories: tutorials
description: This page explains how to write and edit pages.
---

# Getting started

Creating or editing a page on GitHub pages is super easy! Pages can be created or modified online via GitHub's online file editor (clicking "Edit page" on the top right of this page will bring you to this specific page's source) or, for advanced users, via a local installation of jekyll and the imagej.github.io site. (See our advanced user guide for jekyll set-up instructions)

If you do not need to create a new page and would like to make changes to an existing page, skip to [adding and editing page content](Editing_the_Wiki#adding-and-editing-page-content).

## Creating a new page
<br>

{% include image-right name="create-page" image-path="/images/readme/create-page-etw.png" %}

<br>

1. Navigate to the [_pages section](https://github.com/imagej/imagej.github.io/tree/master/_pages) of the `imagej.github.io` repository.
Click `Add file` then  `Create new file` from the drop-down.

2. Add a name for your file. **Note: this is not the page title;** the page title will be applied in the next section, front matter. File names should be lowercase, avoid symbols, and contain no spaces (use underscores or dashes instead, `_` `-`).

{% include image-right name="name-your-file" image-path="/images/readme/name-your-file.png" classes="grey-border" %}

## Add the page's *front matter*
The *front matter* precedes the content of your page, and sets several parameters that help setup your page within the repository. Without the front matter, your page will not render correctly.

**title:** The title of your page.\
**description:** A short description of your page. Also used for the site's search engine.

Find below the front matter for this page. You can copy and paste this code into the editor of a new page from lines 1-6. Replace the settings in the `title` and `description` fields with details from the new page.

```
---
title: Editing the Wiki
description: This page explains how to write and edit pages.
---
```

## Adding and editing page *content*
Pages on `imagej.github.io` are optimized to be written in git markdown, but will also read `html` syntax. This section will cover how to populate the *content* of your page, including: links to GitHub markdown resources, as well as guides on how to use this site's includes.

#### Markdown
Markdown is plain-text syntax formatting, allowing a user to easily and cleanly modify text with italics, bold, ordered or bulleted lists, etc. As a GitHub pages hosted website, imagej.github.io uses the `git` flavor of markdown. [A basic Git markdown guide can be found here.](https://guides.github.com/features/mastering-markdown/)

#### Using includes
Includes provide more robust formatting options and are unique to this site (think of this as: "I would like to *include* an image," etc). With includes, you can insert menus, images, tables, sideboxes, figures, math, warnings, etc with pre-formatted settings into a page. For a full list of includes with utilization instructions, [see below](Editing_the_Wiki#available-includes).

#### Available "includes"

| Action | Link to demo page|
| : --- : | :---: |
| Insert the about menu | [about-menu](about-menu)
| Insert a citation | [citation](citation)
| Insert conference info | [conference](conference)
| Info/details boxes | [alt-boxes](additional-info-boxes) |
| Insert figure | [figure](figure) |
| Insert a gallery | [gallery](gallery) |
| Link to github files | [github](github) |
| Insert Git menu | [git-menu](git-menu) |
| Insert images | [image](image) |
| Insert a notice | [info-box](info-box)
| Insert logos | [logo](logo) |
| Insert menu breadcrumb | [menu-bc](menu-breadcrumb) |
| Insert math | [math](math) |
| Insert person details | [person](person)
| Insert a sidebox | [sidebox](sidebox)
| Insert the SNT nav bar | [SNT-nav](SNT-nav)|
| Insert a symbol | [symbol](/help/editing/symbols)
| Insert a table | [markdown-table](markdown-table)
| Insert a todo list | [todo-list](todo-list)
| Insert a tech box | [tech-box](tech-box)
| Insert a warning | [warning-box](warning-box) |
| Insert a YouTube video | [youtube-video](youtube-video) |


# Syntax highlighting

Java example:

```java
Image3DUniverse univ = new Image3DUniverse();
univ.show();
univ.addMesh(yourImagePlus, null, "somename", 50, new boolean[] {true, true, true}, 2);
...
```

Python example:

```python
def update_progress(progress):
    barLength = 10 # Modify this to change the length of the progress bar
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if not isinstance(progress, float):
        progress = 0
        status = "error: progress var must be float\r\n"
    if progress < 0:
        progress = 0
        status = "Halt...\r\n"
    if progress >= 1:
        progress = 1
        status = "Done...\r\n"
    block = int(round(barLength*progress))
    text = "\rPercent complete: [{0}] {1}% {2}".format( "#"*block + "-"*(barLength-block), progress*100, status)
    sys.stdout.write(text)
    sys.stdout.flush()
```
# Advanced editing with jekyll

## Install jekyll
The jekyll static site generator can be installed on Linux, MacOS and Windows. To install a local version of jekyll follow the instructions for your respective operating system [here](https://jekyllrb.com/docs/installation/).

## Clone the `imagej.github.io` repository
Once jekyll has been installed, [clone](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository) the the imagej.github.io repository. Navigate to the cloned repository and run `bundle install` to install the specific ruby gems necessary to run jekyll and serve the site . Once installation is complete, it is a good idea to run `bundle update` (it is a good idea to `bundle update` every so often to stay up to date).

## Serve a local version of imagej.github.io
Now that the both jekyll and the repository are installed on your local machine, you can run the static site generator by navigating to your local imagej.github.io directory within a terminal and running `bundle exec jekyll serve`. Wait for a minute or two while the site generates, and then in your browser navigate to the server address that as been output in your terminal, ie `http://127.0.0.1:4000`. Changes you make to any file in the directory will be detected by jekyll, regenerating the site to reflect the new changes.

Alternatively, you can run `bundle exec jekyll serve --incremental` to initiate the local server. This command will reduce the amount of time it takes for the site to regenerate if you anticipate making many changes in quick succession.

## Create a new page in `_pages`

In `/path/to/imagej.github.io/_pages`, create a new text file i.e. `cat > your_page_name.md`.

<br>

NOTE: filenames should be lowercase, omit spaces, and use extension `.md`.

## Editing a page locally

We recommend using a [text editor](https://hackernoon.com/5-best-text-editors-for-programmers-3f54ef51d5ae) to add content and make changes to a page when working locally. A text editor makes navigating between files, searching for text within your page, and making multiple edits more efficient and provides a more user-friendly interface.

From here, the [front matter](Editing_the_Wiki#add-the-pages-front-matter) and content of the new page can be populated with a text editor of your choosing.

* Images and other media should be stored in `/path/to/imagej.github.io/media`.

* Regularly save your progress with commits. The process of commiting your changes pushes your edits to the master branch of the repository hosted on `GitHub`. The process of commiting is described below.

## Pushing, pulling, and commiting with Git

Once you are ready to publish your your new page you will need to add, commit, and push your changes to the repository. These steps should looks something like:

1. `git add path/to/your-page-name.md` This step stages your changes to be commited
2. `git commit path/to/your-page-name.md` Note: you will not be prompted to enter a commit message. Our usership uses imperative tense, i.e. "Add new page xzy"
3. `git push` Your new page or edits will not be pushed to the master branch of the repository.

[This guide](https://rogerdudler.github.io/git-guide/) provides further explanations on the above steps, as well as how to keep your local repository up-to-date with the master with `git pull`.
