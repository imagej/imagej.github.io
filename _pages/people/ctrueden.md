---
title: Curtis Rueden

name: Curtis Rueden
website: https://ctrue.name/cv
gravatar: 63df759e2779af56fd050a968ff98d09
affiliation:
  - Eliceiri Lab / LOCI | /orgs/loci
  - University of Wisconsin-Madison | https://wisc.edu/
forum: ctrueden
github: ctrueden
stackoverflow: 1207769/ctrueden
openhub: ctrueden
twitter: ctrueden
linkedin: pub/curtis-rueden/15/372/52a
researchgate: Curtis_Rueden
orcid: 0000-0001-7055-6707
arxiv: rueden_c_1
scholar: VqKfxYcAAAAJ
---

Curtis Rueden is a research software engineer at [LOCI](/orgs/loci).
He is the principal architect of [ImageJ2](/software/imagej2),
and the current maintainer of the [Fiji](/software/fiji) distribution of ImageJ.

## Community support pledge

The ImageJ community generates a lot of support activity!
[Forum posts](https://forum.image.sc/tag/imagej), [bug reports](/discuss/bugs),
[chat room](/discuss/chat) messages, and
[mailing list threads](/discuss/mailing-lists), and [more](/discuss).
I want to help, but it's rather overwhelming, especially taken together
with new development efforts and collaborations that are always ongoing.

If you are reading this, perhaps you have posted issues or support requests
that have gone unanswered for weeks, months, or even years. I want to change
that, and am working on process improvements to make it easier for the core
ImageJ2 team to respond to every support request within one work day:

* **Better component status overview.** The site
  [status.scijava.org](https://status.scijava.org/) is a developer-oriented
  view of the status of every component in the SciJava
  [Bill of Materials](/develop/architecture#bill-of-materials), especially
  components built on [pom-scijava](https://github.com/scijava/pom-scijava).
  I am expanding the scope of the component table to include a summary of
  support requests, issues, pull requests, etc., per component, in a way that
  will foster accountability for the people maintaining each component.

* **Community Fridays.** In the meantime, starting in 2022, I am personally
  focusing every Friday on answering support questions. I can't keep up with
  everything, but I can try to make some small impact by responding to as many
  requests as I can. Unfortunately, until the status.scijava.org work is
  complete, I won't always succeed in prioritizing items in a fair order, but
  I'm doing my best.

## What is Curtis working on?

*Last updated: 2022-Apr-18*

### Weekly allocation of effort

|     Day | Focus                                                                                                                                                    |
|--------:|:---------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Mon** | Meetings and mentorship                                                                                                                                  |
| **Tue** | Immediate priorities                                                                                                                                     |
| **Wed** | Review and merge PRs ([my PR queue](https://github.com/users/ctrueden/projects/1/views/2))                                                               |
| **Thu** | Project management                                                                                                                                       |
| **Fri** | Community support ([forum topics](https://forum.image.sc/u/ctrueden/activity/bookmarks), [issues](https://github.com/users/ctrueden/projects/1/views/3)) |

### Immediate priorities

1.  [with {% include person id='hinerm' %}] New pom-scijava release:
    -   Update all community projects to not use log4j ({% include github org='scijava' repo='pom-scijava' issue=179 %})
    -   Update all community projects to 19.04 JHDF5 ({% include github org='scijava' repo='pom-scijava' issue=181 %})
    -   Include the updated ImageJ-OMERO ({% include github org='scijava' repo='pom-scijava' issue=173 %})
    -   Get [labkit](/plugins/labkit) into Fiji ({% include github org='scijava' repo='pom-scijava' pr=183 %})
    -   Finish fixing javadoc.scijava.org ({% include github org='scijava' repo='pom-scijava' issue=130 %})
    -   Catch up on component release backlog (see [status.scijava.org](https://status.scijava.org) table)
    -   Make the mega-melt ({% include github org='scijava' repo='pom-scijava' issue=146 %}) fully work.
    -   Fix failing CI builds:
        * `imagej/pyimagej`
        * `scijava/jgo`
        * `imagej/tutorials`
        * `axtimwalde/mpicbg`
        * `imagej/imagej-omero`
        * `imagej/imagej-opencv`
        * `fiji/H5J_Loader_Plugin`
        * `fiji/Kappa`
        * Update CI-related docs on imagej.net

2.  Fix the {% include github org='fiji' repo='fiji-builds' label='fiji-builds' %} CI workflow.

3.  Finish the imagej.net statbox feature ([related issues](https://github.com/imagej/imagej.github.io/issues?q=is%3Aissue+is%3Aopen+statbox)).

### Project management priorities

1.  Continue populating the project board for SciJava+ImageJ2+Fiji migration to Java 11 and 17 ([roadmap](https://github.com/orgs/imagej/projects/4)).

2.  Finish revamping status.scijava.org ({% include github org='scijava' repo='status.scijava.org' branch='github-issues' label='scijava/status.scijava.org' %}).

### Short-term priorities

- \[Summer 2022\] (with {% include person id='axtimwalde' %}) Migrate ImageJ2 and Fiji to ship with Java 11 or 17 ([roadmap](https://github.com/orgs/imagej/projects/4)), with a **Maven-based ImageJ update site generator** to simplify creation and maintenance of update sites.
- \[Autumn 2022\] (with {% include person id='gselzer' %}) **SciJava Ops** + **ImageJ Ops2** ([roadmap](https://github.com/orgs/scijava/projects/1)), including [JPMS/Jigsaw](https://openjdk.java.net/projects/jigsaw/) modularization and migration of SciJava foundational libraries to Java 11.
- \[Winter 2022\] Make ImageJ Server work again ({% include github org='imagej' repo='imagej-server' issue=41 %}, {% include github org='scijava' repo='pom-scijava' issue=133 %}).

### Medium-term priorities

- **GitHub issue reporting plugin.** The Fiji BugZilla and ImageJ Trac are now static content only. The [Report a Bug](/discuss/bugs) plugin needs to send reports to GitHub instead. ([scijava/scijava-plugins-issues-github](https://github.com/scijava/scijava-plugins-issues-github))
- **Integrate PyImageJ with the ImageJ launcher.** (see also [this forum discussion](https://forum.image.sc/t/fiji-conda/59618/13))

### Longer-term priorities

- **Rich Image.** Improve the [ImageJ Common](/libs/imagej-common) data model to support metadata (e.g., spatial transformations) as a first-class citizen. ([imagej/imagej-common@rich](https://github.com/imagej/imagej-common/compare/rich), [imagej/janelia-hackathon-2016](https://github.com/imagej/janelia-hackathon-2016))
- **SCIFIO blockization.** ({% include github org='scifio' repo='scifio' issue=283 %})
- **ImageJ Launcher.** Switch to a JavaFX-based native launcher. Retire the current ImageJ Launcher.
  ({% include github org='imagej' repo='imagej-launcher' issue=33 %})
- **ImageJ Electron app.** Shared memory between Java, JavaScript and Python. ([imagej/imagej-electron-app](https://github.com/imagej/imagej-electron-app))

## Recommended development tools

So you want to be an effective software developer? Use tools!

{::nomarkdown}
<style>.boxed-table td { border: 1px solid lightgray }</style>
<table class="boxed-table left">
  <thead>
    <tr>
      <th>Tool</th>
      <th>Purpose</th>
      <th colspan=2>Plugins</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan=2><a href="/develop/eclipse">Eclipse</a></td>
      <td rowspan=2>
        Super powerful
        <ul>
          <li><em>Essential</em> for navigation of large projects</li>
          <li>Supreme code completion</li>
          <li>Super useful debugger</li>
        </ul>
      </td>
      <td><a href="http://vrapper.sourceforge.net/">Vrapper</a></td>
      <td>Vim-fu inside Eclipse – almost as good as the real thing</td>
    </tr>
    <tr>
      <td><a href="https://ecd-plugin.github.io/">Enhanced Class Decompiler</a></td>
      <td>Automatic decompilation when browsing classes in Eclipse</td>
    </tr>
    <tr>
      <td rowspan=7><a href="https://www.vim.org/">Vim</a></td>
      <td rowspan=7>Great editor. Crazy fast <a href="https://vim.wikia.com/wiki/Macros">macros</a></td>
      <td><a href="https://github.com/VundleVim/Vundle.vim">Vundle</a></td>
      <td>Manage your vim plugins like a boss</td>
    </tr>
    <tr>
      <td><a href="https://github.com/tpope/vim-sensible">vim-sensible</a></td>
      <td>Defaults everyone can agree on</td>
    </tr>
    <tr>
      <td><a href="https://github.com/vim-airline/vim-airline">vim-airline</a></td>
      <td>Lean & mean status/tabline that's light as air</td>
    </tr>
    <tr>
      <td><a href="https://github.com/tpope/vim-fugitive">vim-fugitive</a></td>
      <td>A Git wrapper so awesome, it should be illegal</td>
    </tr>
    <tr>
      <td><a href="https://github.com/tpope/vim-repeat">vim-repeat</a></td>
      <td>Repeating supported plugin maps with "."</td>
    </tr>
    <tr>
      <td><a href="https://github.com/tpope/vim-surround">vim-surround</a></td>
      <td>Quoting/parenthesizing made simple</td>
    </tr>
    <tr>
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/vimrc">my .vimrc</a></td>
    </tr>
    <tr>
      <td rowspan=6><a href="https://www.zsh.org/">Zsh</a></td>
      <td rowspan=6>Awesome shell – even <a href="https://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692">better than bash</a></td>
      <td><a href="https://github.com/tarjoilija/zgen">zgen</a></td>
      <td>Lightweight plugin manager</td>
    </tr>
    <tr>
      <td><a href="https://ohmyz.sh/">oh-my-zsh</a></td>
      <td>
        Your terminal never felt <em>this</em> good before:
        <ul>
          <li><strong>git</strong> - awesome git completion and aliases</li>
          <li><strong>mvn</strong> - mvn completion, highlighting, aliases</li>
          <li><strong>vi-mode</strong> - vi on the CLI</li>
          <li><strong>vundle</strong> - manage your vim plugins</li>
          <li><strong>z</strong> - stop <code>cd</code>ing your life away</li>
          <li>And <em>much</em> more</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><a href="https://github.com/zsh-users/zsh-syntax-highlighting">zsh-syntax-highlighting</a></td>
      <td>Syntax highlights commands as you type them</td>
    </tr>
    <tr>
      <td><a href="https://github.com/zsh-users/zsh-history-substring-search">zsh-history-substring-search</a></td>
      <td>Better command history navigation</td>
    </tr>
    <tr>
      <td>
        <a href="https://github.com/zsh-users/zsh-completions">zsh-completion</a>
      </td>
      <td>Even more and better tab completions</td>
    </tr>
    <tr>
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/zshrc">my .zshrc</a></td>
    </tr>
    <tr>
      <td rowspan=2><a href="/develop/git">Git</a></td>
      <td rowspan=2>It is worth the pain, I promise</td>
      <td><a href="https://myrepos.branchable.com/">myrepos</a></td>
      <td>Commit, push & pull across repositories <a href="https://github.com/ctrueden/dotfiles/blob/master/mrconfig">en masse</a></td>
    </tr>
    <tr>
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/gitconfig">my .gitconfig</a></td>
    </tr>
    <tr>
      <td><a href="/develop/github">GitHub</a></td>
      <td colspan=3>If you don't have a GitHub account, <a href="https://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/">you don't exist</a></td>
    </tr>
    <tr>
      <td><a href="/develop/maven">Maven</a></td>
      <td colspan=3>Build <a href="https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants">reusable software components</a></td>
    </tr>
  </tbody>
</table>
{:/}

See also:

-   The [Dotfiles](/develop/dotfiles) setup guide
-   [Key developer tools](/develop#key-developer-tools) on this wiki
-   [LOCI developer getting started guide](https://loci.wisc.edu/software/developing-loci-software)
