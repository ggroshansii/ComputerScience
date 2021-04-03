#!/usr/bin/env python3
fileName1 =  open("/home/gh0st/Documents/transcript.txt", "r")

strippedSentences = []

for line in fileName1.readlines():
    strippedSentences.append(line.rstrip())


fileName2 = open("/home/gh0st/Documents/transcript.txt", "w")

for i in strippedSentences:
    fileName2.write(i + " ")


fileName3 = open("/home/gh0st/Documents/transcript.txt", "r")

for line in fileName3:
    print(line)