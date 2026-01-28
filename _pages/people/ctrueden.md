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

## Community support

The Fiji/ImageJ community generates a lot of support activity!
[Forum posts](https://forum.image.sc/tag/imagej), [bug reports](/discuss/bugs),
[chat room](/discuss/chat) messages, and
[mailing list threads](/discuss/mailing-lists), and [more](/discuss).
I want to help, but it's rather overwhelming, especially taken together
with new development efforts and collaborations that are always ongoing.

If you are reading this, perhaps you have posted issues or support requests
that have gone unanswered for weeks, months, or even years. I wish I had the
energy to keep up consistently, but realistically there will always be too many
priorities to respond to everything adequately, despite
[all](https://github.com/ctrueden/monoqueue)
[my](https://github.com/ctrueden/tasks/issues)
[efforts](https://github.com/scijava/pom-scijava)
[to](https://github.com/ctrueden/dotfiles)
[stay](https://status.scijava.org/)
[organized](https://github.com/orgs/fiji/projects/1).

So I fear if you need my help, your best hope is to be loud and persistent about it:
mention `@ctrueden` on the [Image.sc Forum](https://forum.image.sc/) until I notice;
ping me on the [Image.sc Zulip](https://imagesc.zulipchat.com/); or even organize a
[hackathon](/events/hackathons) and invite me so that we can work together in person.

## Recommended development tools

*Last updated: 2026-Jan-28*

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
      <td rowspan="4">AI Coding Assistants</td>
      <td rowspan="4">Ignore the hype and the hate, and <a href="https://www.thatsoftwaredude.com/content/14227/how-to-actually-use-ai-as-a-developer-in-2026">learn to use them</a>&mdash;see my <a href="https://docs.google.com/presentation/d/1esXn1TU5G6KIzRzXM-47aEm9MgWkfidtnCApE5rxe80/present">talk slides from Dec 2025</a></td>
      <td><a href="https://github.com/features/copilot/cli">GitHub Copilot CLI</a></td>
      <td>GitHub Copilot Pro is <a href="https://docs.github.com/en/copilot/how-tos/manage-your-account/get-free-access-to-copilot-pro">free for teachers, students, and OSS maintainers</a></td>
    </tr>
    <tr>
      <td><a href="https://www.claude.com/product/claude-code">Claude Code</a></td>
      <td>Not free (Claude Pro is $20/month), but Claude is awesome&mdash;and Claude models are also available within Copilot</td>
    </tr>
    <tr>
      <td><a href="https://geminicli.com/">Gemini CLI</a></td>
      <td>A strong offering from Google</td>
    </tr>
    <tr>
      <td><a href="https://ollama.com/">Ollama</a></td>
      <td>Run LLMs locally for superior privacy</td>
    </tr>
    <tr>
      <td rowspan="3"><a href="/develop/ides">IDEs</a></td>
      <td rowspan="3">
        Super powerful
        <ul>
          <li>Easily navigate large projects</li>
          <li>Supreme code completion</li>
          <li>Illuminating debugger</li>
        </ul>
      </td>
      <td><a href="/develop/intellij">IntelliJ IDEA</a> (Java)</td>
      <td>For Java and Kotlin projects</td>
    </tr>
    <tr>
      <td><a href="https://www.jetbrains.com/pycharm/">PyCharm</a></td>
      <td>For Python projects</td>
    </tr>
    <tr>
      <td><a href="https://plugins.jetbrains.com/plugin/164-ideavim">IdeaVim</a></td>
      <td>Vim-fu inside JetBrains IDEs – almost as good as the real thing</td>
    </tr>
    <tr>
      <td rowspan=5><a href="https://www.vim.org/">Vim</a></td>
      <td rowspan=5>Great editor. Crazy fast <a href="https://vim.wikia.com/wiki/Macros">macros</a></td>
      <td><a href="https://github.com/VundleVim/Vundle.vim">Vundle</a></td>
      <td>Vim plugin manager</td>
    </tr>
    <tr>
      <td><a href="https://github.com/tpope/vim-sensible">vim-sensible</a></td>
      <td>Defaults everyone can agree on</td>
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
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/-/vimrc">my .vimrc</a></td>
    </tr>
    <tr>
      <td rowspan=6><a href="https://www.zsh.org/">Zsh</a></td>
      <td rowspan=6>Awesome shell – even <a href="https://www.slideshare.net/jaguardesignstudio/why-zsh-is-cooler-than-your-shell-16194692">better than bash</a></td>
      <td><a href="https://github.com/zpm-zsh/zpm">zpm</a></td>
      <td>Lightweight zsh plugin manager</td>
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
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/-/zshrc">my .zshrc</a></td>
    </tr>
    <tr>
      <td rowspan=2><a href="/develop/git">Git</a></td>
      <td rowspan=2>It is worth the pain, I promise</td>
      <td><a href="https://myrepos.branchable.com/">myrepos</a></td>
      <td>Commit, push & pull across repositories <a href="https://github.com/ctrueden/dotfiles/blob/-/mrconfig">en masse</a></td>
    </tr>
    <tr>
      <td colspan=2>See also <a href="https://github.com/ctrueden/dotfiles/blob/-/gitconfig">my .gitconfig</a></td>
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
