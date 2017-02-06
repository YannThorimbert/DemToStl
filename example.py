"""Example of usage for converting DEM to STL.
The DEM example used here is volcano_dem_10m.txt.
In this example we use numpy to load the data from DEM file, but one could
give write_stl function any array of its own.
#-------------------------------------------------------------------------------
# Name:        example.py
#
# Author:      Yann Thorimbert
#
# Created:     06.02.2017
#-------------------------------------------------------------------------------
"""
from __future__ import print_function, division

import numpy as np
import stlwriter

input_file = "volcano_dem_10m.txt"

hmap = np.loadtxt(input_file)
hmap[hmap<0] = 0 #the input file contains values lower than 0; we dont want them

#attention : this is a bit low, since the DEM is quite large.
stlwriter.write_stl(hmap, "output.stl", dh=0.1, dx=1.)
#now you can visualize the stl with any program
