#!/usr/bin/env python3
# Name: Joseph Olivier
# Program: Fibonacci Numbers
# Hyperlink http://rosalind.info/problems/fibo/

def FibonacciGenerator(n):
	if n == 0:
		Fn = 0
	elif n == 1:
		Fn = 1
	else:
		Fn = FibonacciGenerator(n-1)+FibonacciGenerator(n-2)

	return Fn

def main():
	import sys
	for line in sys.stdin:
		fibNum = int(line.strip())
	print(FibonacciGenerator(fibNum))

main()