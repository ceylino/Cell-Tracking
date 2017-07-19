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

if (len(sys.argv) != 3):
	print 'Usage: python NumberofNeighbours.py /path/to/cell_degrees.csv'
	sys.exit()

red_red = NP.genfromtxt(sys.argv[1], delimeter=',', skip_header=1, skip_foooter=0, usecols=(), names=['Frame', 'Red'])
green_green = NP.genfromtxt(sys.argv[2], delimeter=',', skip_header=1, skip_foooter=0, usecols=(), names=['Frame', 'Green'])
red_green = NP.genfromtxt(sys.argv[3], delimeter=',', skip_header=1, skip_foooter=0, usecols=(), names=['Frame', 'Red-Green'])

#Get number of Red-Red neighbours and frame numbers
data_rr = dict(zip(red_red['Frame'], red_red['Red']))

frames_rr = []
neighbours_rr = []

for key in data_rr:
	frames_rr.append(int(key))
	neighbours_rr.append(int(data_rr[key]))

#Get number of Green-Green neighbours and frame numbers
data_gg = dict(zip(green_green['Frame'], green_green['Green']))

frames_gg = []
neighbours_gg = []

for key in data_gg:
	frames_gg.append(int(key))
	neighbours_gg.append(int(data_gg[key]))

#Get number of Green-Green neighbours and frame numbers
data_rg = dict(zip(red_green['Frame'], red_green['Red-Green']))

frames_rg = []
neighbours_rg = []

for key in data_rg:
	frames_rg.append(int(key))
	neighbours_rg.append(int(data_rg[key]))


#Plot data on a graph
PLT.figure()
PLT.title('Types of Neighbours')
PLT.xlabel('Frame Number')
PLT.xlabel('Number of Neighbours')
PLT.plot(frames_rr, neighbours_rr, color='r', linestyle='-', label='Red-Red')
PLT.plot(frames_gg, neighbours_gg, color='g', linestyle='-', label='Green-Green')
PLT.plot(frames_rg, neighbours_rg, color='b', linestyle='-', label='Red-Green')
PLT.xlim([0,400])
PLT.ylim([0,10])
PLT.savefig('CellProfiler_neighbours_stats')
