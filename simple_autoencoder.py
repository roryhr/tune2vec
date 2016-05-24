import tensorflow as tf
from tensorflow.contrib import ffmpeg


def weight_variable(shape):
  initial = tf.truncated_normal(shape, stddev=0.1)
  return tf.Variable(initial)


def bias_variable(shape):
  initial = tf.constant(0.1, shape=shape)
  return tf.Variable(initial)


def conv2d(x, W):
  return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME')


sess = tf.InteractiveSession()

x = tf.placeholder(tf.float32, [None, 784])
y_ = tf.placeholder(tf.float32, [None, 784])

batch_size = tf.shape(x)[0]

# Define all the weight for the encoder part
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = tf.nn.relu(pool_2x2(h_conv1, W_pool1) + b_pool1)



# h_conv5 = tf.nn.relu(tf.nn.conv2d_transpose(h_conv4, W_conv5, output_shape=deconv_shape_conv5, strides=[1, 1, 1, 1],
#                                             padding='SAME') + b_conv5)
# h_pool3 = tf.nn.relu(tf.nn.conv2d_transpose(h_conv5, W_pool3, output_shape=deconv_shape_pool3, strides=[1, 2, 2, 1],
#                                             padding='SAME') + b_pool3)
# h_conv6 = tf.nn.relu(tf.nn.conv2d_transpose(h_pool3, W_conv6, output_shape=deconv_shape_conv6, strides=[1, 1, 1, 1],
#                                             padding='SAME') + b_conv6)
#
#
# error = tf.nn.l2_loss(y_ - y_conv)
# train_step = tf.train.AdamOptimizer(1e-4).minimize(error)
# accuracy = tf.nn.l2_loss(y_ - y_conv)
# sess.run(tf.initialize_all_variables())
# for i in range(20000):
#     batch = mnist.train.next_batch(50)
#     if i % 20 == 0:
#         train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[0]})
#
#     train_step.run(feed_dict={x: batch[0], y_: batch[0]})


