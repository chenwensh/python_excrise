#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import tushare as ts
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

#Scatter
def show_scratter():
	x = np.linspace(-np.pi, np.pi, 256)
	y = np.cos(x)
	plt.scatter(x, y, marker = '.', color = 'blue')
	#set the x_start, x_end, y_start, y_end.
	#plt.axis([0, 10, 0, 10])
	plt.show()

#Line
def show_line():
	x = list(range(1,11))
	y = list(np.cos(y) for y in x)
	plt.plot(x, y, linestyle = '--', label = 'picture')
	plt.show()

#Plot line of stock shanghai
def show_shstock_line():
	df = ts.get_hist_data('sh', start = '2016-01-01')
	df.to_excel('stock_sh.xlsx')
	df.close.plot()
	ax = plt.gca()
	ax.invert_xaxis()
	plt.show()

#Show multiple figures in one picture
def show_multiple_figures():
	fig = plt.figure()

	x = list(range(10, 90))
	y = list(np.sin(y) for y in x)

	p1 = fig.add_subplot(211)
	p1.plot(x, y)

	p2 = fig.add_subplot(212)
	p2.scatter(x, list(np.sin(y + np.random.randn()) for y in x))

	plt.show()

#Show two types figures in single picture
def show_two_in_single():
	x = np.linspace(0, 10, 1000)
	y = np.sin(x)
	z = np.cos(x**2)

	plt.figure(figsize = (8, 4))
	plt.plot(x, y, label = '$sin(x)$', color = "red", linewidth = 2)
	plt.plot(x, z, "b--", label = "$cos(x^2)$")
	plt.xlabel("Time(s)")
	plt.ylabel("Volt")
	plt.title('PyPlot First Example')
	plt.ylim(-1.2, 1.2)
	plt.legend()
	plt.show()

#3D
def show_3D():
	fig = plt.figure()
	ax = fig.add_subplot(111, projection = '3d')

	x = [1, 1, 2, 2]
	y = [3, 4, 4, 3]
	z = [1, 100, 1, 1]

	ax.plot_trisurf(x, y, z)
	plt.show()

if __name__ == "__main__":
	#show_line()
	show_scratter()
	#show_shstock_line()
	#show_multiple_figures()
	#show_two_in_single()
	#show_3D()

