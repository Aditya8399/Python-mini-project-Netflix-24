import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt


# 0. Configure the page

st.set_page_config(
    page_title="Netflix Engagement App",
    page_icon="🎥",
    layout="wide",
)

# 1. Load the data

@st.cache_data
def load_data():
    url = 'Data/Netflix Engagement (plus).csv'
    df = pd.read_csv(url,)
    return df

# 2. Build the UI

st.title("Netflix Engagement App")
with st.spinner("Loading data...."):
    df = load_data()

st.header("Netflix Engagement Dataset")
st.info("Raw data in DataFrame")
st.dataframe(df, use_container_width=True)

st.success("Column information of the dataset")
cols = df.columns.tolist()
st.subheader(f'Total columns {len(cols)} ➡️  {", ".join(cols)}')

# 3. Add some graphs and widgets

st.header("Basic Data Visualization")
gop = ['bar', 'line', 'area']

# Plot for Rating
st.header("Rating Visualization")
sel_op = st.selectbox("Select the type of plot for Rating", gop)
subset = df.sort_values(by='Rating')[:50]
if sel_op == gop[0]:
    fig = px.bar(subset, x='Title', y='Rating', log_y=True)
elif sel_op == gop[1]:
    fig = px.line(subset, x='Title', y='Rating')
elif sel_op == gop[2]:
    fig = px.area(subset, x='Title', y='Rating')
st.plotly_chart(fig, use_container_width=True)

# Plot for Number of Ratings
st.header("Number of Ratings Visualization")
sel_op2 = st.selectbox("Select the type of plot for Number of Ratings", gop)
subset2 = df.sort_values(by='Number of Ratings')[:50]
if sel_op2 == gop[0]:
    fig = px.bar(subset2, x='Title', y='Number of Ratings', log_y=True)
elif sel_op2 == gop[1]:
    fig = px.line(subset2, x='Title', y='Number of Ratings')
elif sel_op2 == gop[2]:
    fig = px.area(subset2, x='Title', y='Number of Ratings')
st.plotly_chart(fig, use_container_width=True)

# Plot for Genre
st.header("Genre Visualization")
sel_op3 = st.selectbox("Select the type of plot for Genre", gop)
subset3 = df.sort_values(by='Genre')
if sel_op3 == gop[0]:
    fig = px.bar(subset3, x='Title', y='Genre', log_y=True)
elif sel_op3 == gop[1]:
    fig = px.line(subset3, x='Title', y='Genre')
elif sel_op3 == gop[2]:
    fig = px.area(subset3, x='Title', y='Genre')
st.plotly_chart(fig, use_container_width=True)

# Plot for Available Globally?
st.header("Available Globally? Visualization")
sel_op4 = st.selectbox("Select the type of plot for Available Globally?", gop)
subset4 = df.sort_values(by='Available Globally?')[:50]
if sel_op4 == gop[0]:
    fig = px.bar(subset4, x='Title', y='Available Globally?', log_y=True)
elif sel_op4 == gop[1]:
    fig = px.line(subset4, x='Title', y='Available Globally?')
elif sel_op4 == gop[2]:
    fig = px.area(subset4, x='Title', y='Available Globally?')
st.plotly_chart(fig, use_container_width=True)

# Histograms for Numerical Columns
st.header("Histograms for Numerical Columns")
num_cols = df.select_dtypes(include=np.number).columns.tolist()
selected_col_hist = st.selectbox("Select a numerical column for histogram", num_cols)
fig_hist = px.histogram(df, x=selected_col_hist, nbins=30, title=f'Histogram of {selected_col_hist}')
st.plotly_chart(fig_hist, use_container_width=True)

# Pie chart for Hours Viewed
st.header("Hours Viewed Distribution")
genre_counts = df['Hours Viewed'].value_counts()
fig_pie = px.pie(genre_counts, names=genre_counts.index, values=genre_counts.values, title='Hours Viewed Distribution')
st.plotly_chart(fig_pie, use_container_width=True)

# 4. Adjust layout

st.header("Bivariate Analysis")
col1 = st.selectbox("Select the first column for scatter plot", num_cols) 
col2 = st.selectbox("Select the second column for scatter plot", num_cols) 
fig_bivariate = px.scatter(df, x=col1, y=col2, title=f'{col1} vs {col2}')
st.plotly_chart(fig_bivariate, use_container_width=True)

st.header("Tivariate Analysis")
col3 = st.selectbox("Select the first column for 3d plot", num_cols)
col4 = st.selectbox("Select the second column for 3d plot", num_cols)
col5 = st.selectbox("Select the third column for 3d plot", num_cols)
fig_trivariate = px.scatter_3d(df, x=col3, y=col4, z=col5, title=f'{col3} vs {col4} vs {col5}', height=600)
st.plotly_chart(fig_trivariate, use_container_width=True)

# About tab 

st.header("About")

st.markdown("""
This Streamlit app provides visualizations and analysis of the Netflix Engagement dataset. 
Explore various aspects of the data using different plot types such as bar, line, and area plots. 
Additionally, analyze bivariate and trivariate relationships through scatter plots and 3D scatter plots.

### How to run the app
1. Ensure you have Python and Streamlit installed.
2. Open the terminal.
3. Run the command: `streamlit run main.py`

Enjoy exploring the Netflix Engagement data interactively!

Created By
Aditya singh
""")
