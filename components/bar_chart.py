import altair as alt
import streamlit as st


# Define a function to create a bar chart
def create_bar_chart(data, x_col, y_col):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X(f"{x_col}:O", sort='-y'),  # Sort x-axis in descending order
        y=f"{y_col}:Q"
    ).properties(
        width=600
    )
    streamlit_chart = st.altair_chart(chart, use_container_width=True)
    return streamlit_chart