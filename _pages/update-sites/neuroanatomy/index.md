---
name: "Neuroanatomy update site"
title: Neuroanatomy update site
categories: [Analysis, Neuroanatomy]
project: /software/fiji
dev-status: "Active"
team-founder: "@tferr"
team-maintainer: "@tferr"
source-url: https://github.com/morphonets
---

The *Neuroanatomy update site* is [Fiji](/software/fiji)'s [update site](/update-sites) for the distribution of [SNT](/plugins/snt) and related plugins.

# Subscribing to the Neuroanatomy update site

1.  Run [{% include bc path='Help|Update...'%}](/update-sites)
2.  Click {% include button label="Manage update sites" %}
3.  Select the *Neuroanatomy* checkbox (see also [list of update sites](/list-of-update-sites))
4.  Click {% include button label="Apply changes" %}
5.  Restart ImageJ


# Installed Commands

## Main ImageJ Window

| Command                                                                  | Description |
|--------------------------------------------------------------------------|-------------|
| Neuroanatomy Shortcuts Tool                                              | A ImageJ macro tool (SNT icon, installed next to the ">> More Tools" switch) to toggle the visibility of the Neuroanatomy Shortcut Window  |
| {% include bc path='Plugins|Neuroanatomy|Neuroanatomy Shortcut Window'%} | A centralized hub to access all neuroanatomy commands, including [SNT](/plugins/snt), [Sholl](/plugins/sholl-analysis), [Strahler](/plugins/strahler-analysis), demos, and [scripts](/snt/scripting) |
| {% include bc path='Plugins|Neuroanatomy|Reconstruction Plotter...'%}    | Starts [Reconstruction Plotter](/plugins/snt/reconstruction-plotter) |
| {% include bc path='Plugins|Neuroanatomy|Reconstruction Viewer'%}        | Starts [Reconstruction Viewer](/plugins/snt/reconstruction-viewer) |
| {% include bc path='Plugins|Neuroanatomy|SNT...'%}                       | Starts [SNT](/plugins/snt) |
| {% include bc path='Plugins|Neuroanatomy|Sholl|'%}                       | Starts [Sholl analyses](/plugins/sholl-analysis) without running SNT |
| {% include bc path='Analyze|Skeleton|Summarize Skeleton'%}               | Bulk statistics of skeletonized images |
| {% include bc path='Analyze|Skeleton|Classify Particles Using Skeleton'%}| Tags particles according to skeleton features. Detects maxima on a masked image and clusters detected maxima using features of the skeletonized mask. A maxima is considered to be associated to a skeleton feature (e.g., a junction or end-point, see <a href="/plugins/analyze-skeleton">AnalyzeSkeleton</a>) if the distance between its centroid and the feature is less than or equal to a cutoff ("snap to") distance |
| {% include bc path='File|Open Samples|Fractal Tree'%} | Synthetic image (<a href="https://en.wikipedia.org/wiki/L-system">L-System</a> Tree) useful for debugging, testing or prototyping |
| {% include bc path='File|Open Samples|ddaC Neuron'%} | Binary image (2D) of a Drosophila class IV ddaC sensory neuron in which dendrites have been segmented. Useful for debugging, testing or prototyping. Run {% include bc path='Image|Show Info...'%} to know more about this cell type |

## Script Editor

| Command                                        | Description                         |
|------------------------------------------------|-------------------------------------|
| {% include bc path='Templates|Neuroanatomy|'%} | Demo scripts exemplifying SNT usage |


# Further information

A list of all ImageJ extensions related to the neurosciences can be found on the [list of extensions](/list-of-extensions) page, by filtering to the Neuroanatomy category.
