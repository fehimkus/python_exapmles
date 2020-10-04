import tensorflow as tf

a=tf.constant(5)
b=tf.constant(4)
c=tf.constant(a, b)
d=tf.constant(2)
e=tf.constant(3)
f=tf.constant(d, e)
g=tf.constant(c, f)


with tf.Session() as sess:
    writer=tf.summary.FileWriter("output", sess.graph)
    print(sess.run(g))
    writer.close()
