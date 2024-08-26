from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from numpy import loadtxt

dataset = loadtxt('gester_dataset_new.csv', delimiter=',')
train_X = dataset[:,0:42]
train_Y = dataset[:,42]

model = Sequential()
model.add(Dense(21, input_shape=(42,), activation='relu'))
model.add(Dense(5, activation='sigmoid'))

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(train_X, train_Y, epochs=50, batch_size=20)

model.save('trained_model_new')
