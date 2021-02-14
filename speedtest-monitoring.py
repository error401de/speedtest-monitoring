#!/usr/bin/env python

import os, re, datetime

speedtestCliFile = 'speedtest.py'
speedtestParameters = ''

path = os.path.dirname(os.path.abspath(__file__)) + "/"
speedtest = os.popen("python " + path + speedtestCliFile + " " + speedtestParameters).read()

downloadOutput = False
uploadOutput = False
writeOutput = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

download = re.search('Download: (.*?) ', speedtest)
if download:
	downloadOutput = ";" + download.group(1)
	writeOutput = writeOutput + downloadOutput

upload = re.search('Upload: (.*?) ', speedtest)
if upload:
	uploadOutput = ";" + upload.group(1)
	writeOutput = writeOutput + uploadOutput

with open(path + 'output.csv', 'a+') as file:
	file.write(writeOutput + '\n')
