---
title: Coding style
section: Extend:Development
project: /libs/scijava
---

 We make a serious effort to keep the SciJava codebase clean, consistent and easy to read—which includes both the source code and the revision history.

## Interface-driven design

SciJava projects use an [interface-driven design](https://msdn.microsoft.com/en-us/library/aa260635%28v=vs.60%29.aspx) where possible. Public interfaces, enumerations and constants (i.e., `public static final` fields) form the basis of SciJava's API contract with downstream code. While we make an effort not to change the public methods and fields of non-interfaces, they may require occasional changes to improve the system.

## Versioning

SciJava projects use [Semantic Versioning](http://semver.org/). As of this writing, the project is still in beta, so the API is not finalized yet. But once we make the final 2.0.0 release, future versions will be fully compliant. See the [Architecture](/develop/architecture#versioning) page for further details.

## Naming

We have tried to name classes with similar logic to how the Java standard library does. We eschew the "I" prefix for interfaces, as well as the "Impl" suffix for implementations. Instead, like the Java standard library, we prefix abstract superclasses with "Abstract" and canonical implementations with "Default"—for example, the `Display` interface is implemented by an abstract superclass named `AbstractDisplay` and extended by a concrete implementation named `DefaultDisplay`.

## Cleverness

Because a large number of developers study the SciJava codebase, and it provides many examples of use, we try to provide [easy to understand, maintainable code](http://www.daedtech.com/writing-maintainable-code-demands-creativity). We avoid "clever" or obfuscated solutions to problems, since such code tends to be much harder to understand.

## SCM history

We try to follow best practices for maintaining a clean and organized Git history:

-   We provide a permanent, stable main branch (i.e., no force pushes).
-   We try to write [thorough, informative](http://chris.beams.io/posts/git-commit/) and [well-formatted](http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html) commit messages. As a rule of thumb: relevant information that cannot be deduced easily from the patch itself should be provided in the commit message's *body*, e.g. what other approaches were tried first and why they did not work, a motivating blurb why the patch is desirable, or links to discussions.
-   In general, we prefer merging to rebasing, so that individual commits continue to reflect what was actually the true development history (i.e., what was tested and working at the time). That said, we do use rebasing sometimes on topic branches to keep our commits well organized and easy to understand.
-   We use topic branches for large feature additions and complex code changes, and purge them promptly once merged to main. We prefer to make explicit merges (i.e. with `--no-ff`) to document the purpose of each merged branch.
-   To refine commits on topic branches, we use `git commit --fixup <commit>` extensively. Subsequent `git rebase --autosquash` will squash the fixup into the other commit.
-   In the case of unfinished work at the conclusion of a coding session, we commit it with the subject *WIP* and push to the topic branch. (Calling `git reset HEAD^` next time makes it easy to pick up the work from there.) Doing this reduces the chance of lost work, and makes it easier for other programmers to collaborate during development.
-   We avoid monster commits (with commit messages like "Many changes to several subsystems") in favor of well-separated, modular commits with one conceptual change at a time. Git's staging area feature makes this much easier (e.g., `git add -p`). Granular commits have many advantages; e.g., [`git` bisect`](/develop/git/pinpoint-regressions) becomes much more useful for understanding mysterious bugs.

## Javadoc and comments

We try to write Javadoc as code is added, rather than earmarking it for addition later. It is our intention to provide Javadoc for all public types. At minimum, we add TODO comments for any pending Javadoc. Our goal is for all Javadoc to render correctly as HTML (i.e., in web browsers) rather than abusing whitespace formatting in source.

We also have several comment tokens we use in various situations:

-   Anywhere the code may be unintuitive or surprising, we add an {% include wikipedia title='Nota bene' text='"NB"'%} comment that provides an explanation.
-   For code that is considered "dirty" or less than ideal, but necessary from a practical perspective, we add a {% include wikipedia title='Kludge#In_computer_science' text='"HACK"'%} comment explaining it.
-   For code (or lack thereof) that is considered wrong or broken, and in need of repair, we add a "FIXME" comment with the relevant developer's initials, to serve as a reminder to address it as soon as time allows.
-   When additional work is needed somewhere, but not urgently, we add a "TODO" comment marking it.
-   For temporary code intended to be removed as soon as possible, we label it with a "TEMP" token.

## Eclipse code style profiles

We provide [Eclipse configuration files in the source repository](https://github.com/scijava/scijava-coding-style) that define our rules for code structure and formatting. **NB** when downloading an `.epf` file from the repository, don't click *Save link as...*, rather create a file `my-file-name.epf`, and then copy-paste the contents of the file. To do this, click on `eclipse-preferences.epf` and then the *Raw* button.

You can import them to your system using {% include bc path='File | Import | Preferences'%} and selecting the `eclipse-preferences.epf` file. Then, in Eclipse preferences, navigate to {% include bc path='Java | Code Style | Clean Up'%} and select "ImageJ" for the active profile. You can then format your source code by right-clicking your source file(s) and choosing {% include bc path='Source | Clean Up'%} from the context menu. As of this writing, these rules are not automatically applied by CI, but we make an effort to apply them to the codebase occasionally by hand.

## Ordering of code blocks

For consistency, we prefer the following order for code blocks within a class:

1.  Public constants (i.e., `public static final`).
2.  Non-public constants.
3.  Static fields.
4.  Static initializer, if needed.
5.  Instance fields.
6.  Constructors.
7.  New public methods for that specific class.
8.  Public method overrides of the class's superclass(es).
9.  Public method implementations of the class's implemented interface(s), in the same order they appear in the interface(s).
10. Public, static methods (labeled "-- Utility methods --").
11. Protected event handler methods (labeled "-- Event handlers --").
12. Any other protected methods (labeled "-- Internal methods --").
13. Private methods (labeled "-- Helper methods --").
14. Deprecated methods (labeled " -- Deprecated methods --").
15. Inner types (labeled "-- Helper classes --").

We also try to label each section of code separately; i.e., each class's and interface's methods are labeled and grouped separately.

Even though modern IDEs provide a lot of functionality for understanding where methods and variables come from, we still believe this ordering makes it easier to find what you are looking for in code.

## Private over protected fields and methods

We prefer use of private fields and methods over protected ones, where possible. While non-private fields can be a convenient construct for classes intended to be subclassed, there are several disadvantages to using them:

1.  Protected fields provide an API contract to subclasses, which especially for reusable libraries must be carefully considered, just as you would public API. With too many protected fields, you can find yourself locked into your current internal design, with refactoring difficult or impossible.
2.  You cannot exercise any restrictions or control over the usage of the protected fields. Conversely, providing getters and setters for private fields offers the ability to define in code any restrictions you need on those fields.
3.  Relatedly, there is no mechanism in Java, even using a bytecode library such as Javassist, to add "seams" that inject or modify behavior when that field is read or written. For example, you could not later add a notification system for listeners that care about when the value of that field changes. In fact, you cannot detect at all when a field has changed, for the purposes of e.g. synchronization. We encountered this specific problem with [ImageJ2](/software/imagej2)'s legacy layer to [ImageJ](/software/imagej), since it has quite a few non-private fields: when unknown third-party code changes an ImageJ field which stores some portion of the ImageJ program state, we cannot update the corresponding ImageJ2 state to match. We still have essentially no solution to this dilemma (the best we have come up with so far is polling, which is complex and error prone).
4.  One nice usage of non-private fields is for "struct"-style classes, such as `java.awt.Rectangle`, with its `x`, `y`, `width` and `height` fields. If all you are looking for is a "dumb" data structure class consisting of collections of primitives and object references, it can suffice, but given the points above, it is almost always superior to use private fields with getters and setters, even in classes fully intended to be subclassed.

More observations on this issue can be found at [this post on StackOverflow](http://stackoverflow.com/a/3631338).

All of that said, there are times when use of the `protected` modifier is appropriate, so you will certainly see it in a few places in the SciJava codebase. In particular, we use `protected` for event handler methods, both to avoid unused method warnings in Eclipse, as well as to make it easier for subclasses to override the event handling behavior.

## See also

[Eclipse code style profiles and IntelliJ](/develop/intellij#code-style-profiles)
