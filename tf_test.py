#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import tensorflow as tf
import numpy as np

def mode1():
	# Create the input data
	x_data = np.random.rand(100).astype(np.float32)
	y_data = x_data * 0.1 + 0.3

	# Create the tensorflow structure
	Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
	biases = tf.Variable(tf.zeros([1]))

	y = x_data * Weights + biases
	
	# Define the loss,optimizer and the train of the optimizer.	
	loss = tf.reduce_mean(tf.square(y - y_data))
	optimizer = tf.train.GradientDescentOptimizer(0.5)
	train = optimizer.minimize(loss)

	# init = tf.initialize_all_variables()
	sess = tf.Session()
	
	init = tf.global_variables_initializer()
	sess.run(init)

	for step in range(201):
		sess.run(train)
		if step % 20 == 0:
			print(step, sess.run(Weights), sess.run(biases))

if __name__ == '__main__':
	# Call the modes...
	mode1()
