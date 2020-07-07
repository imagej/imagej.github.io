import os
import re

from ij_mw_preprocess import *

path_in = "/home/edward/Documents/Workspaces/imagej-net-conversion/imagej_mediawiki_source/3D_Viewer.mw"
path_out = "/home/edward/Documents/Development/Repos/LOCI/imagej.github.io/pages/3D_Viewer.md"
file_contents = read_file(path_in)
output = process_file(path_in, file_contents)
write_file(output, path_out)
run_pandoc(path_in, path_out)
