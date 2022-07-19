---
title: TrackMate-ExTrack
categories: [Tracking]
description: Export a TrackMate results to the Cell-Tracking-Challenge file format
artifact: fr.pasteur.iah:TrackMate-ExTrack
---

# TrackMate-ExTrack: diffusion and binding kinetics in live cells.

TrackMate-ExTrack is a [TrackMate](/plugins/trackmate/index) action that contains a port of the Python analysis tool ExTrack to Java and TrackMate.
The paper that describes the science behin dthis tool is here:

{% include citation doi='10.1101/2022.07.13.499913' %}

Please cite it if ExTrack is useful for your research.

The Python version of ExTrack, which should be considered the nominal and prime source, can be found [on its GitHub repo](https://github.com/vanteeffelenlab/extrack).
This page solely documents the TrackMate port.

## ExTrack analysis.

ExTrack performs track analysis and can determine whether a particle is undergoing diffusive motion or is bound and appear as stuck.
Importantly, ExTrack can resolve the transitions from one state to another for a single particle. 
It is built to be robust against noisy trajectories and offers an excellent accuracy even when facing large localization inaccuracies.
Check the article for the details on how ExTrack works.

## Installation.

TrackMate-ExTrack is shipped as an optional ImageJ  [update site](/update-sites/following).
Just go to the Fiji updater and in the list of update site, check the **TrackMate-ExTrack** update site and restart Fiji.

{% include img src='/media/plugins/trackmate/actions/trackmate-extrack-01.png' align='center'  %}

## Usage.

ExTrack performs analysis of exising tracks, so you need to either use TrackMate to generate them or import them.
The TrackMate-ExTrack analysis is an action and is launched via the last panel in the TrackMate UI:

{% include img src='/media/plugins/trackmate/actions/trackmate-extrack-02.png' align='center'  %}

Select this action and click on the `Execute` button.
The TrackMate-ExTrack UI window is shown:

{% include img src='/media/plugins/trackmate/actions/trackmate-extrack-03.png' align='center'  %}

## Short tutorial.

It is best explaining how ExTrack works with a short tutorial on synthetic data.
Francois prepared 100 synthetic particles switching between diffusive  and bound states and arranged them on a 10x10 grid. 
Then he saved the corresponding tracks as a TrackMate fle. 
You can get the TrackMate file (and more) on Zenodo:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.6862839.svg)](https://doi.org/10.5281/zenodo.6862839)

