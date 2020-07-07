import os
from ij_mw_preprocess import *

# TODO actually implement mass conversion

path_in = "/home/random/Development/imagej/imagej/imagej-net-temp/3D_Viewer.mw"
path_out = "/home/random/Development/imagej/imagej/imagej.github.io/pages/3D_Viewer.md"
run_pandoc(path_in, path_out)
