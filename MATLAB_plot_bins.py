#!/usr/bin/env python

#
# Last modified: Jul 25 2017 (edited by Ceylin to make it more user friendly)
# Author: Dhananjay Bhaskar <dbhaskar92@gmail.com>
#

import re
import sys
import collections
import numpy as NP
import matplotlib.pyplot as PLT

if (len(sys.argv) != 3):
	print '\nMake sure to include both the Green and the Red csv files, see usage below...\n'
	print 'Usage: python MATLAB_plot_bins.py /path/to/Green.csv /path/to/Red.csv'
	sys.exit()

GFP_data = NP.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, skip_footer=0, usecols=(0, 2, 3), names=['Frame', 'CentroidX', 'CentroidY'])

mCherry_data = NP.genfromtxt(sys.argv[2], delimiter=',', skip_header=1, skip_footer=0, usecols=(0, 2, 3), names=['Frame', 'CentroidX', 'CentroidY'])

xlim = int(raw_input('Enter max x limit: '))
ylim = int(raw_input('Enter max y limit: '))

bin1_green = collections.defaultdict(list)
bin2_green = collections.defaultdict(list)
bin3_green = collections.defaultdict(list)
bin4_green = collections.defaultdict(list)
bin5_green = collections.defaultdict(list)
bin6_green = collections.defaultdict(list)
bin7_green = collections.defaultdict(list)
bin8_green = collections.defaultdict(list)

for i in range(0, len(GFP_data)):

	frame = int(GFP_data['Frame'][i])
	green_X = int(GFP_data['CentroidX'][i])
	
	if frame not in bin1_green.keys():
		bin1_green[frame] = 0
	if frame not in bin2_green.keys():
		bin2_green[frame] = 0
	if frame not in bin3_green.keys():
		bin3_green[frame] = 0
	if frame not in bin4_green.keys():
		bin4_green[frame] = 0
	if frame not in bin5_green.keys():
		bin5_green[frame] = 0
	if frame not in bin6_green.keys():
		bin6_green[frame] = 0
	if frame not in bin7_green.keys():
		bin7_green[frame] = 0
	if frame not in bin8_green.keys():
		bin8_green[frame] = 0	
	
	if green_X <= 200:
		bin1_green[frame] = bin1_green[frame] + 1
			
	elif (green_X > 200 and green_X <= 400):
		bin2_green[frame] = bin2_green[frame] + 1
	
	elif (green_X > 400 and green_X <= 600):
		bin3_green[frame] = bin3_green[frame] + 1
	
	elif (green_X > 600 and green_X <= 800):
		bin4_green[frame] = bin4_green[frame] + 1
		
	elif (green_X > 800 and green_X <= 1000):
		bin5_green[frame] = bin5_green[frame] + 1
		
	elif (green_X > 1000 and green_X <= 1200):
		bin6_green[frame] = bin6_green[frame] + 1
		
	elif (green_X > 1200 and green_X <= 1400):
		bin7_green[frame] = bin7_green[frame] + 1
		
	elif (green_X > 1400 and green_X <= 1600):
		bin8_green[frame] = bin8_green[frame] + 1
	
	else:
		print "Warning! Out of bounds."
		
frames_g = bin1_green.keys()
frames_g.sort()

bin1_red = collections.defaultdict(list)
bin2_red = collections.defaultdict(list)
bin3_red = collections.defaultdict(list)
bin4_red = collections.defaultdict(list)
bin5_red = collections.defaultdict(list)
bin6_red = collections.defaultdict(list)
bin7_red = collections.defaultdict(list)
bin8_red = collections.defaultdict(list)

for i in range(0, len(mCherry_data)):

	frame = int(mCherry_data['Frame'][i])
	red_X = int(mCherry_data['CentroidX'][i])
	
	if frame not in bin1_red.keys():
		bin1_red[frame] = 0
	if frame not in bin2_red.keys():
		bin2_red[frame] = 0
	if frame not in bin3_red.keys():
		bin3_red[frame] = 0
	if frame not in bin4_red.keys():
		bin4_red[frame] = 0
	if frame not in bin5_red.keys():
		bin5_red[frame] = 0	
	if frame not in bin5_red.keys():
		bin5_red[frame] = 0	
	if frame not in bin6_red.keys():
		bin6_red[frame] = 0	
	if frame not in bin7_red.keys():
		bin7_red[frame] = 0	
	if frame not in bin8_red.keys():
		bin8_red[frame] = 0		
	
	if red_X <= 200:
		bin1_red[frame] = bin1_red[frame] + 1
			
	elif (red_X > 200 and red_X <= 400):
		bin2_red[frame] = bin2_red[frame] + 1
	
	elif (red_X > 400 and red_X <= 600):
		bin3_red[frame] = bin3_red[frame] + 1
	
	elif (red_X > 600 and red_X <= 800):
		bin4_red[frame] = bin4_red[frame] + 1
		
	elif (red_X > 800 and red_X <= 1000):
		bin5_red[frame] = bin5_red[frame] + 1
		
	elif (red_X > 1000 and red_X <= 1200):
		bin6_red[frame] = bin6_red[frame] + 1
		
	elif (red_X > 1200 and red_X <= 1400):
		bin7_red[frame] = bin7_red[frame] + 1
		
	elif (red_X > 1400 and red_X <= 1600):
		bin8_red[frame] = bin8_red[frame] + 1
	
	else:
		print "Warning! Out of bounds."
		
frames_r = bin1_red.keys()
frames_r.sort()


fig, axarr = PLT.subplots(2, 2)
axarr[0, 0].plot(frames_g, [bin1_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[0, 0].plot(frames_r, [bin1_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[0, 0].set_title('0um < Bin 1 <= 80um')
axarr[0, 0].set_xlim([0,xlim])
axarr[0, 0].set_ylim([0,ylim])
axarr[0, 1].plot(frames_g, [bin2_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[0, 1].plot(frames_r, [bin2_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[0, 1].set_title('80um < Bin 2 <= 160um')
axarr[0, 1].set_xlim([0,xlim])
axarr[0, 1].set_ylim([0,ylim])
axarr[1, 0].plot(frames_g, [bin3_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[1, 0].plot(frames_r, [bin3_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[1, 0].set_title('160um < Bin 3 <= 240um')
axarr[1, 0].set_xlim([0,xlim])
axarr[1, 0].set_ylim([0,ylim])
axarr[1, 1].plot(frames_g, [bin4_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[1, 1].plot(frames_r, [bin4_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[1, 1].set_title('240um < Bin 4 <= 320um')
axarr[1, 1].set_xlim([0,xlim])
axarr[1, 1].set_ylim([0,ylim])
PLT.savefig('MATLAB_Bins_1.png', dpi=120)

fig, axarr = PLT.subplots(2, 2)
axarr[0, 0].plot(frames_g, [bin5_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[0, 0].plot(frames_r, [bin5_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[0, 0].set_title('320um < Bin 5 <= 400um')
axarr[0, 0].set_xlim([0,xlim])
axarr[0, 0].set_ylim([0,ylim])
axarr[0, 1].plot(frames_g, [bin6_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[0, 1].plot(frames_r, [bin6_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[0, 1].set_title('400um < Bin 6 <= 480um')
axarr[0, 1].set_xlim([0,xlim])
axarr[0, 1].set_ylim([0,ylim])
axarr[1, 0].plot(frames_g, [bin7_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[1, 0].plot(frames_r, [bin7_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[1, 0].set_title('480um < Bin 7 <= 560um')
axarr[1, 0].set_xlim([0,xlim])
axarr[1, 0].set_ylim([0,ylim])
axarr[1, 1].plot(frames_g, [bin8_green[t] for t in frames_g], color='g', marker='None', linestyle='-')
axarr[1, 1].plot(frames_r, [bin8_red[t] for t in frames_r], color='r', marker='None', linestyle='-')
axarr[1, 1].set_title('560um < Bin 8 <= 640um')
axarr[1, 1].set_xlim([0,xlim])
axarr[1, 1].set_ylim([0,ylim])
PLT.savefig('MATLAB_Bins_2.png', dpi=120)
