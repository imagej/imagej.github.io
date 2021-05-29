---
mediawiki: NONE
title: The Great Wiki Launch
description: This page organizes the community effort to launch the new ImageJ wiki.
---

| **What**  | In order to launch the new ImageJ website at the highest possible level of quality, we need to do a pass over all the content, [correcting broken syntax](https://github.com/imagej/imagej.github.io/issues/117), [organizing the plugin categories](https://github.com/imagej/imagej.github.io/issues/119), and making notes about any remaining issues. |
| **Why**   | Because there are more than 1400 pages which were mass converted from the old MediaWiki, and there are still rough edges that cannot be fixed automatically. |
| **Who**   | ***We will all do it as a team!*** Please join us&mdash;[sign up here](https://docs.google.com/spreadsheets/d/1CdRCMFBXCg6ypDGdDaZNEN5cBY_1Ye47-kyTZQ11wBQ/edit#gid=0) |
| **Where** | We will meet virtually in the [wiki chat room](https://gitter.im/imagej/imagej.github.io) and in a [gather.town space](https://gather.town/app/ipHMoZp6WOdATHE4/FijiHackathon) (for audio/video; still under construction). |
| **When**  | Tuesday, June 1 through Friday, June 4: the first of five **virtual Fiji summer hacking weeks**. Kickoff meeting (attendance optional!) will be Tuesday at 1300 UTC (3pm CEST / 8am CT). |
| **How**   | The [How you can help](#how-you-can-help) section below has all the details. |

## About gather.town

{% include notice icon='warning' content='The gather.town for next week
  is still under construction! This page will be updated accordingly when it is
  fully ready.' %}

The [I2K 2020 virtual
conference](https://www.janelia.org/you-janelia/conferences/from-images-to-knowledge-with-imagej-friends)
used gather.town to great effect, creating a nice shared virtual space even
though the community could not gather in person. We are doing the same for the
Fiji hacking weeks: this space will provide a place for you to jump in and out
of the effort according to your availability over the course. You have the
option to turn on audio, video, or both while in the town.

Alternately, you are of course also welcome to participate solely
[via chat](https://gitter.im/imagej/imagej.github.io).
But participating in some aspects may not be feasible via text alone; e.g.,
{% include person id='ctrueden' %} will give a video presentation covering
the state of the site some time on Tuesday after the hackathon kickoff, and
it is likely this will be on gather.town.

## How you can help

{% include notice icon="tip" content="Even if you only have a little time to
  help, anything you can do to make progress will help to launch the site by
  the target date of Friday, June 4!
  [Sign up here](https://docs.google.com/spreadsheets/d/1CdRCMFBXCg6ypDGdDaZNEN5cBY_1Ye47-kyTZQ11wBQ/edit#gid=0)."
%}

More details will be posted here before Tuesday. PLEASE STAY TUNED!

**What's coming:**
* A checklist of details to consider when reviewing a page.
* A guide covering how to correct common problems discovered.
* Instructions on how to file issues on GitHub for problems
  that are too complex for us to fix during the hackathon week.
* Suggestions on how to choose pages you might enjoy working on.

## Important links

* [Organizational spreadsheet](https://docs.google.com/spreadsheets/d/1CdRCMFBXCg6ypDGdDaZNEN5cBY_1Ye47-kyTZQ11wBQ/edit)
  with two parts: the
  [sign-up sheet](https://docs.google.com/spreadsheets/d/1CdRCMFBXCg6ypDGdDaZNEN5cBY_1Ye47-kyTZQ11wBQ/edit#gid=0)
  and the
  [pages to review](https://docs.google.com/spreadsheets/d/1CdRCMFBXCg6ypDGdDaZNEN5cBY_1Ye47-kyTZQ11wBQ/edit#gid=1).
* [Image.sc Forum thread](https://forum.image.sc/t/53246)
  where this project is being discussed.
* [Wiki editing guide](/editing) which teaches how to edit this wiki.
* [Road to Production](https://github.com/imagej/imagej.github.io/projects/2)
  project board on GitHub with a bird's eye view of issues
  remaining to address before the site launches. As a group,
  we will focus on issues in the "To do - crowdsource!" column,
  particularly
  [#117](https://github.com/imagej/imagej.github.io/issues/117),
  [#119](https://github.com/imagej/imagej.github.io/issues/119),
  and [#57](https://github.com/imagej/imagej.github.io/issues/57),

<style>
.todo-list {
  column-width: 18em;
  column-gap: 2em;
  line-height: 1em;
}
.todo-list ul {
  break-inside: avoid;
}
.todo-list li {
  padding-bottom: 0.5em;
}
</style>

## Pages on the site

As we review pages and mark them done, they will automatically jump from
[Pages remaining](#pages-remaining) to [Completed pages](#completed-pages).
Our goal is to review every page by the end of Thursday, June 4!
WE CAN DO IT! 💪

## Pages remaining

{%- assign todo-pages = site.pages | where_exp: "p", "p.mediawiki != nil" | sort: "url" -%}
{%- assign remain = todo-pages | size -%}
{%- assign total = site.pages | size -%}
{%- assign done = total | minus: remain -%}
{%- assign percent = done | times: 100 | divided_by: total -%}

{%- comment -%} Progress bar! {%- endcomment %}
<style>
.progress-bar {
  width: 100%;
  border: 1px solid gray;
  position: relative;
  margin: 1em 0;
  text-align: center;
  font-weight: bold;
}
.progress-bar div {
  position: absolute;
  top: 0;
  opacity: 0.3;
  background-image: repeating-linear-gradient(120deg, skyblue, gold 30px, skyblue 30px, gold 60px);
  border-right: 1px solid black;
  height: 100%;
}
</style>
<div class="progress-bar">
  Pages complete: {{done}}/{{total}} ({{percent}}%)
  <div style="width: {{percent}}%"></div>
</div>

{%- assign todo-pages = site.pages | where_exp: "p", "p.mediawiki != nil" | sort: "url" -%}
{%- assign depth = 1 %}
<div class="todo-list">
<ul>
<h3>/</h3>
{%- assign bucket = '' -%}
{% for p in todo-pages %}
{%- capture this-bucket -%} {%- include util/dir path=p.url -%} {%- endcapture -%}
{%- if bucket == this-bucket -%}
  {%- comment -%} Same directory -- carry on! {%- endcomment -%}
{%- else -%}
  {%- assign bucket = this-bucket -%}
  </ul>
  <ul>
  <h3>{{bucket}}</h3>
{%- endif -%}
<li><a href="{{p.url | replace: "/index", ""}}">{{p.title}}</a></li>
{% endfor %}
</ul>
</div>
