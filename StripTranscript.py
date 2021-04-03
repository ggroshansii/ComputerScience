#!/usr/bin/env python3
fileName = open("/home/gh0st/Documents/transcript.txt", "w+")

for line in fileName.readlines():
    fileName.write(line.rstrip())

for line in fileName:
    print(line)