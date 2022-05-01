---
title: Advanced Editing
section: Contribute:Editing the Wiki
nav-links: true
---

This page describes how to install [Jekyll](https://jekyllrb.com/),
and work with the wiki locally as a [Git](/develop/git) repository.

## Install jekyll

The jekyll static site generator can be installed on Linux, MacOS and Windows.
To install a local version of jekyll follow the instructions for your
respective operating system [here](https://jekyllrb.com/docs/installation/).

## Clone the repository

Once jekyll has been installed,
[clone](https://docs.github.com/en/enterprise/2.13/user/articles/cloning-a-repository)
the repository. Navigate to the cloned repository and run `bundle install` to
install the specific ruby gems necessary to run jekyll and serve the site.
Once installation is complete, it is a good idea to run `bundle update`
(it is a good idea to `bundle update` every so often to stay up to date).

## Serve a local version of the site

Now that the both jekyll and the repository are installed on your local
machine, you can run the static site generator by navigating to your local site
directory within a terminal and running `bundle exec jekyll serve`. Wait for a
minute while the site generates, and then in your browser navigate to the
server address that has been output in your terminal, i.e.
[http://127.0.0.1:4000](http://127.0.0.1:4000). Changes you make to any file in
the directory will be detected by jekyll, regenerating the site to reflect the
new changes.

Alternatively, you can run `bundle exec jekyll serve --incremental` to initiate
the local server. This command will reduce the amount of time it takes for the
site to regenerate if you anticipate making many changes in quick succession.

## Create a new page in `_pages`

In the desired folder beneath `_pages`, create a new text
file&mdash;e.g. `touch _pages/plugins/my-awesome-plugin.md`.

{% include notice icon="info" content="Filenames should be lowercase, omit spaces, and use extension `.md`." %}

## Editing a page locally

We recommend using a
[text editor](https://hackernoon.com/5-best-text-editors-for-programmers-3f54ef51d5ae)
to add content and make changes to a page when working locally. A text editor
makes navigating between files, searching for text within your page, and making
multiple edits more efficient and provides a more user-friendly interface.

From here, the [front matter](/editing#add-the-pages-front-matter) and
content of the new page can be populated with a text editor of your choosing.

* Images and other media should be stored in `/path/to/imagej.github.io/media`.

* Regularly save your progress with commits. The process of commiting your
  changes pushes your edits to the main branch of the repository hosted on
  `GitHub`. The process of commiting is described below.


## Create an extension
If you want to extend the features of the wiki, for example, load a custom javascript library to certain pages.
You can add your scripts into `_includes/extensions`, and then the user can enable your extension by adding the extension name to `extensions` in the [Front Matter](https://jekyllrb.com/docs/front-matter/) of their markdown file.

For example, you can find two example extensions `mathjax` and `imjoy` in the `_includes/extensions` folder.
And in the begining of any page, you can enable them by:
```yaml
---
title: My Awesome Page
extensions: ["imjoy", "mathjax"]
---
```

## Pushing, pulling, and commiting with Git

Once you are ready to publish your your new page you will need to add, commit,
and push your changes to the repository. These steps should looks something
like:

1. `git add path/to/your-page-name.md` This step stages your changes to be commited.
2. `git commit path/to/your-page-name.md` Note: you will not be prompted to enter a commit message. Our usership uses imperative tense, i.e. "Add new page xzy"
3. `git push` Your new page or edits will not be pushed to the main branch of the repository.

[This guide](https://rogerdudler.github.io/git-guide/) provides further
explanations on the above steps, as well as how to keep your local repository
up-to-date with the remote with `git pull`.
