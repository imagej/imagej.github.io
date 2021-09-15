---
title: Labkit tutorials

---

# Tutorials

## General

### Automatic segmentation (quick demo)

Follow these steps to segment an image:

1.  Open an image in ImageJ.
2.  Start Labkit by selecting {% include bc path="Plugins | Segmentation | Labkit" %} from the menu.
3.  Labkit should start and display the image. If it shows a black window instead of the image: Click {% include key key='S' %} and adjust the contrast.
4.  Select "foreground" (In the side bar of Labkit). Select the pencil tool (top bar of Labkit) and draw on the image.
5.  Select "background" and the pencil tool, and mark some other region of the image as background.
6.  In the side bar of Labkit, under the heading "Segmentation" you will find an entry "Classifier \#1". And next to it there is a play button (black triangle). Click it, to train the Classifier. After a moment you will see the automatic segmentation of your image.
7.  From Labkit's main menu select {% include bc path="Segmentation | Show Segmentation Result in ImageJ" %}, to export your segmentation into ImageJ.

As video:
![labkit-quick-start](https://user-images.githubusercontent.com/24407711/133519201-67d6e29f-f024-4803-8eee-75831a996952.gif)

### Manual segmentation

1.  Start Fiji, open your image, start Labkit (`Plugins > Labkit > Open Current Image With Labkit`)
2.  Select `+ Add label`
3.  Use the `Draw` button (pencil icon) to mark the contour around any one object instance
4.  Use the `Flood Fill` button (bucket icon) to fill inside this contour
5.  When all objects have been labeled in the manner above, select `Labeling > Save Labeling`

<img src="https://user-images.githubusercontent.com/34229641/106534470-6b4df100-64f4-11eb-8c76-600a33de669a.gif"  width="800" />



### Curating automated segmentation results

### Curating segmentation obtained by other software

1. Convert the segmentation results to a single file per label, of dimensions equal to those of the raw image
2. Load the raw image in Labkit
3. Load the bitmap semgentation as labels by using the menu Labeling > Import bitmap
4. Use the drawing tools to curate the labels
5. Save the labels as image or export them to Fiji

## Advanced tutorials

### Use Labkit With GPU acceleration

Labkit can use NVIDIA graphics cards to speed up calculation and segment images faster. The speed difference is significant but will vary from machine to machine. In order to perform GPU-accelerated segmentation, follow these steps:

1. Install [CLIJ2 in Fiji](https://clij.github.io/clij2-docs/installationInFiji)
2. In Labkit, after selecting a classifier, open the "Classifier Settings" and select "Use GPU acceleration".

### Segment a list of images with a macro

Automatic image segmentation can be used to segment a large number of images. Beforehand, make sure of the following:

- Images must be similar in order to get reproducible results
- Brightness and contrast must be normalized across images
- (Optional) background removal can improve results
- Select a representative image

Open the representative image with Labkit and segment the image as described in the [quick automatic segmentation](). Save the trained classifier {% include bc path="Segmentation | Save Classifier ..." %} into a file. Finally, you can use the following ImageJ macro to automatically segment images with the trained classifier.

```java
// ImageJ macro for segmenting a list of images
folder = "C:/path/to/folder/"
for (i = 0; i < 10; i++) {
   open(folder + "image_" + i + ".tif");
   run("Segment Image With Labkit", "segmenter_file=" + folder + "my_pretrained_classifier.classifier use_gpu=false");
   saveAs("Tiff", folder + "segmentation_" + i + ".tif");
   close();
   close();
}
```

### Segment a large image on an HPC cluster

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

1. Run the snakemake script:

```sh
$ snakemake --cluster=”sbatch --partition=gpu” --jobs=10 --local-cores=1 --restart-times=10
```

