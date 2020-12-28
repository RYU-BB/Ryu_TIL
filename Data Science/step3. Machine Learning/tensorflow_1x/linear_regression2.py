# with tensorflow function
import numpy as np
import matplotlib.pyplot as plt
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

sample_n = 100
x = np.random.randn(sample_n)
y = x*10 + 10
noise = np.random.randn(sample_n) * 7
y = y + noise

X = tf.placeholder("float")
Y = tf.placeholder("float")
W = tf.Variable(np.random.randn(), name = "W")
b = tf.Variable(np.random.randn(), name = "b")

# Graph
y_pred = X * W + b
cost = tf.reduce_mean(tf.square(y_pred - Y))

# deep learning
learning_rate = 0.02
epochs = 300

optimizer = tf.train.GradientDescentOptimizer(learning_rate = learning_rate)
train = optimizer.minimize(cost)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

loss_history = []

for epoch in range(epochs):
    cost_val, W_val, b_val, _ = sess.run([cost, W, b, train], feed_dict={X:x, Y:y})
    loss_history.append(cost_val)
    print("epoch", epoch, ": ", cost_val)
    
sess.close()

plt.plot(loss_history)