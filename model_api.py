from flask import Flask,request,json
import numpy as np
from keras.models import Model,Sequential
from keras.utils import to_categorical
from keras.optimizers import RMSprop,Adam
from keras.losses import categorical_crossentropy
from keras.layers.pooling import GlobalAveragePooling2D,MaxPool2D
from keras.layers import Dense,Input,Conv2D,Flatten,BatchNormalization,Dropout
from keras.callbacks import ModelCheckpoint
from flask_cors import CORS
import cv2
import os
import pickle
app = Flask(__name__)

CORS(app)
IMG_SHAPE = (225,225, 3)
NUM_CLASS = 2

def get_model():
    model = Sequential()
    model.add( Conv2D (32,kernel_size=(3,3),activation='relu', 
                        input_shape=(225,225,3),data_format="channels_last"))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add( Conv2D (64,kernel_size=(3,3),activation='relu', 
                        input_shape=IMG_SHAPE,data_format="channels_last"))
    model.add(BatchNormalization())
    model.add(MaxPool2D(pool_size=(2, 2)))

    model.add(Flatten())
    model.add(Dense(2, activation='softmax'))

    if os.path.isfile('flood_weights.h5'):
        model.load_weights('flood_weights.h5')
        print( "Loaded weights!")
    
    return model

model = get_model()
classes = ['Not','Flood']

@app.route("/classify", methods=['POST'])
def predict():
    image = request.data
    im = pickle.loads(image)
    print(im.shape)
    img = cv2.resize(im, IMG_SHAPE[:2])
    print(img.shape)
    cl = model.predict(np.expand_dims(img, axis=0))
    rs = classes[np.argmax(cl)]
    print(rs)
    return rs

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
