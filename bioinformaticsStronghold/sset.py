#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Counting Subsets
# Hyperlink http://rosalind.info/problems/sset/
# What a satisfying problem! Did it without built-in function for practice.

def combinatorialCalculator(n):
	numberofSubSets = 1
	nfactorial = 1
	for i in range(1,n+1):
		nfactorial *= i

	for k in range(1,n+1):
		if k == 1:
			numberofSubSets+=n
			continue
		if k == n:
			numberofSubSets+=1
			continue
		numberofSubSets += nfactorial/findFactorial(k,n-k)

	return int(numberofSubSets % 1000000)

def findFactorial(k,nMinusk):
	kfactorial = 1
	nMinuskfactorial = 1
	for i in range(1,min(k,nMinusk)+1):
		kfactorial *= i
		nMinuskfactorial *= i
	
	if k != nMinusk:
		for i in range(min(k,nMinusk)+1,max(k,nMinusk)+1):
			if k > nMinusk:
				kfactorial*=i
			else:
				nMinuskfactorial*=i
	return kfactorial*nMinuskfactorial



def main():
	import sys
	n = int(sys.stdin.readline())
	numberofSubSets = combinatorialCalculator(n)
	print(numberofSubSets)


main()
