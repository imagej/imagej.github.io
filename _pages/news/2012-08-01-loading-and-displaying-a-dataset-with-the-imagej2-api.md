---
mediawiki: 2012-08-01_-_Loading_and_displaying_a_dataset_with_the_ImageJ2_API
title: 2012-08-01 - Loading and displaying a dataset with the ImageJ2 API
---

Recently, someone [someone asked on the mailing list](/ij/pipermail/imagej-devel/2012-July/001117.html) how to load and display a dataset using the [ImageJ2](/software/imagej2) API. Here is code that does so:

    import imagej.ImageJ;
    import imagej.data.Dataset;
    import imagej.display.DisplayService;
    import imagej.io.IOService;

    import java.io.File;

    public class DisplayDataset {

        public static void main(final String[] args) throws Exception {
            final ImageJ context = ImageJ.createContext();

            final File file = new File("/path/to/data-file.tif");

            // load the dataset
            final IOService ioService = context.getService(IOService.class);
            final Dataset dataset = ioService.loadDataset(file.getAbsolutePath());

            // display the dataset
            final DisplayService displayService =
                context.getService(DisplayService.class);
            displayService.createDisplay(file.getName(), dataset);
        }

    }

We have {% include github org='imagej' repo='tutorials' branch='master' path='maven-projects/load-and-display-dataset/src/main/java/LoadAndDisplayDataset.java' label='published this code as an ImageJ tutorial' %}.

For this to work, you will need to add compile-time dependencies to `ij-core`, `ij-data` and `ij-io`, as well as a runtime dependency to your user interface of choice (e.g., `ij-ui-swing`). If you don't add the UI JAR dependency, nothing will be displayed, because ImageJ2 won't know how to do it! See the {% include github org='imagej' repo='tutorials' branch='master' path='maven-projects/load-and-display-dataset/pom.xml' label='tutorial code"s pom.xml' %} for details.

Note that as of this writing, there is a bug with the Swing SDI user interface (and maybe other UIs) that causes the display to initially appear white. Hit minus (-) and then plus (+), which will zoom out then back in, to force the image window to repack and redraw.

 
