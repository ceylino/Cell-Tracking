#!/usr/bin/env python

#
# Last modified: 22 Jun 2017
# Author: Ceylin Ozdemir
#

import re
import sys
import collections
import numpy as NP
import matplotlib.pyplot as PLT

if (len(sys.argv) != 3):
    print 'Usage: python Matlab_cell_count.py /path/to/Green.csv /path/to/Red.csv'
    sys.exit()


green_channel = NP.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, skip_footer=0, usecols=(24, 1), names=['Frame', 'CellID'])

red_channel = NP.genfromtxt(sys.argv[2], delimiter=',', skip_header=1, skip_footer=0, usecols=(24, 1), names=['Frame', 'CellID'])


# Get Green Channel Frames and CIDs
data_g = dict(zip(green_channel['Frame'], green_channel['CellID']))

#for key in data:
#   print "key: %s , value: %s" % (key, data[key])

frames_g = []
cids_g = []

for key in data_g:
    frames_g.append(int(key))
    cids_g.append(int(data_g[key]))


#Get Red Channel Frames and CIDs
data_r = dict(zip(red_channel['Frame'], red_channel['CellID']))

frames_r = []
cids_r = []

for key in data_r:
    frames_r.append(int(key))
    cids_r.append(int(data_r[key]))


#Plot data on a graph

PLT.figure()
PLT.title('Cell Count')
PLT.xlabel('Frame Number')
PLT.ylabel('Number of Cells')
PLT.plot(frames_g, cids_g, color='g', linestyle='-')
PLT.plot(frames_r, cids_r, color='r', linestyle='-')
PLT.xlim([0,550])
PLT.ylim([20, 300])
PLT.savefig('Matlab_cell_count.png')







