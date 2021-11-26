---
title: Labkit - How To Segment A Large Image On An HPC Cluster
---

# Labkit - How To Segment A Large Image On An HPC Cluster

High performance computing (HPC) cluster are helpful to process large images that do not fit on consumer computers at very high speed. In order to use Labkit to segment a very large image on an HPC cluster, we need to train a classifier on a small subimage and run the [Labkit command tool line](https://github.com/maarzt/labkit-command-line) on the cluster.

On the local computer:

1.  Download the dataset of interest, unzip
2.  Use [BigStitcher](/bigstitcher/index) FIJI plugin to convert the dataset to BDV HDF5 + XML format:
    - Install BigStitcher [update site](/update-sites/following) in Fiji
    - Run Plugins > BigStitcher > Batch Processing > Define dataset …
      (Use Bioformats importer and make sure to select the correct pixel size)
3.  Open the image in Labkit using:
    Plugins > Lakit > Open Image File With Labkit
4.  Continue as described in the [quick automatic segmentation]()
5.  Save the trained classifier {% include bc path="Segmentation | Save Classifier ..." %}

On the HPC cluster:

{:start="6"}

6.  Copy the dataset HDF5 + XML to the cluster
7.  Copy the trained classifier to the cluster
8.  Download the [Labkit command line tool](https://github.com/maarzt/labkit-command-line/releases/download/v0.1.1/labkit-snakemake-exmaple-0.1.1.zip)
9.  Unzip the command line tool archive
10.  Edit the “Snakemake” file and change the following lines:

```sh
IMAGE = “/path/to/your/dataset.xml”
CLASSIFIER = “/path/to/your/pixel.classifier”
USE_GPU = ”true”
```

{:start="11"}

11. Run the snakemake script:

```sh
$ snakemake --cluster=”sbatch --partition=gpu” --jobs=10 --local-cores=1 --restart-times=10
```

