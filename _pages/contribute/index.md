---
title: Contributing
section: Contribute
nav-links: true
---

{% include notice icon="osi-symbol" content="The [ImageJ](/software/imagej)
  project, and related projects in the [SciJava](/libs/scijava)
  software ecosystem, are [open source](/licensing/open-source) software
  projects. See the [Licensing](/licensing) page for details." %}

Everybody is welcome to [contribute](/contribute) with [plugins](/plugins),
[patches](/develop/github), [bug reports](/discuss/bugs),
[tutorials](/tutorials), [documentation](/learn), and artwork.

The community encourages discussion about proposed changes on ImageJ's [communication channels](/discuss/#ways-to-get-help). Submit your ideas!

Start on the [Image.sc Forum](https://forum.image.sc/), searching for discussions related to your contribution to get some context & background. It can also be helpful to [search](/discuss#searching-imagej-resources) for applicable issues and plans across the spectrum of ImageJ resources. The ImageJ community believes that [public discussion is important](/develop/philosophy#open-source) so that ideas are exposed to healthy alternate points of view rather than lost.

If you are interested in helping to tackle open issues, see the [wish list](/develop/wish-list) page.

## This website

This site, imagej.net, is a wiki (similar to the {% include wikipedia title='Wikipedia' text='Wikipedia'%} project). This site is built by the ImageJ community, and anyone can contribute!

Contributing documentation is an easy way to give back to the community without needing to learn software development skills.

If you are a software developer, please consider [documenting your work on this site](/contribute/distributing#documenting-your-extension). You can also create your own [tutorial](/tutorials).

When in doubt, [discuss](/discuss) your ideas publicly on the [Image.sc Forum](https://forum.image.sc/)!

## ImageJ2

Submit patches to [ImageJ2](/software/imagej2) via [pull requests](https://help.github.com/articles/using-pull-requests/) against [ImageJ2's source on GitHub](https://github.com/imagej).

Note that since ImageJ2 has a modular [architecture](/develop/architecture), it is possible that your change would be more applicable to one of the supporting technologies such as [ImgLib2](https://github.com/imglib), [SCIFIO](https://github.com/scifio) or [SciJava](https://github.com/scijava).

## ImageJ

Changes to the original [ImageJ](/software/imagej) are made by {% include person id='rasband' %}, the ImageJ developer, along with many contributors. He takes patch submissions and then reworks them to fit within the project's development model and style before merging them. Attribution for the changes is noted in the release notes (see [Release Notes/News](https://imagej.nih.gov/ij/notes.html)).

Methods of getting the patch to Wayne include:

-   Submit a pull request on GitHub against {% include github org='imagej' repo='imagej1' label='the ImageJ repository' %}. Be aware that PRs will be reviewed and integrated by hand, not merged via the standard Git/GitHub workflow.
-   Send the modified code in a [private mail to Wayne](mailto:rasband@gmail.com).

The important part is that Wayne receive the code/patch, since he is the only one with the authority to merge it.

(See also this [nice response](https://list.nih.gov/cgi-bin/wa.exe?A2=IMAGEJ;17b8ec52.1406) from Curtis Rueden on the ImageJ mailing list.)
