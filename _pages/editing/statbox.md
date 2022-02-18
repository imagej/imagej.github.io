---
title: Vital Statistics Sidebar
section: Contribute:Editing the Wiki
nav-title: Statbox
nav-links: true
---

This page explains how the "Vital statistics" sidebar works.

The sidebar supports quite a few fields; see [this comment](https://github.com/imagej/imagej.github.io/blob/main/_includes/layout/statbox#L31-L75) for a list. Including at least one of these fields will cause the statbox to appear; otherwise, there will be no statbox for the page.

## Tips

### Multi-part URL statistics

Several URL-type stats have multiple related keys (e.g. `release-url` and `release-version`). This is to give you control over displayed text in the limited space of the Vital Statistics box. Note that entering a URL alone is typically insufficient to display: you must also enter a corresponding label.

### Keys with Special Values

All statbox front matter supports plain-text `key:value` pairs, but several key types have additional value parsing options.

#### Affiliation

* **Name \| link** - Displays the given name with a custom link. This can be absolute (`Google | https://google.com`) or relative (`Google | /people/google`)

#### Team members

All of the `team-` sections (e.g. `team-leads`, `team-developers`) accept comma-separated (`,`) lists of one or more individual(s). Each person can be in one of three formats, and the formats can be mixed and matched:

* **@person** - Looks up the person as an id in the [people directory](/people). Note that the `@` can appear anywhere in the id, but can not be the very first character of a value - which can be solved by putting the value in quotes, i.e. `'@ctrueden, @hinerm'`
* **Name \| link** - Displays the given name with a custom link. See also [Affiliation](#affiliation).
