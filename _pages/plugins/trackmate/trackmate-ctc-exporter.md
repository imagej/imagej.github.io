title: Export tracking results in the cell tracking challenge format
categories: [Segmentation,Tracking,Benchmark]
logo: /media/logos/trackmate-300p.png
description: Export a TrackMate results to the Cell-Tracking-Challenge file format
artifact: sc.fiji:TrackMate

# Export tracking results in the cell tracking challenge format.

The cell tracking challenge (CTC) aims to compare and evaluate cells and nuclei tracking methods objectively. To perform the evaluation, both segmentation and tracks predicted by a tracking algorithm are compared to manually annotated ground truth. Authors of the CTC developed several evaluation metrics to score the tracking quality and a tool to compute them. More information about the CTC is available on their [<span class="underline">website</span>](http://celltrackingchallenge.net/) and publication:

> *Ulman, V., Maška, M., Magnusson, K. et al. An objective comparison of cell-tracking algorithms. Nat Methods 14, 1141--1152 (2017). https://doi.org/10.1038/nmeth.4473*

TrackMate now allows users to export their tracking session into the CTC format to compute evaluation metrics (see tutorial below). The TrackMate helper also uses the CTC metrics to identify the best possible tracking parameters to use; more information about the TrackMate helper is available here.

## Export tracks in CTC format

-   After a successful tracking session (automated tracking / manual tracking)
-   In the action panel, select **Export to CTC format** and click **Execute**.

{% include img 
src="/media/plugins/trackmate/trackmate-ctc-exporter-01.png" 
align="center"
width='400'  %}

-   A new window will open where you can select where to save your files and the data type.

    -   Select **Gold truth** if your tracking results were generated manually (human-made reference annotations, also called ground truths).

    -   Select **Silver truth** if a computer algorithm generated the tracking results and you manually corrected them.

    -   Select **Results** if a computer algorithm generated your tracking results.
-   Then, click **OK**.

{% include img 
src="/media/plugins/trackmate/actions/trackmate-ctc-exporter-02.png" 
align="center"
width='800'  %}

-   Ground truths will be saved in a CTC format in your selected location. There will be two folders 01 and 01GT (if exported as Gold truth). The 01 folder contains the original data frame by frame. The GT01 folder contains two subfolders, **SEG** and **TRA**:

    -   The **SEG folder** contains reference segmentation for each corresponding original image. In the case of gold segmentation truth, manual segmentation needs to be is provided from selected frames (segmentation of each time frame is not necessary). In the case of silver segmentation truth, every frame is usually annotated, for example, by the Stardist segmentation integrated into Trackmate.
    -   The **TRA folder** contains:
    
        -   A text file representing an acyclic graph for the whole video. Every row corresponds to a single track. Each track (row) is encoded by four numbers: Column 1 (L - label) - a unique label of the track (label of markers, 16-bit positive value). Column 2 (B - begins) - a zero-based temporal index of the frame in which the track starts. Column 3 (E - ends) is a zero-based temporal index of the frame where the track ends. Columns 4 (P - parent) - label of the parent track (0 is used when no parent is defined)
    -   Reference tracking annotations consist of cell markers interlinked between frames to form cell lineage trees. These are used to evaluate the detection and tracking performance of competing methods.

{% include img 
src="/media/plugins/trackmate/trackmate-ctc-exporter-03.png" 
align="center"
width='800'  %}

