import streamlit as st
import pandas as pd
from PIL import Image

data_dir = './data/'

st.title('ORCA Benchmark Test')
st.caption('Orca Benchmark Scripts from PySDKExamples')
#Single model benchmark
st.subheader('single_model_performance_test.ipynb')
st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/benchmarks/single_model_performance_test.ipynb')

st.text('Output Example')
image = Image.open(data_dir + 'benchmark_single_model.png')
st.image(image, width = 1000)


#Multi model benckmark
st.subheader('multi_model_performance_test.ipynb')
st.link_button('Script', 'https://colab.research.google.com/github/DeGirum/PySDKExamples/blob/main/examples/benchmarks/multi_model_performance_test.ipynb')

st.text('Output Example')
image = Image.open(data_dir + 'benchmark_multi_model.png')
st.image(image, width = 800)

# single_model_benchmark = pd.read_table('/home/gotom/orca_test_plans/orca_test_web_app/data/benchmark_multi_model.txt')
# df = pd.DataFrame(single_model_benchmark)
# st.table(df)
