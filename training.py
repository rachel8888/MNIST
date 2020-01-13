import tensorflow as tf
def loading_dataset(trainX, testX, trainy, testy):
    mnist = tf.keras.datasets.mnist
    (trainX, trainy), (testX, testy) = mnist.load_data()
    trainX = tf.keras.utils.normalize(trainX, axis=1)
    testX = tf.keras.utils.normalize(testX, axis=1)
    return trainX, testX, trainy, testy
    
def training_model():
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Flatten())
    model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
    model.add(tf.keras.layers.Dense(128, activation = tf.nn.relu))
    model.add(tf.keras.layers.Dense(10, activation = tf.nn.softmax))
    model.compile(optimer= 'adam',loss='sparse_categorical_crossentropy',metrics = ['accuracy'])
    return model
def fitting_model():
    model = training_model()
    trainX, trainy, testX = loading_dataset()
    model.fit(trainX, trainy, epochs = 40)
    predictions = model.predict(testX)
    return predictions

def checking_validation(val_loss, val_acc):
    testX, testy = loading_dataset()
    model = training_model()
    val_loss, val_acc  = model.evaluate(testX,testy)
    return val_loss , val_acc
def saving_Newmodel():
    model = training_model()
    return model.save('epic_num_reader.model')

def main():
    loading_dataset()
    training_model()
    fitting_model()
    checking_validation()
    saving_Newmodel()

if __name__ == 'main':
    main()