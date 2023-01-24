---
title: Dotfiles
section: Extend:Development:Tools
---

There are several [dotfiles](https://dotfiles.github.io/) repositories filled with command line configuration goodness for the different [layers](/develop/architecture) of the [SciJava](/libs/scijava) component collection.

## Repositories

You can find the dotfiles in the following repositories:

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/people/ctrueden"><img src="https://gravatar.com/avatar/63df759e2779af56fd050a968ff98d09" width="48" height="48"></a><br>
        {% include github org='ctrueden' repo='dotfiles' label='ctrueden/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/libs/scijava"><img src="/media/icons/scijava.png" width="48px"></a><br>
        {% include github org='scijava' repo='dotfiles' label='scijava/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/software/imagej2"><img src="/media/icons/imagej2.png" width="48px"></a><br>
        {% include github org='imagej' repo='dotfiles' label='imagej/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/orgs/loci"><img src="/media/logos/loci.png" width="48px"></a><br>
        {% include github org='uw-loci' repo='dotfiles' label='uw-loci/dotfiles' %}</p>
      </td>
    </tr>
    <tr>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/libs/imglib2"><img src="/media/icons/imglib2.png" width="48px"></a><br>
        {% include github org='imglib2' repo='dotfiles' label='imglib2/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/libs/scifio"><img src="/media/icons/scifio.png" width="48px"></a><br>
        {% include github org='scifio' repo='dotfiles' label='scifio/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/software/fiji"><img src="/media/icons/fiji.png" width="48px"></a><br>
        {% include github org='fiji' repo='dotfiles' label='fiji/dotfiles' %}</p>
      </td>
      <td style="text-align: center; vertical-align: bottom">
        <p><a href="/plugins/flimj"><img src="/media/icons/slim-curve.png" width="48px"></a><br>
        {% include github org='flimlib' repo='dotfiles' label='flimlib/dotfiles' %}</p>
      </td>
    </tr>
  </tbody>
</table>
{:/}

## What's included?

There are several tools for which configuration and customization is provided:

-   Shells: [bash](https://www.gnu.org/software/bash/) and [zsh](http://www.zsh.org/)
-   Editors: [Vim](http://www.vim.org/)
-   SCM tools: [Git](/develop/git) and [myrepos](https://myrepos.branchable.com/)

Where possible, configuration is driven by plugin managers:

-   [zpm](https://github.com/zpm-zsh/zpm) and [Oh-My-Zsh](http://ohmyz.sh/) for zsh
-   [Vundle](https://github.com/VundleVim/Vundle.vim) for vim

## How to get started?

Bootstrap:
```bash
cd
mkdir -p code/ctrueden
cd code/ctrueden
git clone git://github.com/ctrueden/dotfiles
cd dotfiles
sh setup.sh
```

Clone code for organization(s) of interest—e.g., imagej:
```bash
cd
mkdir -p code/imagej
cd code/imagej
mr up
```

Switch to zsh:
```bash
# on Linux
sudo apt-get install zsh
sudo chsh -s /bin/zsh

# on macOS
brew install zsh
sudo chsh -s /usr/local/bin/zsh

# on Windows, use Chocolatey to install Cygwin
choco install cygwin cyg-get
# and then from Cygwin:
cyg-get install zsh
chsh -s /bin/zsh
```
