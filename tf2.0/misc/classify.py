import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense, Activation
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam
 
learning_rate = 0.001
training_iters = 5
batch_size = 128
display_step = 10
 
n_input = 28
n_step = 28
n_hidden = 128
n_classes = 10

fashion_mnist = keras.datasets.fashion_mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
#(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()
print('y_train:',y_train)
 
x_train = x_train.reshape(-1, n_step, n_input)
x_test = x_test.reshape(-1, n_step, n_input)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print('x_train.shape:',x_train.shape)
print('x_test.shape:',x_test.shape)
#y_train = keras.utils.to_categorical(y_train, n_classes)
#y_test = keras.utils.to_categorical(y_test, n_classes)
print('y_train:',y_train)

model = Sequential()
model.add(LSTM(n_hidden,
               batch_input_shape=(None, n_step, n_input),
               unroll=True))
 
model.add(Dense(n_classes))
model.add(Activation('softmax'))

adam = Adam(lr=learning_rate)
model.summary()
model.compile(optimizer=adam,
              #loss='categorical_crossentropy',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])
 
model.fit(x_train, y_train,
          batch_size=batch_size,
          epochs=training_iters,
          verbose=1,
          validation_data=(x_test, y_test))
 
scores = model.evaluate(x_test, y_test, verbose=0)
print('LSTM test score:', scores[0])
print('LSTM test accuracy:', scores[1])
