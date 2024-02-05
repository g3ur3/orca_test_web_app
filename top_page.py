import streamlit as st
from PIL import Image
import pandas as pd
#Text
st.title('ORCA Test Plans for Target Device (Preliminary)')
st.caption('Basic interoeprability checking procedure')
st.subheader('Installation')
st.text('* ORCA driver (OS:Linux)')
st.text('* PySDK')
st.subheader('Benchmark')
st.text('* Single model')
st.text('* Multi model')
#st.text('* Benchmark (ORCA vs. EdgeTPU)')
st.subheader('PySDKExamples')
st.subheader('Basic')
st.text('* basic_pysdk_demo_image.ipynb')
st.text('* basic_pysdk_demo_video_stream.ipynb')
st.subheader('Advanced algorithm')
st.text('* multi_object_tracking__video_file.ipynb')
st.text('* object_in_zone_counting_video_stream.ipynb')
st.text('* sliced_object_detection.ipynb')

# test_categoriesL = ['Installation', 'Benchmark', 'Run PySDKExamples script']
# scriptsL = ['NA', 'single_model_performance_test.ipynb'+'\n'+'single_model_performance_test.ipynb','']
# remarksL = ['OS: Linux','','']

# df = pd.DataFrame({'Test Category': test_categoriesL, 'Test Script': scriptsL, 'Remarks': remarksL})

# st.dataframe(df, width=600)
