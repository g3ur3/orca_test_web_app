import streamlit as st
import pandas as pd
from PIL import Image
data_dir = './data/'

st.title('PySDKExamples output examples')
st.caption('Running the scripts within PySDKExamples')
#PySDKExamples Outputs
st.subheader('Basic Examples')
st.text('object_detection_image.ipynb')
st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/basic/basic_pysdk_demo_image.ipynb')
#Image
image = Image.open(data_dir + './object_detection_image.png')
st.image(image, width = 200)