---
title: Miniature Faking
categories: [Filtering,Interactive,Integral Image,Photography]
---

This is an interactive non-scientific fun plugin to {% include wikipedia title='Miniature faking' text='fake miniature photographs'%} from existing images. The plugin fakes an effect that can be achieved optically by {% include wikipedia title='Tilt-shift' text='tilting'%} the projection plane behind the lens in a camera. It uses {% include wikipedia title='Summed area table' text='Integral Images'%} to smooth the image with a variant smoothing kernel whose size increases in proportion with its distance to the 'tilt axis'. The 'tilt axis' is a line where the images remains maximally sharp. The location and orientation of the 'tilt axis' and the intensity of the effect can be adjusted using the line tool which is activated by the plugin by default. The plugin is not (yet) in the menus but can be executed from the [Javascript/ Jython/ Beanshell terminal](/scripting) using:

    new mpicbg.ij.integral.InteractiveTilt().run("");

{%- include img src='mpi-cbg' -%} People sitting in the MPI-CBG cafeteria.
{%- include img src='street' -%} A crossroad in NYC.
{%- include img src='dc' -%} A view over DC.
{%- include img src='car' -%} Some cars in front of a restaurant.
{%- include img src='traveler' -%} A traveler in the mountains.
{%- include img src='wood' -%} Landscape.
