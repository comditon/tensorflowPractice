from __future__ import print_function
import tensorflow as tf

sess = tf.Session()

a = tf.placeholder(tf.float32)
b = tf.placeholder(tf.float32)
adder_node = a + b

adder_node_triple = adder_node * 3
print(sess.run(adder_node_triple, {a: 10, b : 27}))
