import os
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# text
st.title("What is Streamlit?")
st.header("Allows you to quickly build web applications and dashboards in Python")

"""
Three advantages of Streamlit
1. Regular python files as a source
2. Compatible with many visualizations libraries (Matplotlib, Plotly, Altair)
3. User interactions are simple to write
"""

st.subheader("Hope you are excited about this demo!")


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

# basic plot
fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4])
ax.set_xlabel("x-label")
ax.set_ylabel("y-label")
ax.set_title("Basic Plot")

st.write(fig)


# better plot
fontsizes = itertools.cycle([16, 16, 24, 32])


def example_plot(ax):
    ax.plot([1, 2])
    ax.set_xlabel("x-label", fontsize=next(fontsizes))
    ax.set_ylabel("y-label", fontsize=next(fontsizes))
    ax.set_title("Better Plot", fontsize=next(fontsizes))


fig, ax = plt.subplots(figsize=(8, 5))
example_plot(ax)
fig.tight_layout()

st.write(fig)


# interaction

# radio
# multiselect
st.header("`st.multiselect`")
options = st.multiselect(
    "What is your favorite pet?",
    ("dog", "cat", "fish", "bird", "snake")
)
st.subheader(f"Multiselect:  **{options}**")
st.write("---")

# iris flower data set
iris = st.radio(
    "Select an Iris",
    options=["setosa", "versicolor", "virginica"])
st.header(f"Here is a {iris}!")
image_path = os.path.join("images", f"{iris}.jpeg")
st.image(image_path)


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
