#!/usr/bin/env Python
# Name: Joseph Olivier
PROTEINDICT = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L", "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S", "UAU":"Y", "UGC":"C",
    "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L", "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "UGG":"W",
    "CAA":"Q", "CAG":"Q", "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M", "UAA":"",
    "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K", "AGU":"S", "AGC":"S", "UAG":"",
    "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V", "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "UGA":"",
    "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E", "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G", "UAC":"Y", "UGU":"C"}
amount = ""
dict1 = {}
for key in PROTEINDICT:
	amount += PROTEINDICT[key]
	for c in amount:
		dict1[c] = amount.count(c)
with open("rosalind_mrna.txt", "r") as f:
	seq = f.read().upper().strip()

def possibilityCounter(seq):
	total = 3
	for char in seq:
		total *= dict1[char] 
		total = total % 1000000
	return total
print(dict1)
print(possibilityCounter(seq))

