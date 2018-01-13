from __future__ import print_function
import tensorflow as tf

sess = tf.Session()

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

print(sess.run(adder_node, {a : 3, b : 4.5}))
print(sess.run(adder_node, {a : [3,4], b : [4.5,5.5]}))
