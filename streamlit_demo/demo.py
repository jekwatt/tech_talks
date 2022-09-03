import os
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


media_dir = Path("media")
data_dir = Path("data")


# text

st.title("What is Streamlit?")
st.image(str(media_dir / "streamlit.png"))
st.header("Allows you to quickly build web applications and dashboards in Python")

# streamlit supports markdown
st.write("""
Three advantages of Streamlit
1. Regular python files as a source
2. Compatible with many visualizations libraries (Matplotlib, seaborn, Plotly, Altair)
3. User interactions are simple to write

[Link to docs](https://docs.streamlit.io/)
for `streamlit documentation`
""")

st.subheader("Hope you are excited about the demo!")

# TODO: audio

# TODO: video


# Demo


# button
result = st.button("Click Me 👈")
st.write(result)
if result:
    st.write(":snake:")


# dataframe
df = pd.DataFrame(
    data=np.random.randn(10, 4),
    columns=[f"col_{i}" for i in range(4)],
)

st.title("DataFrame")
st.write("Show me the data!")
st.write(df)


# plot
st.title("Plot")

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
ax.set_title("Plot")
ax.set_xlabel("x-label")
ax.set_ylabel("y-label")
st.write(fig)


# data
st.title("Iris Data")

iris_path = data_dir / "iris.csv"
iris = pd.read_csv(iris_path)
st.write(iris)


# Matplotlib + pandas

st.header("How many iris flowers of each species are in our dataset?")

counts = iris["species"].value_counts()

count_ax = counts.plot.bar(
    color=["blue", "red", "green"]
)
st.write(count_ax.figure)


# seaborn

st.header("Can petal widthbe used to distingushed the species?")

petal_dist = sns.displot(
    iris, x="petal_width",
    hue="species", kind="kde"
)
st.write(petal_dist.fig)

# Plotly

st.header("Is the sepal length useful for classifying species?")

scat = px.scatter(
    iris,
    x="sepal_length",
    y="sepal_width",
    marginal_x="box",
    marginal_y="violin",
    color="species"
)
st.write(scat)


# interaction

# radio

iris = st.radio(
    "Select an Iris",
    options=["setosa", "versicolor", "virginica"])
st.header(f"Here is a {iris}!")
image_path = os.path.join("media", f"{iris}.jpeg")
st.image(image_path)
# multiselect
st.header("`st.multiselect`")
options = st.multiselect(
    "What is your favorite pet?",
    ("dog", "cat", "fish", "bird", "snake")
)
st.subheader(f"Multiselect:  **{options}**")
st.write("---")


# slider
st.header("`st.slider`")
value = st.slider(
    "Choose a value",
    min_value=0,
    max_value=100,
    step=1,
    value=50,
)
st.subheader(f"Slide selected: {value}")
st.write("---")
