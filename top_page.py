import streamlit as st
from PIL import Image
#Text
st.title('ORCA Test Plans (Preliminary)')
st.caption('Basic interoeprability checking procedure')
st.subheader('Install')
st.text('* Install ORCA driver')
st.text('* Install PySDK')
st.subheader('Benchmark')
st.text('* Benchmark Single Model')
st.text('* Benchmark Multi Model')
st.subheader('PySDKExamples(basic)')
st.text('* object_detection_image.ipynb')
st.text('* object_detection_video_stream.ipynb')
st.text('* Install PySDK')
st.subheader('PySDKExamples(specialized)')
st.text('* multi_object_tracking__video_file.ipynb')
st.text('* object_in_zone_counting_video_stream.ipynb')
st.text('* sliced_object_detection.ipynb')

#Image
#image = Image.open('./object_detection.png')
#st.image(image, width = 200)