import streamlit as st # library using to build app
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
import pickle #loading our scikit learn scalar
import random
import cv2


X_sample = np.load('data/sample/X_sample.npy') # loading in our x and y samples for google collab and model
y_sample = np.load('data/sample/y_sample.npy')
model = load_model('models/Updated_Best_Model/best_model03')
scaler = pickle.load(open('models/pre_process/scaler.pkl', 'rb'))

#define button
if st.button("Load and Predict Random Galaxy Image"): #defines what text you want on button


# install streamlit, 


    #pick a random number --> have code that can randomly select between 0-49
    random_index = random.randint(0,X_sample.shape[0]-1) # one less than 50 0-49 it will generate random number between 0-49
    image = X_sample[random_index] # pick random index image
    st.image(image) # display image to user on screen


    # we want to preprocess image
    image = cv2.resize(image, (64, 64)) # that's the one we used to preprocess to train our model needs to be same
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # we are doing gray scaling
    image = image.ravel() # to get 4096 pixels(columns)
    image = image.reshape(1,-1) # this is new , we are only processing 1 image , we want to reshape, adding extra dim
    image = scaler.transform(image) # min max scalar this is what we needed to downloading collab using pickle
    image = image.reshape((1, 64, 64, 1)) # reshaping image to fit convo

  


    #feed this image to model --> model will give us a prediction telling us which class this belongs to
    pred = model.predict(image)

    pred = np.argmax(pred, axis=1)[0] # slight modification so we can just extract which class it belongs to 1 value out 10 


    # after we get the prediction , we need to display to user need to stream it 
    st.text(f'Predicted class: {pred}') # pred is just number 1-10 1,  one for predicted one for actual : f means insert variables inside string to display pred as string
    st.text(f'Actual class: {y_sample[random_index]}') # the actual class will be the correct label out of 10 for that image


#pip install scikit_learn
#pip install matplotlib
#pip install numpy
#pip install tensorflow
#pip install opencv-python 
