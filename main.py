import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


uploaded_file = st.file_uploader("Choose a file")

data = pd.read_csv(uploaded_file)
shape = data.shape
row_count = shape[0]
col_count = shape[1]

st.write("number of rows:", row_count)
st.write("number of columns:", col_count)

numeric_count = 0
for column in data.columns:
    if pd.api.types.is_numeric_dtype(data[column]):
        numeric_count += 1


categorical_count = 0
for column in data.columns:
    if pd.api.types.is_string_dtype(data[column]):
       categorical_count += 1


st.write("number of numeric variable:", numeric_count)
st.write("number of categorical variable:", categorical_count)

selected_col = st.selectbox( "Select one of the columns", data.columns)
data_col = data[selected_col]

st.write(selected_col, ":")
if pd.api.types.is_numeric_dtype(data_col):
    st.table(data_col.describe())
    #sns.distplot(a = data_col)
    fig, ax = plt.subplots()
    ax.hist(data_col, bins=20, color = 'red')
    st.pyplot(fig)
else:
    prop = data_col.value_counts(normalize=True)
    st.write(prop)
    fig2, ax2 = plt.subplots()
    prop.plot(kind='bar', ax = ax2 ,color = 'purple')
    st.pyplot(fig2)
    




