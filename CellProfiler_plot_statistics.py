#!/usr/bin/env python

#
# Last modified: 25 Jul 2017 (edited by Ceylin to make it more user friendly)
# Author: Dhananjay Bhaskar <dbhaskar92@gmail.com>
# 
import re
import sys
import numpy as NP
import matplotlib.pyplot as PLT

if (len(sys.argv) != 2):
	print '\nMake sure to include the right csv file, see usage below...\n'
	print 'Usage: /usr/bin/python2 CellProfiler_plot_statistics.py /path/to/AllMyExpt_Image.csv'
	sys.exit()

data = NP.genfromtxt(sys.argv[1], delimiter=',', skip_header=1, skip_footer=0, usecols=(1,24,48,49,50,51), names=['cell_count','f_num','lost_obj','merged_obj','new_obj','split_obj'])

xlim = int(raw_input('Enter number of frames: '))
channel = (raw_input('Green/Red?: '))
#ylim = int(raw_input('Enter approximate number of cells: '))

totalframes = len(data['f_num'])
# Lost frames due to lamp 
lostframes = 0
for num_cells in data['cell_count']:
	if num_cells == 0:
		lostframes = lostframes + 1
remaining_frames = totalframes - lostframes
caption = "Total frames: "+`totalframes`+" Lost frames: "+`lostframes`+" Remaining frames: "+`remaining_frames`

if channel == 'Red':

	PLT.figure(1)
	PLT.title('Cell Count')
	PLT.plot(data['f_num'], data['cell_count'], color='r', linestyle='-')
	PLT.xlabel('Frame Number')
	PLT.ylabel('Number of Cells')
	#PLT.text(5,10,caption)
	axes = PLT.gca()
	#axes.set_ylim([100, ylim])
	axes.set_xlim([0, xlim])
	PLT.savefig('CellProfiler_red_cellcount')

elif channel == 'Green':
	PLT.figure(1)
	PLT.title('Cell Count')
	PLT.plot(data['f_num'], data['cell_count'], color='g', linestyle='-')
	PLT.xlabel('Frame Number')
	PLT.ylabel('Number of Cells')
	#PLT.text(5,10,caption)
	axes = PLT.gca()
	#axes.set_ylim([100, ylim])
	axes.set_xlim([0, xlim])
	PLT.savefig('CellProfiler_green_cellcount')


PLT.figure(2)
PLT.title('CellProfiler Statistics')
line1, = PLT.plot(data['f_num'], data['lost_obj'], color='r', linestyle='-', label='Lost Objects')
line2, = PLT.plot(data['f_num'], data['merged_obj'], color='g', linestyle='-', label='Merged Objects')
line3, = PLT.plot(data['f_num'], data['split_obj'], color='b', linestyle='-', label='Split Objects')
PLT.legend([line1, line2, line3], ['Lost Objects', 'Merged Objects', 'Split Objects'])
PLT.legend(loc="upper left")
PLT.xlabel('Frame Number')
PLT.ylabel('Object Count')
axes = PLT.gca()
axes.set_xlim([0, xlim])
#axes.set_ylim([-5, ylim])
PLT.savefig('CellProfiler_plot2.png')
