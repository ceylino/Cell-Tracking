#!/usr/bin/env python

#
# Last modified: 18 Jul 2017
#Author: Ceylin Ozdemir
#

import re
import sys
import collections
import numpy as NP
import matplotlib.pyplot as PLT

if (len(sys.argv) != 2):
	print 'Usage: python NumberofNeighbours.py /path/to/cell_degrees.csv'
	sys.exit()

params = NP.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, skip_footer=0, usecols=(0, 3, 4, 5), names=['Frame', 'Green', 'Red', 'RG'])


#Plot data on a graph
PLT.figure()
PLT.title('Types of Neighbours')
PLT.xlabel('Frame Number')
PLT.ylabel('Number of Neighbours')
PLT.plot(params['Red'], color='r', linestyle='-', label='Red-Red')
PLT.plot(params['Green'], color='g', linestyle='-', label='Green-Green')
PLT.plot(params['RG'], color='b', linestyle='-', label='Red-Green')
PLT.xlim([0,400])
PLT.ylim([0,3000])
PLT.legend(loc="upper left")
PLT.savefig('Neighbours_notnormalized')
