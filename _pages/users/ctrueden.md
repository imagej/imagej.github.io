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

## What is Curtis working on?

### Immediate priorities

*Last updated: 2021-May-03*

1.  \[Spring 2021\] (with {% include person id='hinerm' %} and {% include person id='elevans' %}) **New ImageJ website.** ([roadmap](https://github.com/imagej/imagej.github.io/projects/2))
2.  \[Summer 2021\] **ImageJ-OMERO** update to OMERO 5.5+. ([imagej/imagej-omero#107](https://github.com/imagej/imagej-omero/pull/107))
3.  **Fix ImageJ1 patching.** Reconcile latest ImageJ 1.x versions with ImageJ2 patching logic ([imagej/ij1-patcher#47](https://github.com/imagej/ij1-patcher/pull/47))
4.  \[Summer 2021\] (with {% include person id='elevans' %} and {% include person id='hinerm' %}) *PyImageJ paper.* ([roadmap](https://github.com/imagej/pyimagej/projects/1))
5.  \[Fall 2021\] (with {% include person id='gselzer' %} and {% include person id='hinerm' %}) **SciJava Ops** + **ImageJ Ops2** ([roadmap](https://github.com/orgs/scijava/projects/1)), including [JPMS/Jigsaw](https://openjdk.java.net/projects/jigsaw/) modularization and migration of SciJava foundational libraries to Java 11.
6.  \[Winter 2021\] **Maven-based ImageJ Launcher.** And migrate ImageJ and Fiji to ship with Java 11. Use a Java-6-compatible stub classpath that checks your Java version and tells you how to upgrade to Java 11 if needed. Retire the Java-8 update site, using Maven coordinates instead.

### Medium-term priorities

1.  **GitHub issue reporting plugin.** The Fiji BugZilla and ImageJ Trac are now static content only. The [Report a Bug](/help/bugs) plugin needs to send reports to GitHub instead. ([scijava/scijava-plugins-issues-github](https://github.com/scijava/scijava-plugins-issues-github))
2.  **Integrate PyImageJ with the ImageJ launcher.**

### Longer-term priorities

1. **Rich Image.** Improve the [ImageJ Common](/libs/imagej-common) data model to support metadata (e.g., spatial transformations) as a first-class citizen. ([imagej/imagej-common@rich](https://github.com/imagej/imagej-common/compare/rich), [imagej/janelia-hackathon-2016](https://github.com/imagej/janelia-hackathon-2016))
2. **SCIFIO blockization.** ([scifio/scifio#283](https://github.com/scifio/scifio/issues/283))
3. **ImageJ Launcher.** Switch to a JavaFX-based native launcher. Retire the current ImageJ Launcher. ([imagej/imagej-launcher#33](https://github.com/imagej/imagej-launcher/issues/33))
4. **ImageJ Electron app.** Shared memory between Java, JavaScript and Python. ([imagej/imagej-electron-app](https://github.com/imagej/imagej-electron-app))

### Constant priorities

I also have the following continuous priorities:

1.  Project management tasks (e.g., managing [issues](/develop/project-management#issue-tracking))
2.  Coordinating efforts and mentoring programmers at [LOCI](/orgs/loci)
3.  Server maintenance and troubleshooting
4.  User support: questions on the [Image.sc Forum](/help), [bug reports](/help/bugs), [pull requests](https://github.com/search?q=is%3Apr+is%3Aopen+user%3Afiji+user%3Aimagej+user%3Amaven-nar+user%3Ascifio+user%3Ascijava+user%3Aslim-curve&type=Issues), email

## Recommended development tools

So you want to be an effective software developer? Use tools!

{::nomarkdown}
<table>
  <thead>
    <tr class="header">
      <th>
        <p>Tool</p>
      </th>
      <th>
        <p>Purpose</p>
      </th>
      <th>
        <p>Plugins</p>
      </th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <p><a href="/develop/eclipse">Eclipse</a></p>
      </td>
      <td>
        <p>Super powerful</p>
        <ul>
          <li><em>Essential</em> for navigation of large projects</li>
          <li>Supreme code completion</li>
          <li>Super useful debugger</li>
        </ul>
      </td>
      <td>
        <p><a href="http://vrapper.sourceforge.net/">Vrapper</a></p>
      </td>
      <td>
        <p>Vim-fu inside Eclipse – almost as good as the real thing</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="https://ecd-plugin.github.io/">Enhanced Class Decompiler</a></p>
      </td>
      <td>
        <p>Automatic decompilation when browsing classes in Eclipse</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://www.vim.org/">Vim</a></p>
      </td>
      <td>
        <p>Great editor. Crazy fast <a href="https://vim.wikia.com/wiki/Macros">macros</a></p>
      </td>
      <td>
        <p><a href="https://github.com/VundleVim/Vundle.vim">Vundle</a></p>
      </td>
      <td>
        <p>Manage your vim plugins like a boss</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/tpope/vim-sensible">vim-sensible</a></p>
      </td>
      <td>
        <p>Defaults everyone can agree on</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/vim-airline/vim-airline">vim-airline</a></p>
      </td>
      <td>
        <p>Lean & mean status/tabline that's light as air</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/tpope/vim-fugitive">vim-fugitive</a></p>
      </td>
      <td>
        <p>A Git wrapper so awesome, it should be illegal</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/tpope/vim-repeat">vim-repeat</a></p>
      </td>
      <td>
        <p>Repeating supported plugin maps with "."</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/tpope/vim-surround">vim-surround</a></p>
      </td>
      <td>
        <p>Quoting/parenthesizing made simple</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/vimrc">my .vimrc</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://www.zsh.org/">Zsh</a></p>
      </td>
      <td>
        <p>Awesome shell – even <a href="https://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692">better than bash</a></p>
      </td>
      <td>
        <p><a href="https://github.com/tarjoilija/zgen">zgen</a></p>
      </td>
      <td>
        <p>Lightweight plugin manager</p>
      </td>
    </tr>
    <tr>
      <td>
        <p><a href="https://ohmyz.sh/">oh-my-zsh</a></p>
      </td>
      <td>
        <p>Your terminal never felt <em>this</em> good before:</p>
        <ul>
          <li><strong>git</strong> - awesome git completion and aliases</li>
          <li><strong>mvn</strong> - mvn completion, highlighting, aliases</li>
          <li><strong>vi-mode</strong> - vi on the CLI</li>
          <li><strong>vundle</strong> - manage your vim plugins</li>
          <li><strong>z</strong> - stop <code>cd</code>ing your life away</li>
          <li>And <em>much</em> more</li>
        </ul>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/zsh-users/zsh-syntax-highlighting">zsh-syntax-highlighting</a></p>
      </td>
      <td>
        <p>Syntax highlights commands as you type them</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/zsh-users/zsh-history-substring-search">zsh-history-substring-search</a></p>
      </td>
      <td>
        <p>Better command history navigation</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="https://github.com/zsh-users/zsh-completions">zsh-completion</a></p>
      </td>
      <td>
        <p>Even more and better tab completions</p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/zshrc">my .zshrc</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/develop/git">Git</a></p>
      </td>
      <td>
        <p>It is worth the pain, I promise</p>
      </td>
      <td>
        <p><a href="https://myrepos.branchable.com/">myrepos</a></p>
      </td>
      <td>
        <p>Commit, push & pull across repositories <a href="https://github.com/ctrueden/dotfiles/blob/master/mrconfig">en masse</a></p>
      </td>
    </tr>
    <tr>
      <td>
        <p>See also <a href="https://github.com/ctrueden/dotfiles/blob/master/gitconfig">my .gitconfig</a></p>
      </td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/develop/github">GitHub</a></p>
      </td>
      <td>
        <p>If you don't have a GitHub account, <a href="https://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/">you don't exist</a></p>
      </td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td>
        <p><a href="/develop/maven">Maven</a></p>
      </td>
      <td>
        <p>Build <a href="https://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants">reusable software components</a></p>
      </td>
      <td></td>
      <td></td>
    </tr>
  </tbody>
</table>
{:/}

See also:

-   The [Dotfiles](/develop/dotfiles) setup guide
-   [Key developer tools](/develop#key-developer-tools) on this wiki
-   [LOCI developer getting started guide](https://loci.wisc.edu/software/developing-loci-software)
