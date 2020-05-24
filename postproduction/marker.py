import os
import datetime as dt
from string import Template
import sys

directory = "./pics"

cmdTemplate = Template("magick convert $file -pointsize 32 -background Orange label:$timeStamp +swap -gravity Center -append $outputFileName")

def markImage(index, timeStamp, fileName):
	outputFileName = "./pics/marked-" + str(index) +".png"
	fileName = "./pics/" + fileName
	cmd = cmdTemplate.substitute(file=fileName, timeStamp=timeStamp, outputFileName=outputFileName)
	print(cmd)
	os.system(cmd)

def getTimeStamp(fileName):
	parts = fileName.split("-")
	lastPart = parts[-1]
	split = lastPart.split(".")
	timeStampString = split[0]
	timeStamp = dt.datetime.strptime(timeStampString, '%Y%m%d%H%M%S')
	formatted = timeStamp.isoformat()
	return formatted

def walkFiles(path):
	# sort the files according to creation timestamp
	for index, filename in enumerate(sorted(os.listdir(path))):
		if filename.endswith(".png"): 
			print(filename)
			timeStamp = getTimeStamp(filename)
			print(timeStamp)
			markImage(index, timeStamp, filename)
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