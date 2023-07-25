~~~markdown
[![Build Status](https://github.com/trackmate-sc/TrackMate-Cellpose/actions/workflows/build.yml/badge.svg)](https://github.com/trackmate-sc/TrackMate-Cellpose/actions/workflows/build.yml)

# Omnipose integration in TrackMate.

The Omnipose integration in TrackMate works roughly as the Cellpose integration one. 
It requires Omnipose to be installed on your system and working independently. This page gives installation details and advices at how to use the omnipose integration in TrackMate.

## Omnipose
Omnipose is a segmentation algorithm based on Deep-Learning techniques, and inspired from the Cellpose architecture. Omnipose is well suited for bacterial cell segmentation, and achieves remarkable performances on mixed bacterial cultures, antibiotic-treated cells and cells of elongated or branched morphology.

If you use the Omnipose TrackMate module for your research, please also cite the Omnipose paper:
[Cutler, K.J., Stringer, C., Lo, T.W. et al. Omnipose: a high-precision morphology-independent solution for bacterial cell segmentation. Nat Methods 19, 1438–1448 (2022)](https://www.nature.com/articles/s41592-022-01639-4).



## Example
https://github.com/marieanselmet/TrackMate-Omnipose/assets/32811540/3c2365c9-8d1b-4057-b4d1-2939e4e2b818

*E. Coli, Marie Anselmet and Rodrigo Arias Cartin, Barras lab, Institut Pasteur*


## Omnipose installation

This code works with the Omnipose version 0.3.6. It doesn't work with the last version of Omnipose.

To install Omnipose, you can refer directly to the installation guide provided on the [Omnipose repository](https://github.com/kevinjohncutler/omnipose#how-to-install-omnipose).

An example Windows installation working on GPU:
```
conda create -n omnipose
conda activate omnipose
conda install pytorch==2.0.0 torchvision==0.15.0 torchaudio==2.0.0 pytorch-cuda=11.8 -c pytorch -c nvidia
pip install omnipose==0.3.6
pip install cellpose-omni==0.7.3
```

The default models *bact_phase_omni* and *bact_fluor_omni* are stored in the cellpose pretrained models folder.
~~~