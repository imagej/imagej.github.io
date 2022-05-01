---
title: Why Closed-Source Is Wrong
section: Contribute:Licensing:Proprietary
---

This page has a few war stories about having to fight with developing software where you should not need to fight.

{% include notice icon="note" content="There are places for closed-source.
  Research, however, is only impeded by closed-source." %}

## QuickTime for Java

QuickTime for Java is a small component on top of the QuickTime SDK (software development kit). In theory, it should make it easy to create movies in QuickTime format. In practice, it is a hassle:

-   QuickTime is only supported on Windows and macOS. Good bye, Linux users.
-   QuickTime for Java is not supported on 64-bit macOS. Which means that every time you try to write a QuickTime movie on that platform, it complains that QuickTime is not installed. Good bye, almost every new macOS user.
-   QuickTime for Java does not follow a standard API (see also "Java Media Framework" below). So you will never be able to write code that writes movies in general. You will always have to special-case QuickTime. Goodbye, disgusted developers.

All in all, QuickTime is just a nuisance, and were it not for Apple shipping it by default with every of their computers, the format would be long dead: the .avi format is a much more open and wider-spread format that does everything QuickTime ever could do, and more.

If QuickTime for Java was [open source](/licensing/open-source), we could do something about the problems, at least.

## TransformJ

For a long time, the [TransformJ](/plugins/transformj) plugin suite was closed-source. As it is used for science, we asked the author whether we could look at the source. Scientific process must be transparent so that other scientists can understand and question it. The skepticism in science arises not so much of distrust, but more of the knowledge that we are all human, and humans err.

Happily, the author of TransformJ—Erik Meijering—agreed to let us redistribute the source code for exactly that purpose: that you can understand how it works, and why.

Therefore, TransformJ is not so much an example why closed-source is wrong, but why [open source](/licensing/open-source) is right!

## Java Media Framework

Sun was never really open, except when it had to.

It open-sourced Java only because IBM and others threatened them in a big way starting the [Harmony](http://harmony.apache.org/) project, which was basically an [open source](/licensing/open-source) rewrite of the complete Java Suite, licensed via the [Apache License](/licensing/apache) (which allows companies to take the source code, make a product of it, and never give anything back to the original authors—in contrast to the [GNU Public License](/licensing/gpl)). Facing this huge opposition, Sun had only one chance to keep their advantage (already having a full implementation): make their version of Java truly [open source](/licensing/open-source), and licensing it in a way that would guarantee other companies a disadvantage, namely via the [GNU Public License](/licensing/gpl). In a sense, this license is used against its original intention: as a weapon in cut-throat business against IBM and friends. But at least the common coder gets something nice in the process: true (albeit fair) freedom with the code.

It will take a few years, probably, until the Java Media Framework is licensed in a true [open source](/licensing/open-source) manner: at the moment, you can download the binaries, but not redistribute them; You can only get the source code under a pretty restrictive research license, and only if you ask personally, and you cannot redistribute it either.

Due to these limitations, it must have been obvious to everybody from the beginning, that the API was doomed. If you have to depend on the whims of a company that can retract the basis of your software if it pleases them, you will not even start writing that software.

## SUSAN

Did you ever hear of the SUSAN edge detector? If you have, you are one of a few lucky. Why? This is a sad story how to utterly destroy the value of your research, once and for all.

Granted, SUSAN is not closed-source, but for all *practical* matters, it is. Its license is pretty restrictive (much like Java's "Java Research License"), and it points out pretty strongly that there is a patent on the algorithm, and that you are not free to do anything with it.

To this day, [this](http://www.pvv.org/~perchrh/imagej/smooth.html) is the only adaptation of the SUSAN algorithm in Java, which does not even detect edges, but only smoothes images. And it uses the platform-dependent SUSAN library which is only bundled for 32-bit Linux and Windows, which flies in the face of the platform-independence Java is supposed to give you.

Yes, they wanted to protect their research—let's not even try to fool ourselves into believing (or for that matter, try to insult people's intelligence by pretending) that this has anything to do with "property"—by patenting the algorithm, and putting the code under a very restrictive license. Unfortunately, they succeeded in protecting their research from being enhanced, being widely used, or even being meaningful for anybody.
