#!/bin/bash

dir="./pics/*.png"

for file in $dir
do
	echo $file
	timeStamp=$(echo $file | cut -d "-" -f3 | cut -d "." -f1)
	# filePath without fileEnding
	filePath=$(echo $file | cut -d "." -f2 )
	fileName=".${filePath}-marked.png"
	magick convert $file -pointsize 32 -background Orange label:$timeStamp +swap -gravity Center -append $fileName
done