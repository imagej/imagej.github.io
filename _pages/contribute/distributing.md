---
title: Distribution
section: Contribute
nav-links: true
---

If you create a useful extension of ImageJ—e.g., a [plugin](/plugins), [script](/scripting/script-editor) or [macro](/scripting/macro)—the next step is to *distribute* it to others, including:

-   **Distribute** the extension itself to users
-   Share the extension's **source code**
-   **Document** the extension somewhere

## Best practices

Here is a quick summary of the most recommended options:

-   **Distribution:**
    -   A\) **[create your own update site](/update-sites/setup)**; or
    -   B\) **[bundle your plugin with Fiji](/contribute/fiji)**.
-   **Source code:**
    -   Make your project **[open source](/licensing/open-source)**.
    -   Host it on **[GitHub](/develop/github)**.
    -   Use **[Maven](/develop/maven)** to build and SemVer for **[versioning](/develop/versioning)**.
    -   Use **[Travis](/develop/travis)** for continuous integration and artifact deployment to the [SciJava Maven repository](/develop/project-management#maven).
-   **Documentation.**
    -   Create a page here on the **[ImageJ Wiki](/)**.

The tables below discuss additional options for these three aspects of distribution. Green items are recommended. Other options are given but not recommended for various reasons.

## Distributing your extension

The first goal is to get your extension into the hands of users.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <td style="background: #afa" colspan=4>
        <p><strong>Create your own update site</strong></p>
      </td>
    </tr>
    <tr>
      <td>
        <p><strong>Steps</strong></p>
      </td>
      <td>
        <p><strong>Installation</strong></p>
      </td>
      <td>
        <p><strong>Advantages</strong></p>
      </td>
      <td>
        <p><strong>Disadvantages</strong></p>
      </td>
    </tr>
    <tr>
      <td style="background: #dfd; vertical-align: top">
        <ul>
          <li><strong><a href="/update-sites/setup">Create your update site</a></strong>, then <strong><a href="/update-sites/setup#uploading-files-to-your-update-site">upload your extension to it</a></strong>.</li>
          <li>You may add your update site to the list of built-in sites by editing the <strong><a href="/list-of-update-sites">list of update sites</a></strong> page.</li>
          <li>To release a new version, <strong><a href="/update-sites/setup#uploading-files-to-your-update-site">upload it to the update site</a></strong>.</li>
        </ul>
      </td>
      <td style="background: #dfd; vertical-align: top">
        <ul>
	  <li> Users <b><a href="/update-sites/following">enable the update site</a></b> to receive your extension.</li>
	  <li> ImageJ's <b><a href="/plugins/updater">Updater</a></b> automatically checks for updates from all enabled update sites.</li>
        </ul>
      </td>
      <td style="background: #dfd; vertical-align: top">
        <ul>
	  <li> You do not need server space to host your extensions; you can use a <b><a href="/update-sites/setup">hosted update site</a></b> on <code>sites.imagej.net</code>.</li>
          <li> Alternately, you can retain full control by hosting your update site yourself.</li>
          <li> Users are notified of updates without needing to check proactively.</li>
          <li> The updater manages dependencies for you.</li>
          <li> You can automate distribution using the <b><a href="/plugins/updater#command-line-usage">command line updater</a></b>.</li>
        </ul>
      </td>
      <td style="background: #dfd; vertical-align: top">
        <ul>
	  <li> <b>The <a href="/software/imagej">original ImageJ</a></b> does not support update sites; users will need to use <b><a href="/software/imagej2">ImageJ2</a></b> (or <b><a href="/software/fiji">Fiji</a></b>: "Fiji Is Just ImageJ2").</li>
          <li> You will miss out on the <b><a href="/develop/project-management">tools and tests</a></b> used to ensure compatibility and reproducibility, making undetected breakages much more likely (at the least).</li>
        </ul>
      </td>
    </tr>
<tr>
<td colspan="4" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="4" style="background: #afa"> <b>Distribute it as part of Fiji</b>
</td></tr>
<tr>
<td style="background: #dfd"><b>Steps</b>
</td>
<td style="background: #dfd"><b>Installation</b>
</td>
<td style="background: #dfd"><b>Advantages</b>
</td>
<td style="background: #dfd"><b>Disadvantages</b>
</td></tr>
<tr>
<td style="background: #dfd; vertical-align: top">
<ul><li> Make a post on the <b><a href="/discuss" title="Forum">ImageJ forum</a></b> to initiate a request.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> Users <b><a href="/software/fiji/downloads" title="Fiji/Downloads">install Fiji</a></b>, or <b><a href="/update-sites/following" title="How to follow a 3rd party update site">enable the Fiji update site</a></b>.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> Your extension is available with Fiji out of the box.</li>
<li> A <b><a href="/contribute/governance" title="Governance">Fiji maintainer</a></b> will help you to manage your project.</li>
<li> You can lean on existing tools and documentation to maintain <b><a href="/develop/architecture#reproducible-builds" title="Reproducible builds">reproducibility</a></b> of your project.</li>
<li> Your project will always be compatible with the latest Fiji distribution.</li>
<li> <a href="/develop/travis" title="Travis">Travis</a> automatically tests your project for errors, deploying successful builds to the <a href="/develop/project-management#maven" title="SciJava Maven repository">SciJava Maven repository</a>.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> You must abide by the <b><a href="/contribute/fiji" title="Fiji contribution requirements">Fiji contribution requirements</a></b>.</li>
<li> You must rely on a Fiji maintainer (for now) to upload new versions for you.</li></ul>
</td></tr>
<tr>
<td colspan="4" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="4" style="background: lightgray"> <b>Serve it from a website as a download</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Installation</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Create an archive (TAR, ZIP, etc.).</li>
<li> Upload the archive to the relevant web space, and link it.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Users download the archive, unpacking it into ImageJ's <code>plugins</code> folder.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> You avoid the activation barrier of learning to use the <a href="/plugins/updater" title="Updater">Updater</a>.</li>
<li> <a href="/software/imagej2" title="ImageJ2">ImageJ2</a> is not required to install the extension.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Users must find your plugin via a link or web search.</li>
<li> Users must perform a manual installation procedure.</li>
<li> Users must manually check for later updates.</li>
<li> Users <i>will</i> report bugs found in outdated versions of the extension.</li></ul>
</td></tr></table>
{:/}

## Sharing your source code

If you want to facilitate good science, please [share your source code](/licensing/open-source). Otherwise, your extension is a black box and its results are not verifiable.

{::nomarkdown}
<table>
<tr>
<td colspan="3" style="background: #afa"> <b>Host on GitHub in your userspace or organization</b>
</td></tr>
<tr>
<td style="background: #dfd"> <b>Steps</b>
</td>
<td style="background: #dfd"> <b>Advantages</b>
</td>
<td style="background: #dfd"> <b>Disadvantages</b>
</td></tr>
<tr>
<td style="background: #dfd; vertical-align: top">
<ul><li> Create an account on <b><a rel="nofollow" class="external text" href="https://github.com">GitHub</a></b>.</li>
<li> <b><a rel="nofollow" class="external text" href="https://help.github.com/articles/create-a-repo">Create a new repository</a></b> for your project.</li>
<li> <b><a rel="nofollow" class="external text" href="https://help.github.com/articles/pushing-to-a-remote">Push your code</a></b> there.</li>
<li> <b><a href="/develop/git" title="Git">Learn Git</a></b> to manage your code effectively.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> Git is an incredibly powerful way to keep track of your code.</li>
<li> GitHub greatly facilitates collaboration: sharing ideas and patches.</li>
<li> Seriously: Git and GitHub are amazing tools, and you will be orders of magnitude less effective without them.</li>
<li> "Doing it in public" is a great way to <b><a rel="nofollow" class="external text" href="http://blog.codinghorror.com/how-to-stop-sucking-and-be-awesome-instead/">stop sucking and be awesome instead</a></b>.</li>
<li> All of <b><a href="/software/imagej" title="ImageJ">ImageJ</a></b>, <b><a href="/software/imagej2" title="ImageJ2">ImageJ2</a></b>, <b><a href="/software/fiji" title="Fiji">Fiji</a></b> and related <b><a href="/libs/scijava" title="SciJava">SciJava</a></b> projects are <b><a href="/develop/source" title="Source code">hosted on GitHub</a></b>.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> Git has a steep learning curve—the <b><a rel="nofollow" class="external text" href="https://desktop.github.com/">GitHub Desktop</a></b> client makes things easier.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: #afa"> <b>Host on GitHub in the Fiji organization (for <a href="/software/fiji" title="Fiji contribution requirements">extensions distributed with Fiji</a>)</b>
</td></tr>
<tr>
<td style="background: #dfd"><b>Steps</b>
</td>
<td style="background: #dfd"><b>Advantages</b>
</td>
<td style="background: #dfd"><b>Disadvantages</b>
</td></tr>
<tr>
<td style="background: #dfd; vertical-align: top">
<ul><li> Request a <b><a href="/contribute/governance" title="Governance">Fiji maintainer</a></b> create a repository for you and add you as a contributor.</li>
<li> Meet the <b><a href="/contribute/fiji" class="mw-redirect" title="Fiji contribution requirements">Fiji contribution requirements</a></b>.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> All the benefits of GitHub.</li>
<li> A <b><a href="/contribute/governance" title="Governance">Fiji maintainer</a></b> helps you to manage your project.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> You must abide by the <b><a href="/contribute/fiji" class="mw-redirect" title="Fiji contribution requirements">Fiji contribution requirements</a></b>.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Host on BitBucket</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Similar to GitHub, but using <a rel="nofollow" class="external text" href="https://bitbucket.org/">BitBucket</a> instead.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Similar to GitHub.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> ImageJ and related projects are hosted on GitHub, not BitBucket.</li>
<li> BitBucket has a smaller user base than GitHub does.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Host on SourceForge</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Similar to GitHub, but using <a rel="nofollow" class="external text" href="http://sourceforge.net/">SourceForge</a> instead.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> SourceForge predates GitHub; some people prefer it.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> The interface is not as powerful as GitHub and BitBucket: 
<ul><li> Common workflows require many more mouse clicks.</li>
<li> The user interfaces of GitHub and BitBucket provide much better guidance.</li>
<li> SourceForge's servers tend to be very slow compared to GitHub and BitBucket.</li>
<li> The collaboration features are vastly inferior.</li></ul></li>
<li> SourceForge has a lot of downtime. (The <a rel="nofollow" class="external text" href="/develop/jenkins">ImageJ mirrors of SourceForge projects</a> hence have a lot of problems.)</li>
<li> Using SourceForge is highly discouraged compared to other code hosting sites.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Serve it from a website as a download</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Create an archive (TAR, ZIP, etc.).</li>
<li> Upload the archive to the relevant web space, and link it.</li>
<li> Users download and unpack the archive.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> You avoid the activation barrier of learning a revision control system.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> No revision control system.</li>
<li> No easy browsing of source code online.</li>
<li> No easy submission of patches.</li>
<li> No finding the code in web searches.</li>
<li> No reading the change logs to understand why changes were made.</li>
<li> No studying the history to better understand the project's activity.</li>
<li> No bisecting the history to track down when bugs were introduced.</li>
<li> No safety net to revert unwanted changes or avoid lost work.</li>
<li> No branching to maintain multiple development trajectories.</li>
<li> No easy switching between versions.</li>
<li> No automatic credit and tracking of which authors did which work.</li>
<li> No distribution and backup of the project's development history.</li></ul>
</td></tr></table>
{:/}

## Documenting your extension

Useful extensions deserve corresponding documentation explaining how to use them.

{::nomarkdown}
<table>
<tr>
<td colspan="3" style="background: #afa"> <b>Create an ImageJ wiki page</b>
</td></tr>
<tr>
<td style="background: #dfd"> <b>Steps</b>
</td>
<td style="background: #dfd"> <b>Advantages</b>
</td>
<td style="background: #dfd"> <b>Disadvantages</b>
</td></tr>
<tr>
<td style="background: #dfd; vertical-align: top">
<ul><li> <b><a href="/editing#creating-a-new-page">Create a page</a></b> for your extension.</li></ul>
</td>
<td style="background: #dfd; vertical-align: top">
<ul><li> The ImageJ wiki is a central repository of ImageJ-related community knowledge and documentation.</li>
<li> The ImageJ wiki uses Jekyll with GitHub Pages; see [Editing the Wiki](/editing) for details.</li>
</td>
<td style="background: #dfd; vertical-align: top">
<p>-
<li> You can get started immediately, but your first edit will be submitted as a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) (PR), where it will be approved by another editor. After that, you will be added to the list of direct editors, so that subsequent edits do not need to go through the PR mechanism (although they still can, if you prefer to have others review your changes before they go live).</li></ul>
</p>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Use the ImageJ Information and Documentation Portal (IIDP)</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Request an account from an IIDP administrator.</li>
<li> <a rel="nofollow" class="external text" href="http://imagejdocu.list.lu/doku.php?id=create_new_content">Create a page</a> for your extension.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> The <a rel="nofollow" class="external text" href="http://imagejdocu.list.lu/">ImageJ Information and Documentation Portal</a> predates the ImageJ wiki, and many extensions are still primarily documented there.</li>
<li> The IIDP is a fairly <a rel="nofollow" class="external text" href="http://imagejdocu.list.lu/doku.php?id=start&amp;do=recent">active</a> wiki (but not <a href="https://github.com/imagej/imagej.github.io/commits/main" title="Recent changes">compared to this one</a>!).</li>
<li> The ImageJ developers hope to unify these two wikis in the future.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> The IIDP documents only the original <a href="/software/imagej" title="ImageJ">ImageJ</a>, not <a href="/software/imagej2" title="ImageJ2">ImageJ2</a>.</li>
<li> You must explicitly request an IIDP account from an administrator.</li>
<li> The wiki uses Plone, a lesser known CMS engine.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Add a page to the ImageJ website</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top">
<ul><li> Prepare an HTML page modeled after the <a rel="nofollow" class="external text" href="https://imagej.nih.gov/ij/plugins/index.html">list of ImageJ plugins</a>.</li>
<li> Email it to <a href="/people/rasband" title="Wayne Rasband">Wayne Rasband</a>, the developer of ImageJ, and sole maintainer of the <a rel="nofollow" class="external text" href="https://imagej.nih.gov/ij">ImageJ website</a>.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Listed on the ImageJ website.</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Not collaborative. No one else can edit the ImageJ website—not even you!</li>
<li> Hence, turnaround time on updates is longer.</li>
<li> The list of plugins there is extensive and difficult to sort through.</li></ul>
</td></tr>
<tr>
<td colspan="3" style="background: white; border: none; height: 1em">
</td></tr>
<tr>
<td colspan="3" style="background: lightgray"> <b>Create your own webpage elsewhere</b>
</td></tr>
<tr>
<td><b>Steps</b>
</td>
<td><b>Advantages</b>
</td>
<td><b>Disadvantages</b>
</td></tr>
<tr>
<td style="vertical-align: top"> (Varies)
</td>
<td style="vertical-align: top">
<ul><li> Total control of the content</li></ul>
</td>
<td style="vertical-align: top">
<ul><li> Nonstandard location. Users may have trouble finding your documentation.</li>
<li> Not collaborative. No one else can improve the documentation.</li>
<li> If your site goes down, users lose access to the information. (This happened with the <a href="/plugins/3d-viewer" title="3D Viewer">3D Viewer</a> and <a href="/plugins/vib-protocol" title="VIB Protocol">VIB Protocol</a> on multiple occasions. And the <a href="/software/mbf-imagej" title="MBF Plugin Collection">MBF Plugin Collection</a> went permanently offline!)</li></ul>
</td></tr></table>
{:/}
