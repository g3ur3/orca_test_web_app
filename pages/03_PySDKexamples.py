import streamlit as st
import pandas as pd
from PIL import Image
data_dir = './data/'

st.title('PySDKExamples output examples')
st.caption('Running the scripts within PySDKExamples')

#Basic outputs
st.subheader('Basic Exampels')
col1, col2 = st.columns(2)

with col1:
    st.text('object_detection_image.ipynb')
    image = Image.open(data_dir + 'object_detection_image.png')
    st.image(image, width = 300)
    st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/basic/basic_pysdk_demo_image.ipynb')
    
with col2:
    st.text('object_detection_video_stream.ipynb')
    image = Image.open(data_dir + 'object_detection_video.png')
    st.image(image, width = 300)
    st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_video_stream.ipynb')

#Specialized outputs
st.subheader('Advanced Algorithms')
col1, col2 = st.columns(2)

with col1:
    st.text('multi_object_tracking_video_file.ipynb')
    image = Image.open(data_dir + 'multi_object_tracking_video.png')
    st.image(image, width = 350)
    st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/multi_object_tracking_video_file.ipynb')
    
with col2:
    st.text('object_detection_in_zone_counting_video_file.ipynb')
    image = Image.open(data_dir + 'object_in_zone_counting_video.png')
    st.image(image, width = 350)
    st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/singlemodel/object_detection_video_stream.ipynb')

col1, col2 = st.columns(2)

with col1:
    st.text('sliced_object_detection.ipynb')
    image = Image.open(data_dir + 'sliced_object_detection.png')
    st.image(image, width = 350)
    st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/specialized/multi_object_tracking_video_file.ipynb')
