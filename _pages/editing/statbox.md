---
title: Vital Statistics Sidebar
section: Contribute:Editing the Wiki
nav-title: Statbox
nav-links: true
---

The "Vital Statistics" sidebar (statbox) is a dynamic component that displays metadata about software components or people. It appears on the right side of wiki pages when relevant fields are provided in the page's YAML front matter.

## Overview

The statbox operates in two modes:

1. **Manual mode**: You specify metadata fields manually in the page front matter
2. **Automatic mode**: The statbox scrapes information from Maven repositories using JavaScript

The two modes can be combined: the automatic population only fills empty fields, which allows manual overrides as needed.

## Basic Usage

To enable the statbox, add at least one supported field to your page's YAML front matter:

```yaml
---
title: My Component
name: My Component Name
icon: /media/icons/my-component.png
source-url: https://github.com/myorg/my-component
---
```

## Supported Fields

### General Fields

| Field | Description | Example |
|-------|-------------|---------|
| `icon` | URL of the image icon to show in the statbox header | `/media/icons/fiji.png` |
| `name` | Name of the component or person | `"Fiji"` |
| `affiliation` | Organizational affiliation | `"Fiji University"` |
| `website` | Primary website link | `https://fiji.sc/` |

### Component-Specific Fields

| Field | Description | Example |
|-------|-------------|---------|
| `artifact` | Maven groupId:artifactId for automatic population | `sc.fiji:fiji` |
| `repository` | Maven repository URL (defaults to maven.scijava.org) | `https://repo1.maven.org/maven2` |
| `pom-url` | Direct URL to a POM file for automatic population | `https://raw.githubusercontent.com/imagej/imagej2/main/pom.xml` |
| `source-url` | Source code repository URL | `https://github.com/imagej/imagej2` |
| `source-label` | Custom label for source link (auto-detected if not provided) | `"on GitHub"` |
| `license-url` | License details URL | `/licensing/bsd` |
| `license-label` | License name/label | `"BSD-2"` |
| `release-url` | Latest release URL | `https://github.com/fiji/fiji/releases/latest` |
| `release-version` | Latest release version | `"2.14.0"` |
| `release-date` | Latest release date | `"2023-07-07"` |
| `dev-status` | Development status | `"Active"`, `"Stable"`, `"Unstable"`, `"Obsolete"` |
| `support-status` | Support level | `"Active"`, `"Partial"`, `"Minimal"`, `"None"` |
| `forum-tag` | Image.sc forum tag | `"fiji"` |

### Team Fields

Team fields support multiple people in various formats:

| Field | Description |
|-------|-------------|
| `team-founders` | Project creators |
| `team-leads` | Decision makers |
| `team-developers` | Feature developers |
| `team-debuggers` | Bug fixers |
| `team-maintainers` | Release managers |
| `team-reviewers` | Code reviewers |
| `team-support` | Community support |
| `team-contributors` | Code contributors |

### Person-Specific Fields

| Field | Description | Example |
|-------|-------------|---------|
| `gravatar` | Gravatar hash for profile image | `"abc123def456..."` |
| `forum` | Image.sc Forum username | `"username"` |
| `github` | GitHub username | `"username"` |
| `stackoverflow` | Stack Overflow user ID | `"12345"` |
| `openhub` | Open Hub username | `"username"` |
| `twitter` | Twitter username | `"username"` |
| `linkedin` | LinkedIn profile path | `"in/username"` |
| `researchgate` | ResearchGate profile | `"Username_Name"` |
| `loop` | Loop Research Network ID | `"12345"` |
| `orcid` | ORCID identifier | `"0000-0000-0000-0000"` |
| `researcherid` | ResearcherID | `"A-1234-2023"` |
| `scopus` | Scopus Author ID | `"12345678900"` |
| `arxiv` | arXiv author identifier | `"smith_j_1"` |
| `scholar` | Google Scholar ID | `"AbCdEfGhIjK"` |
| `honorific` | Special community title | `"Grand Poobah"` |

## Advanced Features

### Automatic Population

The most powerful feature is automatic metadata population from Maven artifacts:

```yaml
---
title: Fiji
artifact: sc.fiji:fiji
---
```

This will automatically populate:
- Component name
- Source repository link
- License information  
- Latest release version and URL
- Release date
- Team information from POM
- Development and support status

### Multi-part URL Statistics

Several fields have URL/label pairs for better control over display text:

```yaml
---
release-url: https://github.com/imagej/imagej2/releases/tag/v2.14.0
release-version: "2.14.0"
license-url: /licensing/bsd
license-label: "BSD-2"
---
```

### Source URL Auto-detection

The `source-url` field automatically generates appropriate labels based on the domain:

- `github.com` → "on GitHub"
- `gitlab.com` → "on GitLab" 
- `bitbucket.org` → "on BitBucket"
- `sourceforge.net` → "on SourceForge"
- Other URLs → "online"

### Team Member Formats

Team fields accept comma-separated lists with three supported formats:

1. **Wiki people reference**: `@ctrueden` (looks up `/people/ctrueden`)
2. **Name with custom link**: `John Doe | https://johndoe.com`
3. **Plain name**: `Jane Smith`

Example:
```yaml
team-leads: '@ctrueden, Curtis Rueden | /people/curtis-rueden'
team-developers: '@ctrueden, @hinerm, Jane Smith'
```

### Affiliation Links

The `affiliation` field supports the `Name | URL` format:

```yaml
affiliation: 
  - 'University of Wisconsin-Madison | https://wisc.edu'
  - 'Morgridge Institute for Research | https://morgridge.org'
```

## Examples

### Manual Component Example

```yaml
---
title: Fiji
name: Fiji
icon: /media/icons/fiji.png
website: https://fiji.sc
source-url: https://github.com/fiji/fiji
license-url: /licensing/gpl
license-label: GPLv3
release-version: "2.14.0"
release-date: "2023-06-01"
dev-status: Active
support-status: Active
team-leads: '@ctrueden'
team-developers: '@ctrueden, @hinerm'
forum-tag: fiji
---
```

### Automatic Component Example

```yaml
---
title: ImgLib2
artifact: net.imglib2:imglib2
---
```

### Person Example

```yaml
---
title: Curtis Rueden
name: Curtis Rueden
gravatar: abc123def456
affiliation: 'University of Wisconsin-Madison | https://wisc.edu'
website: https://ctrue.name
github: ctrueden
forum: ctrueden
orcid: 0000-0001-7055-6707
scholar: VqJdqBEAAAAJ
honorific: Fiji Maintainer
---
```

## Implementation Details

The statbox is implemented in `_includes/layout/statbox` using Liquid templating and enhanced with JavaScript from `assets/js/maven.js` for automatic population features. When `artifact` or `pom-url` is specified, the JavaScript automatically fetches and parses Maven metadata to populate empty fields.

The automatic metadata population logic works best for components using [Maven](/development/maven) as their project management/build tool, and which extend the [pom-scijava parent](https://github.com/scijava/pom-scijava) for build configuration and dependency version management, because pom-scijava [enforces the presence of all the needed metadata](https://github.com/scijava/pom-scijava-base?tab=readme-ov-file#enforcer-rules-declared-in-this-parent). See [here](https://github.com/fiji/fiji/blob/fiji-2.14.0/pom.xml#L16-L178) for an example of how populated metadata might look in your project's `pom.xml` file.

The refresh button (⟲) allows users to reload the automatic data, useful when new releases are available.
