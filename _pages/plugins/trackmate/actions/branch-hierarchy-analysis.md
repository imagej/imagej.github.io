---
title: Branch hierarchy analysis
categories: [Track analysis]
description: Decomposition and analysis of tracks in successives branches.
artifact: sc.fiji:TrackMate
---

`Branch hierarchy analysis` decomposes each track in branches and output a summary table of analysis.
For each branch, it computes statistics as the duration of the branch, the number of sucessors, of predecessors..

{% include img src='/media/plugins/trackmate/actions/Icons4_print_transparency.png' align='center'  %}

For instance, if a track is composed of one cell that divide at time t, 3 branches will be created, one of the mother cell until time t, and 2 branches (its sucessors) of the daughter cells after time t.


## Usage
Once the tracking is done, move to the last panel of the main TrackMate window, called **Actions**, by clicking on the `Next` button.
The branch hierarchy analysis action can be found in the list. 
After selecting, click the `Execute` button.
A new window should appear.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_action.png'  align='center' width='200px' %}

TrackMate decomposes all the tracks in branchs and give the results in a table that will appear in the new window.
The list of the columns and their significations is given in the section [Analysis of a branch](#analysis-of-a-branch) below.

The rows of the table can be sorted by a column value by clicking on the corresponding column.
For example, click on `Label` to sort the results by tracks.
You can export the results as a csv file directly.
The `Branch table` that pops up is synchronized with the active selection in TrackMate. If you click on a branch (a row of the table), it will select the targetted branch in the other TrackMate windows opened.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_selection.png'  align='center' %}


## Definition of a branch

A branch is a portion of a track, in which all spots except for the first and last one have exactly one predecessor and one succesor spot in time.
In other words, it is a portion of a track between divisions/splits or fusions/merges.
A branch can be composed of one spot only or more.

In the example below, Track 0 has 4 branches and Track 1 has 6 branches, circled with dashed lines.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_tracks.png'  align='center' width='400px' %}

### Definition of predecessors and succesors
A branch is limited by its first and last spot, but can be linked to other branch(s).

**Predecessors** of a branch are branchs which last spot is linked to the first spot of the branch, and temporally prior to this spot.

**Successors** of a branch are branchs which first spot is linked to the last spot of the branch, and temporally placed after this spot.

For example, if we consider the branch circled in red in the image below, its first spot is the spot `ID2007` and its last is `ID2019`. The branch has one predecessor: the branch finishing with the spot `ID2003` and one sucessor: the branch that begin with the spot `ID2021`. For all branches, the first spot are colored in lighter color, and last spot in a darker one.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_trackshierarchy.png'  align='center' width='400px' %}


## Analysis of a branch
`Branch hierarchy analysis` measures several features for each branch. Below is the output of branch analysis on the previous example.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_branchtable.png'  align='center' width='600px' %}

The proposed measures are:

- *Label*: the name of the track from which the branch is extracted, followed by the IDs of the first and last spot of the branch. The branch is composed of all the spots that are in between these 2 spots in the hierarchy.

- *Track ID*: identification number of the track from which the branch is extracted in TrackMate.

- *N predecessors*: number of predecessors of the branch. It will be more than 1 if the branch comes from a fusion/merge event.

- *N successors*: number of successors of the branch. It will be more than 1 if the branch comes from a division/split event.

- *Delta T*: temporal duration of the branch. It corresponds to the time between the first and the last spot of the branch. If the movie is calibrated, the time calculated will be calibrated too. These values are given in separate columns.

- *Dist*: total distance travelled in the branch. It is the sum of the distances between each consecutive points in the branch.

- *Mean V*: average velocity of the point in the branch.

- *First ID*: identification number of the first point of the branch.

- *Last ID*: identification number of the last point of the branch.

- *Succ. delay*: average time between the last spot of the branch and its successors (the first point of successor branchs). There can be several successors, in general positionned at the same time point (e.g. daughter cells) but in some situation, the successors could start at different time point, so the average is given.

- *Pred delay*: average time between the first spot of the branch and its predecessors (the last point of predecessors branchs). There can be several predecessors, positionned at different time points. The average temporal distance with its predecessors is given.

