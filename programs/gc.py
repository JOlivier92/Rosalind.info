#!/usr/bin/env Python
# Name: Joseph Olivier
dict1 = {}
headerline = []
sequence = []
with open('sampleinput.txt','r') as file:
	seq = file.read().upper()
for line in file:
	if line.startswith(">") in file:
		headerline = line
print(headerline)
#print(max(dict1, key=dict1.get))
#print(max(dict1, key=lambda key: dict1[key])