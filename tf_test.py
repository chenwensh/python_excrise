#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import tensorflow as tf
import numpy as np

def linear_regression_model():
	# Model parameters
	W = tf.Variable([.3], tf.float32)
	b = tf.Variable([-.3], tf.float32)

	# Model input and output
	x = tf.placeholder(tf.float32)
	y = tf.placeholder(tf.float32)
	linear_model = x * W + b

	# Loss function
	loss = tf.reduce_sum(tf.square(linear_model - y))

	# Optimizer
	optimizer = tf.train.GradientDescentOptimizer(0.01)
	train = optimizer.minimize(loss)
	
	# Training data
	x_train = [1,2,3,4]
	y_train = [0,1,2,3]

	# Traing loop
	init = tf.global_variables_initializer()
	sess = tf.Session()
	sess.run(init)

	for step in range(1000):
		sess.run(train, {x:x_train, y:y_train})
		if step % 100 == 0:
			curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x:x_train, y:y_train})
			print("Current W is %s, current b is %s, current loss is %s."%(curr_W, curr_b, curr_loss))
	
def linear_mode1():
	# Create the training data
	x_data = np.random.rand(100).astype(np.float32)
	y_data = x_data * 0.1 + 0.3

	# Create the tensorflow structure
	Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
	biases = tf.Variable(tf.zeros([1]))

	y = x_data * Weights + biases
	
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
	#linear_mode1()
	linear_regression_model()
