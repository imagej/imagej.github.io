---
title: Curtis Rueden
name: Curtis Rueden
website: https://restlesscoder.net/
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

Curtis Rueden directs the
[software development efforts](https://loci.wisc.edu/software/home)
of [LOCI](/orgs/loci).
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

* **Community Mondays.** In the meantime, starting in 2022, I am personally
  focusing every Monday on answering support questions. I can't keep up with
  everything, but I can try to make some small impact by responding to as many
  requests as I can. Unfortunately, until the status.scijava.org work is
  complete, I won't always succeed in prioritizing items in a fair order, but
  I'm doing my best. And once the component table is upgraded, I will switch
  to a daily rather than weekly support workflow.

## What is Curtis working on?

### Immediate priorities

*Last updated: 2022-Feb-01*

1.  Fix `net.imagej:ij` deployment ({% include github org='imagej' repo='ImageJ' issue=142 %})

2.  Discern and document the best way to retire obsolete ImageJ update sites (see {% include github org='imagej' repo='list-of-update-sites' pr=103 %})

3.  Finish revamping status.scijava.org ({% include github org='scijava' repo='status.scijava.org' branch='github-issues' %})

4.  Finish fixing javadoc.scijava.org ({% include github org='scijava' repo='pom-scijava' issue=130 %})

5.  Fix failing CI builds
    * `imagej/pyimagej`
    * `scijava/jgo`
    * `imagej/tutorials`
    * `axtimwalde/mpicbg`
    * `imagej/imagej-omero`
    * `imagej/imagej-opencv`
    * `fiji/H5J_Loader_Plugin`
    * `fiji/Kappa`
    * Update CI-related docs on imagej.net

6.  Migrate fiji-builds to WebDAV (with [hinerm](/people/hinerm))

7.  Update all community projects to not use log4j ({% include github org='scijava' repo='pom-scijava' issue=179 %})

8.  Update all community projects to 19.04 JHDF5 ({% include github org='scijava' repo='pom-scijava' issue=181 %})

9.  Get [labkit](/plugins/labkit) into Fiji ({% include github org='scijava' repo='pom-scijava' pr=183 %})

10. Catch up on component release backlog (see [status.scijava.org](https://status.scijava.org) table)

11. Finish reconciling ImageJ-OMERO and ImageJ Server with PSJ 30+ ({% include github org='scijava' repo='pom-scijava' issue=133 %}, {% include github org='scijava' repo='pom-scijava' issue=173 %}, {% include github org='scijava' repo='pom-scijava' issue=122 %})
    * **ImageJ-OMERO** update to OMERO 5.5+. ({% include github org='imagej' repo='imagej-omero' pr=107 %})
    * **ImageJ Server** fix ({% include github org='imagej' repo='imagej-server' issue=41 %})

12. Finish the mega-melt ({% include github org='scijava' repo='pom-scijava' issue=146 %})

13. Finish reviewing {% include github org='scijava' repo='scijava' issue=75 label='scijava-ops PRs' %}

14. Finish the imagej.net statbox feature ([related issues](https://github.com/imagej/imagej.github.io/issues?q=is%3Aissue+is%3Aopen+statbox))

15. Fix ImageJ 1.x patching ({% include github org='imagej' repo='ij1-patcher' issue=50 %}, {% include github org='imagej' repo='ImageJ' issue=149 %})

### Short-term priorities

1.  \[Winter 2021\] (with {% include person id='elevans' %} and {% include person id='hinerm' %}) *PyImageJ paper.* ([roadmap](https://github.com/imagej/pyimagej/projects/1))
2.  \[Winter 2021\] (with {% include person id='gselzer' %} and {% include person id='hinerm' %}) **SciJava Ops** + **ImageJ Ops2** ([roadmap](https://github.com/orgs/scijava/projects/1)), including [JPMS/Jigsaw](https://openjdk.java.net/projects/jigsaw/) modularization and migration of SciJava foundational libraries to Java 11.
3.  \[Spring 2022\] **Maven-based ImageJ Launcher.** And migrate ImageJ and Fiji to ship with Java 11. Use a Java-6-compatible stub classpath that checks your Java version and tells you how to upgrade to Java 11 if needed. Retire the Java-8 update site, using Maven coordinates instead.

### Medium-term priorities

1.  **GitHub issue reporting plugin.** The Fiji BugZilla and ImageJ Trac are now static content only. The [Report a Bug](/discuss/bugs) plugin needs to send reports to GitHub instead. ([scijava/scijava-plugins-issues-github](https://github.com/scijava/scijava-plugins-issues-github))
2.  **Integrate PyImageJ with the ImageJ launcher.** (see also [this forum discussion](https://forum.image.sc/t/fiji-conda/59618/13))

### Longer-term priorities

1.  **Rich Image.** Improve the [ImageJ Common](/libs/imagej-common) data model to support metadata (e.g., spatial transformations) as a first-class citizen. ([imagej/imagej-common@rich](https://github.com/imagej/imagej-common/compare/rich), [imagej/janelia-hackathon-2016](https://github.com/imagej/janelia-hackathon-2016))
2.  **SCIFIO blockization.** ({% include github org='scifio' repo='scifio' issue=283 %})
3.  **ImageJ Launcher.** Switch to a JavaFX-based native launcher. Retire the current ImageJ Launcher.
    ({% include github org='imagej' repo='imagej-launcher' issue=33 %})
4.  **ImageJ Electron app.** Shared memory between Java, JavaScript and Python. ([imagej/imagej-electron-app](https://github.com/imagej/imagej-electron-app))

### Constant priorities

I also have the following continuous priorities:

1.  Project management tasks (e.g., managing [issues](/develop/project-management#issue-tracking))
2.  Coordinating efforts and mentoring programmers at [LOCI](/orgs/loci)
3.  Server maintenance and troubleshooting
4.  User support: questions on the [Image.sc Forum](/discuss), [bug reports](/discuss/bugs), [pull requests](https://github.com/search?q=is%3Apr+is%3Aopen+user%3Afiji+user%3Aimagej+user%3Amaven-nar+user%3Ascifio+user%3Ascijava+user%3Aslim-curve&type=Issues), email

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
