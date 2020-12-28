import tensorflow.compat.v1 as tf
tf.compat.v1.disable_eager_execution()

x1 = tf.constant([1,2,3,4])
x2 = tf.constant([5,6,7,8])

result = tf.multiply(x1,x2)

with tf.Session() as sess:
    output = sess.run(result)
    print(output)
