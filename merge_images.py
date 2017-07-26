#!/usr/bin/env python

#
# Last modified: 17 Jun 2017
# 
#

import re
import sys
import collections
import os
import numpy as NP
from optparse import OptionParser
from PIL import Image, ImageMath

# Options parsing
usage = '%prog options\n  > at least one file (-r/-g) must be specified\n  > exactly one radius parameter (-m/-p)' \
        ' must be specified\n  > time (-t) must be specified\n  > all other options are not required'
parser = OptionParser(usage=usage)
parser.add_option('-g', type='string', dest='green', help='green images path format')
parser.add_option('-r', type='string', dest='red', help='red images path format')
parser.add_option('-d', type='int', dest='digits', help='number of digits in file name')
(options, args) = parser.parse_args()

print "Merging images..."

if not options.green or not options.red:
    sys.exit('Formats (-g,-r) and are required arguments. Use -h for usage help.')
if options.green:
    green = options.green.split(',')
if options.red:
    red = options.red.split(',')
digits = 3
if options.digits:
    digits = int(options.digits)

os.makedirs('Merged')

def merge(path0, path1, name):
	image0 = Image.open(path0)
	image1 = Image.open(path1)

	r0, g0, b0 = image0.split()[0], image0.split()[1], image0.split()[2]
	r1, g1, b1 = image1.split()[0], image1.split()[1], image1.split()[2]

	r, g, b = ImageMath.eval('convert(max(a, b), "L")', a=r0, b=r1), \
              ImageMath.eval('convert(max(a, b), "L")', a=g0, b=g1), \
              ImageMath.eval('convert(max(a, b), "L")', a=b0, b=b1)

	image = Image.merge('RGB', (r, g, b))
	image.save(name)

counter = 0
def pad(number):
	return ('{:0' + str(digits) + 'd}').format(number)

while not os.path.isfile(green[0] + pad(counter) + green[1]):
	counter += 1

while os.path.isfile(green[0] + pad(counter) + green[1]) and os.path.isfile(red[0] + pad(counter) + red[1]):
	merge(green[0] + pad(counter) + green[1], red[0] + pad(counter) + red[1], 'Merged/Merged_' + pad(counter) + '.png')
	counter += 1


