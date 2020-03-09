#!/usr/bin/env python
# -*- coding:utf-8 

#This programe is to exercise the children who are interest in algorithm.
#Author: Theo Chen    Date:2020/3/8

#Factorial is a method which can calculate the factorial.For example:6*5*4*3*2*1
def factorial():
	n = int(input("Please input the number you want:"))
	x = 1
	for i in range (1, n+1):
		x = x * i

	print("The factorial of %d is %d"%(n, x))

#e.g for n = 10, the result should be: 10+9+8+7+6+5+4+3+2+1
def plus():
	m = int(input("Please input the number you want:"))
	h = 0
	for j in range(1, m + 1):
		h = h + j
	print("The plus of %d is %d."%(m, h))

def prime_number():
	p = int(input("Please input the  number you want:"))
	for i in range(1, p+1):
		flag = True
		for j in range(2, i):
			if i % j == 0:
				flag = False
				break
		if flag == True:
			print(i)

def pertutations(arr, position, end):
	if position == end:
		print(arr)
	else:
		for index in range(position, end):
			arr[index], arr[position] = arr[position], arr[index]
			pertutations(arr, position + 1, end)
			arr[index], arr[position] = arr[position], arr[index]

if __name__ == "__main__":
	print("Welcome to the algorithm! world!I hope you can enjoy it!")
	'''Call factorial.'''
	#factorial()
	#plus()
	#prime_number()
	
	arr = ['1', '2', '3']
	pertutations(arr, 0, len(arr))
