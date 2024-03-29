import streamlit as st
import pandas as pd
from PIL import Image

data_dir = './data/'

st.title('ORCA Driver Installation')
st.caption('Installing ORCA Linux driver to the target system')
#ORCA driver installation
st.subheader('Linux Kernel Driver Installation')
st.link_button('Installation Guide', 'https://docs.degirum.com/content/orca/driver/')

#PySDK installation
st.title('PySDK Installation')
st.caption('Installing PySDK to the target system')
st.subheader('PySDK Python package installation')
st.link_button('Installation Guide', 'https://docs.degirum.com/content/pysdk/installation/')