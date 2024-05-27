---
title: TrackMate-Oneat
description: Trackcorrector that uses oneat's prediction to correct lineage trees
categories: [Tracking]
icon: /media/icons/mtrack.png
---
<img src="/media/icons/mtrack.png" alt="Logo1" width="150"/>
<img src="/media/icons/kapoorlablogo.png" alt="Logo2" width="150"/>

This product is a testament to our expertise at KapoorLabs, where we specialize in creating cutting-edge solutions. We offer bespoke pipeline development services, transforming your developmental biology questions into publishable figures with our advanced computer vision and AI tools. Leverage our expertise and resources to achieve end-to-end solutions that make your research stand out.

**Note:** The tools and pipelines showcased here represent only a fraction of what we can achieve. For tailored and comprehensive solutions beyond what was done in the referenced publication, engage with us directly. Our team is ready to provide the expertise and custom development you need to take your research to the next level. Visit us at [KapoorLabs](https://www.kapoorlabs.org/).


This page describes a track corrector module for TrackMate that relies on [oneat](https://pypi.org/project/oneat/). It is not included in the core of TrackMate and must be installed via its own [update site](/update-sites/following) called **TrackMate-Oneat**.

## Usage

### Obtaining oneat predictions

TrackMate-oneat replies on oneat which is a Keras based action classification library that provides multi-class trained model for doing static and action classification. The output of the network consists of a csv file of cell locations (XYT) that can be visualized using a customized Napari widget that can be found [here](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/Wikioneat/Notebooks/Visualize_seg_with_action_classification_napari.ipynb)). We provide certain [demo notebooks](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/tree/Wikioneat/Demo) where pre-trained models are automatically downloaded along with a test dataset to show the prediction of oneat networks for mitotic cell events.
To use this action you have to create a trained model of oneat for your dataset. This requires training a multi class action classification model as is described 
[here](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/-/Notebooks/Segmentation_free_dynamic_training_data_creator.ipynb). You can use this notebook to create [annotations](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/-/Notebooks/Training_data_maker.ipynb). After creating the data you can use this [notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/Wikioneat/Notebooks/Segmentation_free_dynamic_training_data_creator.ipynb) to train your own network. Once your network is trained you would have obtained the model h5 and json files that can be used in conjugation with the segmentation image for your dataset to get the locations of mitotic/apoptotic/ other cell event that the network was trained on using this [notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/Wikioneat/Notebooks/Visualize_seg_with_action_classification_napari.ipynb). If you do not have segmentation image for your dataset use this [notebook](https://github.com/Kapoorlabs-CAPED/CAPED-AI-oneat/blob/Wikioneat/Notebooks/Visualize_seg_free_action_classification_napari.ipynb) to obtain the location of the cell event of interest. For oneat we currently use the location of mitotic and cell death events to correc tthe lineage trees. To avoid overdetection of the same cell event over time please use this notebook to obtain a "clean" csv file of cell event locations where we perform score based non maximal supression over time. This "clean" csv file serves as input to the TrackMate-Oneat extension post tracking is performed. 

### Starting the TrackMate-Oneat action

As is outlined in the video tutorial, we have to first finish the tracking process using Simple LAP tracker for example to obtain the tracks, then once we reach the last panel of TrackMate we can use the TrackMate-Oneat action by pressing the execute button and loading the "clean" csv file to start the process to track correction. The users additionally have the choice of specifying a veto over the score threshold of the detected events along with a parameter delta T, that checks if TrackMate found mitosis event matches with the oneat found mitosis event for that track. If you also have a trained model for cell death that can also be uploaded to terminate such tracks. Track correction can be done by creating new links and/or by breaking current mitotic cell event links if they do not match with the oneat detected cell locations for mitosis. When using Simple LAP tracker only new links can be created as that algorithm does not support linking segments for mitosis events. If you have chosen LAP tracker with segment splitting option, you can break the mitosis links found by TrackMate if no oneat detection is found for such cells under consideration.

## Algorithm

The algorithm for oneat is described figuratively [here](https://github.com/kapoorlab/imagej.github.io/blob/-/media/plugins/trackmate/actions/TrackMate-oneat-algorithm.jpg).
Essentially in this scheme we describe the breaking and creating new linking process. If users chooses LAP tracker with segment splitting then we check for mitosis events, in this step we match the locations of mitotic cells with that of oneat detected location, if a match is found the track is not marked for re-linking else the mitotic cell link is broken and is marked for re-linking. If the user has also uploaded a file that contains cell death locations then such tracks are terminated at the found location. If the user on the other hand chooses Simple LAP tracker then the check for mitosis is skipped as that algorithm doe snot support segment to segment linking. In the next step the segments are re-linked based on our local segment linker step. In this step we create a local graph which contains the edge between the mother cell and its source cell to be linked with edges in the local neighborhood of daughter cells. We constrain this process of linking by enforcing that the size of the daughter cells to be less than that of the mother cell and  also the difference in the Z slices of the mother and daughter cell links. One such an assingment is determines using Jaqman Segment linker algorithm we break those links in the main graph and create new links based on the assingements determined. This leads to a new graph/trackschem with new TrackId's being generated.


## Tutorial: *Xenopus nuclei* early development

In this video I compare the tracking results using LAP tracker of TrackMate and SimpleLap tracker + oneat correction. 
[LAP tracker comparision with SimpleLAP Tracker + oneat correction](https://youtu.be/9HZvWxr2fsY) The dataset used can be found [here](https://zenodo.org/record/6591369#.YpOTwXZBy3A) along with the ground truth tracks. We used different combinations of TrackMate tracking algorithms and oneat and after converting the tracks to ctc compatiable formats obtianed the following tracking metrics which show that combination of SimpleLAP tracker with Oneat is most appropriate for this particular example to obtain highest tracking accurate results.

## Tracking Metrics

### Simple LAP tracker + Oneat

{DET : 0.9964,    CT : 0.73531,   TRA : 0.9933,    TF : 0.97518,  BCi : 0.10526}

### LAP Tracker with track splitting and Quality as additional cost

{DET : 0.9900,    CT : 0.677033,   TRA :	0.986785;  TF : 0.95041,  BCi :	0.04347}

### LAP Tracker with track splitting and Quality as additional cost + Oneat

{DET : 0.98911,    CT :	0.672629,    TRA : 0.985774,   TF :	0.948692,   BCi : 0.05555}

### LAP Tracker without track splitting and Quality as additional cost + Oneat
{DET : 0.990083,   CT :	0.6766,      TRA : 0.986742, TF : 0.9521, BCi	0.054}







Varun Kapoor - May 2022

