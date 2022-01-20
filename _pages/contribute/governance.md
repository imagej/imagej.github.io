---
title: Governance
section: Contribute
nav-links: true
---

{% include notice icon="info" content='This page describes the *social* structure of [SciJava](/libs/scijava) projects.

-   For information on the *technical* structure, see [Architecture](/develop/architecture).
-   For information on the *legal* structure, see [Licensing](/licensing).' %}


The [ImageJ](/software/imagej) project, and related projects in the [SciJava](/libs/scijava) software ecosystem, are governed as [open source](/licensing/open-source) software projects. Everybody is welcome to [contribute](/contribute) with [plugins](/plugins), patches, [bug reports](/discuss/bugs), [tutorials](/tutorials), [documentation](/learn), and artwork.

That said, every project needs leaders: the ones who participate in *governance* of the project, {% include wikipedia title='Software maintenance' text='maintaining'%} the software and making key decisions.

## Project roles

Because [open source](/licensing/open-source) software (OSS) is highly collaborative, it is extremely important to understand the difference between various roles on the project, to avoid misconceptions about **authority** (who makes decisions) and **responsibility** (who is pledged to do the work) concerning each project.

The most common roles in OSS are:

-   **Founders** are the people who originally launched the project.
-   **Leads** are responsible for making final decisions. In the [open source](/licensing/open-source) world these people are often referred to as [benevolent dictators](http://catb.org/~esr/writings/homesteading/homesteading/ar01s16.html). Changes with a serious impact on the community are typically [discussed on open channels](/discuss) first.
-   **Maintainers** keep the project functional, fix bugs and make releases. They often make day to day decisions, and are typically involved in discussion with the project lead(s) regarding major decisions, although the lead has final decision-making authority.
-   **Developers** are people who work on the project significantly or often. Typically they have direct push access to the source code. In some cases they make day to day decisions, depending on their experience and comfort level with the project.
-   **Contributors** are people who help with the project either currently or in the past. They may participate occasionally or sporadically, and are typically not involved in project decision making.

### SciJava team roles

Projects in the [SciJava component collection](/develop/architecture) define each component's **team** as the group of people who take *responsibility* for it. The following roles formalize the ways people are pledged to help:

| Role        | Commitment                                                                                                                         |
|-------------|------------------------------------------------------------------------------------------------------------------------------------|
| Founder     | Created the project. Does not imply any current participation or responsibility.                                                   |
| Lead        | Has decision-making authority: timing of [releases](/develop/releasing), inclusion of features, etc.                              |
| Developer   | Adds new features or enhancements. Can be assigned to address feature requests.                                                    |
| Debugger    | Fixes [bugs](/develop/project-management#issue-tracking). Can be assigned open [issues](/develop/project-management#issue-tracking) to solve.                                        |
| Reviewer    | Reviews [patch submissions](/contribute).                                                                              |
| Support     | Responds to [community questions](/discuss) and [issue reports](/develop/project-management#issue-tracking). Keeps the issue tracker organized. |
| Maintainer  | Merges [patch submissions](/contribute). Cuts releases.                                                                |
| Contributor | Contributed code to the project. Does not imply any current participation or responsibility.                                       |

Individuals often fill more than one role.

## Component status

This website documents lots of software [components](/develop/architecture#definitions)—and in particular, many ImageJ [plugins](/plugins). Components in the ecosystem each have a distinct development path, with varying levels of maturity and activity, which is ultimately determined by the people who participate in developing it.

Each component's page features an informational sidebar with a status report derived from the component's declared *team*. This sidebar is intended to help users understand what level to expect when seeking help, reporting issues, and submitting feature requests.

### Development status

**Development status** conveys what to expect regarding a component's future.

| Status   | Meaning                                                                                                                                                                                     |
|----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Unstable | Project is under heavy development, with unstable API undergoing iterations of refinement. Typically, these components are either unreleased, or [versioned at 0.x](/develop/versioning). |
| Active   | New features are being actively developed. API breakages are kept as limited as possible.                                                                                                   |
| Stable   | No new features are under development. API is stable.                                                                                                                                       |
| Obsolete | The project is discontinued.                                                                                                                                                                |

### Support status

**Support status** indicates the level to which the team responds to questions and [issue reports](/discuss/bugs).

| Status  | Meaning                                                                                                                                                                                         |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Active  | Someone will respond to questions on community channels, and addresses issue reports in the project's issue tracker. A best effort is made to fix reported bugs within a reasonable time frame. |
| Partial | Someone will respond to questions on community channels, as well as to issue reports in the project's issue tracker. But reported bugs may not be addressed in a timely manner.                 |
| Minimal | There is at least one person pledged to the project in some capacity, but not all roles are filled. Response time to questions and issue reports may be protracted.                             |
| None    | No one is pledged to support the project. Questions and issue reports may be ignored.                                                                                                           |

## SciJava project summary

Here is a summary of roles for projects in the [SciJava](/libs/scijava) ecosystem.

{::nomarkdown}
<table>
  <tbody>
    <tr>
      <th>Logo</th>
      <th>Project</th>
      <th>Founders</th>
      <th>Leads</th>
      <th>Maintainers</th>
      <th>Developers</th>
      <th>Contributors</th>
    </tr>
    <tr>
      <td>
        {% include icon name='ImageJ' %}
      </td>
      <td>
        <strong><a href="/software/imagej">ImageJ</a></strong>
      </td>
      <td>
        {% include person id='rasband' %}
      </td>
      <td>
        {% include person id='rasband' %}
      </td>
      <td>
        {% include person id='rasband' %}<br>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='rasband' %}
      </td>
      <td>
        See <a href="https://imagej.nih.gov/ij/notes.html">release notes</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='ImageJ2' %}
      </td>
      <td>
        <strong><a href="/software/imagej2">ImageJ2</a></strong>
      </td>
      <td>
        {% include person id='ctrueden' %}<br>
        {% include person id='tnargsirrah' %}<br>
        {% include person id='eliceiri' %}<br>
        Anne Carpenter<br>
        Rudolf Oldenbourg

      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        <a href="https://github.com/orgs/imagej/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td rowspan="3" style="vertical-align: middle">
        {% include icon name='Fiji' %}
      </td>
      <td>
        <strong><a href="/software/fiji">Fiji</a></strong>
      </td>
      <td>
        {% include person id='dscho' %}<br>
        {% include person id='acardona' %}<br>
        {% include person id='tomancak' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        <a href="https://github.com/orgs/fiji/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        <strong><a href="/plugins/bdv">BigDataViewer</a></strong>
      </td>
      <td>
        {% include person id='tpietzsch' %}
      </td>
      <td>
        {% include person id='tpietzsch' %}
      </td>
      <td>
        {% include person id='tpietzsch' %}<br>
        {% include person id='StephanPreibisch' %}
      </td>
      <td>
        <a href="https://github.com/orgs/bigdataviewer/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/bigdataviewer/bigdataviewer-core/graphs/contributors">Info on GitHub</a>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        <strong><a href="/plugins/trakem2">TrakEM2</a></strong>
      </td>
      <td>
        {% include person id='acardona' %}
      </td>
      <td>
        {% include person id='acardona' %}
      </td>
      <td>
        {% include person id='acardona' %}<br>
        {% include person id='axtimwalde' %}<br>
        {% include person id='ctrueden' %}
      </td>
      <td>
        <a href="https://github.com/orgs/trakem2/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/trakem2/trakem2/graphs/contributors">Info on GitHub</a>
      </td>
      <td></td>
    </tr>
    <tr>
      <td>
        {% include icon name='SciJava' %}
      </td>
      <td>
        <strong><a href="/libs/scijava">SciJava</a></strong>
      </td>
      <td>
        {% include person id='joshmoore' %}<br>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        <a href="https://github.com/orgs/scijava/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='ImgLib2' %}
      </td>
      <td>
        <strong><a href="/libs/imglib2">ImgLib2</a></strong>
      </td>
      <td>
        {% include person id='axtimwalde' %}<br>
        {% include person id='StephanPreibisch' %}
      </td>
      <td>
        {% include person id='tpietzsch' %}<sup>1</sup><br>
        {% include person id='StephanPreibisch' %}<br>
        {% include person id='axtimwalde' %}
      </td>
      <td>
        {% include person id='tpietzsch' %}<br>
        {% include person id='ctrueden' %}<br>
        {% include person id='StephanPreibisch' %}<br>
        {% include person id='axtimwalde' %}
      </td>
      <td>
        <a href="https://github.com/orgs/imglib/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='SCIFIO' %}
      </td>
      <td>
        <strong><a href="/libs/scifio">SCIFIO</a></strong>
      </td>
      <td>
        {% include person id='ctrueden' %}<br>
        {% include person id='eliceiri' %}<br>
        {% include person id='hinerm' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        {% include person id='ctrueden' %}
      </td>
      <td>
        <a href="https://github.com/orgs/scijava/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='Bio-Formats' %}
      </td>
      <td>
        <strong><a href="/formats/bio-formats">Bio-Formats</a></strong>
      </td>
      <td>
        {% include person id='ctrueden' %}<br>
        {% include person id='eliceiri' %}
      </td>
      <td>
        {% include person id='melissalinkert' %}
      </td>
      <td>
        {% include person id='melissalinkert' %}<br>
        {% include person id='sbesson' %}
      </td>
      <td style="white-space: normal">
        <a href="https://github.com/openmicroscopy/bioformats/graphs/contributors">List on GitHub</a>
      </td>
      <td>
        See <a href="http://www.openmicroscopy.org/site/about/ome-contributors">OME Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='KNIME' %}
      </td>
      <td>
        <strong><a href="/software/knime">KNIME Image Processing</a></strong>
      </td>
      <td>
        {% include person id='dietzc' %}<br>
        Martin Horn
      </td>
      <td>
        {% include person id='dietzc' %}
      </td>
      <td>
        {% include person id='dietzc' %}<br>
        Martin Horn
      </td>
      <td>
        <a href="https://github.com/orgs/knime-ip/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='CellProfiler' %}
      </td>
      <td>
        <strong><a href="/software/cellprofiler">CellProfiler</a></strong>
      </td>
      <td>
        {% include person id='LeeKamentsky' %}<br>
        Anne Carpenter
      </td>
      <td>
        {% include person id='0x00b1' %}
      </td>
      <td>
        {% include person id='0x00b1' %}
      </td>
      <td>
        <a href="https://github.com/orgs/CellProfiler/people">List on GitHub</a>
      </td>
      <td>
        See <a href="/people">Contributors</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='OMERO' %}
      </td>
      <td>
        <strong><a href="/software/omero">OMERO</a></strong>
      </td>
      <td>
        {% include person id='joshmoore' %}<br>
        Jean-Marie Burel<br>
        Chris Allan<br>
        Jason Swedlow
      </td>
      <td>
        {% include person id='joshmoore' %}<br>
        Jean-Marie Burel<br>
        Chris Allan
      </td>
      <td>
        <a href="https://github.com/orgs/openmicroscopy/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/orgs/openmicroscopy/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/openmicroscopy/openmicroscopy/graphs/contributors">Info on GitHub</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='Icy' %}
      </td>
      <td>
        <strong><a href="/software/icy">Icy</a></strong>
      </td>
      <td>
        Stephane Dallongeville<br>
        {% include person id='Fab14' %}<br>
        Jean-Christophe Olivo-Marin
      </td>
      <td>
        Stephane Dallongeville<br>
        {% include person id='Fab14' %}
      </td>
      <td>
        Stephane Dallongeville<br>
        {% include person id='Fab14' %}
      </td>
      <td>
        <a href="https://github.com/orgs/Icy-imaging/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/Icy-imaging/Icy-Kernel/graphs/contributors">Info on GitHub</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='Alida' %}
      </td>
      <td>
        <strong><a href="/software/alida">Alida</a></strong>
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
        <a href="https://github.com/orgs/alida-hub/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/alida-hub/alida/graphs/contributors">Info on GitHub</a>
      </td>
    </tr>
    <tr>
      <td>
        {% include icon name='MiToBo' %}
      </td>
      <td>
        <strong><a href="/plugins/mitobo">MiToBo</a></strong>
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
      Stefan Posch<br>
      Birgit Möller
      </td>
      <td>
        <a href="https://github.com/orgs/mitobo-hub/people">List on GitHub</a>
      </td>
      <td>
        <a href="https://github.com/mitobo-hub/mitobo/graphs/contributors">Info on GitHub</a>
      </td>
    </tr>
  </tbody>
</table>
{:/}

<sup>1</sup> Pietzsch leads on day to day issues. Pietzsch, Preibisch and Saalfeld vote on primary decisions, with Pietzsch's vote breaking ties.  

## Further reading

-   [OSS Watch's article on Governance Models](http://oss-watch.ac.uk/resources/governancemodels)
-   Eric S. Raymond's [Homesteading the Noosphere](http://catb.org/~esr/writings/homesteading/homesteading/)
-   Eric S. Raymond's [The Cathedral and the Bazaar](http://www.catb.org/esr/writings/cathedral-bazaar/cathedral-bazaar/)
