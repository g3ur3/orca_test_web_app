import streamlit as st
import pandas as pd
from PIL import Image

data_dir = '/home/gotom/orca_test_plans/orca_test_web_app/data/'

st.title('ORCA Driver Install')
st.caption('Installing ORCA Linux driver to the target system')
#ORCA driver installation
st.subheader('Linux Kernel Driver Installation')
st.link_button('Explanation', 'https://docs.degirum.com/content/orca/driver/')

#PySDK installation
st.title('PySDK Installation')
st.caption('Install PySDK to the target system')
st.subheader('PySDK Python package installation')
st.link_button('Installation Guide', 'https://docs.degirum.com/content/pysdk/installation/')