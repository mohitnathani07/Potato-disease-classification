import streamlit as st
from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing.image import array_to_img, img_to_array, load_img
from tensorflow.keras.preprocessing import image
import os
import math
import base64


modelPath = "model.keras"
MODEL = load_model(modelPath)
CLASS_NAMES = ["Early Blight", "Late Blight", "Normal"]
st.title("Potato Disease Classification")
st.logo("static/logo.png")
imgPath = st.file_uploader("Upload a image", accept_multiple_files=True)


placeholder = []
if imgPath is not None:
    for i in imgPath:
        placeholder.append(st.image(i))



def getPrediction(imgPath):
    img = image.load_img(imgPath, target_size=(255, 255))
    img_array = image.img_to_array(img)

    # Add an extra dimension to the array (since the model expects a batch)
    img_array = np.expand_dims(img_array, axis=0)

    # Make predictions
    predictions = MODEL.predict(img_array)
    predicted_class = np.argmax(predictions)
    return predicted_class, predictions


if st.button("Submit"):
    for place in placeholder:
        place.empty()
    if imgPath is not None:

        for currentImage in imgPath:

            col1, col2 = st.columns(2)
            potato_class, level = getPrediction(currentImage)
            level = round(max(level[0]) * 100, 2)

            if level < 80:
                with col1:
                    st.image(currentImage)
                with col2:
                    st.text("")
                    st.text("")
                    st.text("")
                    st.text("")
                    st.text("")
                    st.write("Upload the image again")
            else:
                with col1:
                    st.image(currentImage)
                with col2:
                    st.text("")
                    st.text("")
                    st.text("")
                    st.text("")
                    st.text("")
                    st.write(f"Potato is {CLASS_NAMES[potato_class]}")
                    st.write(f"Confidence level: {level}")

            st.text("")
            st.text("")
            st.text("")

    else:
        st.write("Upload an Image")



