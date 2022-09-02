import itertools

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import streamlit as st


# text
st.title("What is Streamlit?")
st.header("Allows you to quickly build web applications and dashboards in Python")
st.subheader("Hope you are excited about this demo!")


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
