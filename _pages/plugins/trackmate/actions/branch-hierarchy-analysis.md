---
title: Branch hierarchy analysis
categories: [Hierarchical analysis]
description: Decomposition and analyse of the tracks in successives branches
artifact: sc.fiji:TrackMate
---

`Branch hierarchy analysis` decomposes each track in branches and output a summary table of analysis.
For each branch, it computes statistics as the duration of the branch, the number of sucessors, of predecessors..
For instance, if a track is composed of one cell that divide at time t, 3 branches will be created, one of the mother cell until time t, and 2 branches (its sucessors) of the daughter cells after time t.
{% include img src='/media/plugins/trackmate/actions/Icons4_print_transparency.png' align='left'  %}

## Usage
Once the tracking is done, move to the last panel of the main TrackMate window, called **Actions**, by clicking on the `Next` button.
The branch hierarchy analysis action can be found in the list. 
After selecting, click the `Execute` button.
A new window should appear.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_action.png'  align='left' %}

TrackMate decomposes all the tracks in branchs and give the results in a table that will appear in a new window.

The rows of the table can be sorted by a column value by clicking on the corresponding column.
For example, click on `Label` to sort the results by tracks.
You can export the results as a csv file directly.
The `Branch table` that pops up is synchronized with the active selection in TrackMate. If you click on a branch (a row of the table), it will select the targetted branch in the other TrackMate windows opened.

{% include img src='/media/plugins/trackmate/actions/branch_analysis_selection.png'  align='left' %}
