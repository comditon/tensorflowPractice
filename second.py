from __future__ import print_function
import tensorflow as tf

sess = tf.Session()

node1 = tf.constant(3.0)
node2 = tf.constant(4.0)
node3 = tf.add(node1, node2)

print(node3)
print(sess.run(node3))
