---
mediawiki: ImageJ2_Python_Scripts
title: ImageJ2 Python Scripts
---

# Introduction

This page is a primer of **ImageJ2 only** Python scripts. It means that the examples included here avoid IJ1 as much as possible, unless it's really necessary.

Note that all the scripts of this page are links from
{% include github org="imagej" repo="imagej-scripting" branch="master"
                  path="src/main/resources/script_templates/ImageJ2"
                  label="this GitHub repository" %}.

# Scripts

## Stack Projection

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Projection.py' %}

## Apply Threshold

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Apply_Threshold.py' %}

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Apply_Threshold_Fast.py' %}

## Crop an image

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Crop.py' %}

## Rotate all the frames of a stack

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Rotate_Stack.py' %}

## Subtract a stack to its first image

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Subtract_First_Image_Stack.py' %}

## Apply DOG Filter

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Apply_DOG_Filtering.py' %}

## Apply a mask

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Apply_Mask.py' %}

## Retrieve objects/particles from a mask

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Particles_From_Mask.py' %}

## Manual Simple Registration on Stack

{% include code org='imagej' repo='imagej-scripting' branch='master' path='src/main/resources/script_templates/ImageJ2/Manual_Registration.py' %}

# Resources

- [Jython Scripting](/scripting/jython)
- [Jython Examples](/scripting/jython/examples)
