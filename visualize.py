import altair as alt

# Define a function to create a bar chart
def create_bar_chart(data, x_col, y_col):
    chart = alt.Chart(data).mark_bar().encode(
        x=alt.X(f"{x_col}:O", sort='-y'),  # Sort x-axis in descending order
        y=f"{y_col}:Q"
    ).properties(
        width=600
    )
    return chart