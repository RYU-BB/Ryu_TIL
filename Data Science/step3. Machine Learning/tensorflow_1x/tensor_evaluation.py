import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

constant = tf.constant([1,2,3])
v1 = constant * constant

with tf.Session() as sess:
    print(v1.eval())
    
with tf.Session() as sess:
    p = tf.placeholder(tf.float32)
    t1 = p + 1.0
    t2 = p + 2.0
    print(sess.run([t1,t2], feed_dict={p: 2.0}))