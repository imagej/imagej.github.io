---
title: TrackMate-Oneat
description: Trackcorrector that uses oneat's prediction to correct lineage trees
categories: [Tracking]
logo: /media/logos/trackmate-oneat.png
---

# TrackMate-Oneat

This page describes a track corrector module for TrackMate that relies on [oneat](https://pypi.org/project/oneat/). It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following) called **TrackMate-Oneat**.

## Usage.

## Tutorial: *Xenopus nuclei* early development.
In this video I compare the tracking results using LAP tracker of TrackMate and SimpleLap tracker + oneat correction. 
[LAP tracker comparision with SimpleLAP Tracker + oneat correction](https://youtu.be/9HZvWxr2fsY)

## Tracking Metrics

## Simple LAP tracker + Oneat

{DET : 0.9964,    CT : 0.73531,   TRA : 0.9933,    TF : 0.97518,  BCi : 0.10526}

## LAP Tracker with track splitting and Quality as additional cost

{DET : 0.9900,    CT : 0.677033,   TRA :	0.986785;  TF : 0.95041,  BCi :	0.04347}

## LAP Tracker with track splitting and Quality as additional cost + Oneat

{DET : 0.98911,    CT :	0.672629,    TRA : 0.985774,   TF :	0.948692,   BCi : 0.05555}

## LAP Tracker without track splitting and Quality as additional cost + Oneat
{DET : 0.990083,   CT :	0.6766,      TRA : 0.986742, TF : 0.9521, BCi	0.054}

### The dataset.

### Obtaining oneat predictions.

### Running TrackMate.

### Starting the TrackMate-Oneat action.







Varun Kapoor - May 2022
{% include warning/stub %}
