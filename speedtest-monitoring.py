#!/usr/bin/env python

import os, re, datetime

speedtestCliFile = 'speedtest.py'
speedtestParameters = ''

speedtest = os.popen("python " + speedtestCliFile + " " + speedtestParameters).read()

downloadOutput = False
uploadOutput = False
writeOutput = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

download = re.search('Download: (.*?) ', speedtest)
if download:
	downloadOutput = ";" + download.group(1)

upload = re.search('Upload: (.*?) ', speedtest)
if upload:
	uploadOutput = ";" + upload.group(1)

if downloadOutput:
	writeOutput = writeOutput + downloadOutput

if uploadOutput:
	writeOutput = writeOutput + uploadOutput

with open('output.csv', 'a+') as file:
	file.write(writeOutput + '\n')
