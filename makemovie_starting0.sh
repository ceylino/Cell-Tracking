#!/bin/bash
#
# Last modified on: 20 Jul 2017
# Author: Ceylin Ozdemir

# Movie Making Script

# Usage
if [ "$#" -ne 3 ]; then
	echo -e "Make sure to include 3 arguments, see usage below...\n"
	echo -e "Usage: ./makemovie.sh ImageNameUntiltheFirstFrameNumber ImageNameAftertheThirdDigitofFrameNumber OutputName\n"
	echo -e "ie. For image name OutlineCells_000.png\n  ./makemovie.sh OutlineCells_ .png outlinecells\n"
	#echo -e "ie. For image name Track_050.png\n  ./makemovie.sh 50 Track_ .png tracked_cells.mp4"
	exit 1
fi

# Calculate length of movie
FRAMESPERSEC="10"

CNT="0"
for f in *.png; do
	((CNT++))
done

LENGTH=$((CNT/FRAMESPERSEC))

# Make movie
echo "Number of Frames: $CNT"
echo -e "Estimated Length: $LENGTH seconds\n"
echo "Creating a movie..."

Name_Part_1=$1
Name_Part_2=$2
Output=$3


avconv -framerate 10 -loglevel quiet -i "${Name_Part_1}%03d${Name_Part_2}" -s:v 1920x1080 -b:v 8640k -c:v libx264 -profile:v high -crf 20 -pix_fmt yuv420p ${Output}.mp4