import os
import datetime as dt
from string import Template
import sys

cmdTemplate = Template("magick convert $file -pointsize 32 -background Orange label:\"$timeStamp\" +swap -gravity Center -append $outputFileName")

sourceTimeFormat = '%Y%m%d%H%M%S'
targetTimeFormat = '%d %B %Y - %H:%M:%S'
def markImage(directory, index, timeStamp, fileName):
	outputFileName = directory + "/marked-" + str(index) +".png"
	fileName = directory + "/" + fileName
	cmd = cmdTemplate.substitute(file=fileName, timeStamp=timeStamp, outputFileName=outputFileName)
	print(cmd)
	os.system(cmd)

def getTimeStamp(fileName):
	parts = fileName.split("-")
	lastPart = parts[-1]
	split = lastPart.split(".")
	timeStampString = split[0]

	timeStamp = dt.datetime.strptime(timeStampString, sourceTimeFormat)
	#formatted = timeStamp.isoformat()
	formatted = timeStamp.strftime(targetTimeFormat)
	return formatted

def walkFiles(path):
	# sort the files according to creation timestamp
	for index, filename in enumerate(sorted(os.listdir(path))):
		if filename.endswith(".png"): 
			print(filename)
			timeStamp = getTimeStamp(filename)
			print(timeStamp)
			markImage(path, index, timeStamp, filename)
			continue
		else:
			continue

def start():
	if (len(sys.argv) != 2): 
		print("Please provide the directory path of the images")
		sys.exit()
	path = sys.argv[1]
	walkFiles(path)

start()