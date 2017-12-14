'''How to open an image in ImageJ2?'''

The answer to this question depends on how you use ImageJ.
* Do you want the open an image using the graphical user interface? ([[#From the GUI]])
* Are you writing a script? ([[#From a Script]])
* Are you using Java, to develop an ImageJ2 plug-in or do write your one program using ImgLib2 and ImageJ libraries? ([[#From Java]])

== From the GUI ==

In the menu select "File > Open ..." or "File > Import > ...".

== From a Script ==

What are then possible ways to open an image when you are writing an Python / Groovy / ... script in ImageJ?

=== Use a parameter of type Dataset ===

When the following script is run in ImageJ.
ImageJ will ask to user to select two Images, before it runs the script.

<source lang="python">
# @Dataset firstImage
# @Dataset secondImage
# @UIService ui
ui.show(firstImage)
ui.show(secondImage)
</source>

=== Use the DatasetIOService ===

<source lang="python">
# @DatasetIOService io
# @UIService ui
path = "C:\Path\to\the\image.tif"
image = io.open(path)
ui.show(image)
</source>

== From Java ==
