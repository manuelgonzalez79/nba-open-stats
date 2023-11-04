
import pandas as pd
import streamlit as st
import nba_calls
import visualize

# Streamlit dashboard
st.title("NBA Player Stats Dashboard")


# Sidebar components
st.sidebar.header("Filters")
age = st.sidebar.slider("Select Age", 18, 38, 18, 1)
height = st.sidebar.slider("Select Height (in feet)", 6.0, 7.5, 6.0, 0.1)
min_mpg = st.sidebar.slider("Select Minimum MPG", 0.0, 40.0, 0.0, 1.0)
games = st.sidebar.slider("Select Minimum Games played", 0, 82, 0, 1)

# Get player statistics
all_players_stats = nba_calls.get_player_combined_stats()

# Replace '-' with '.'
all_players_stats['PLAYER_HEIGHT'] = all_players_stats['PLAYER_HEIGHT'].str.replace('-', '.', regex=False)

# Filter players based on age and height
filtered_players = all_players_stats[(pd.to_numeric(all_players_stats['AGE']) >= age) 
                                     & (pd.to_numeric(all_players_stats['PLAYER_HEIGHT']) >= height) 
                                     & (pd.to_numeric(all_players_stats['MPG']) >= min_mpg) 
                                     & (pd.to_numeric(all_players_stats['GP']) >= games)]



# Display bar charts
st.header("Top 20 Players by Net Rating")
net_rating_data = filtered_players.nlargest(20, 'NET_RATING')
net_rating_chart = visualize.create_bar_chart(net_rating_data, 'PLAYER_NAME', 'NET_RATING')
st.altair_chart(net_rating_chart, use_container_width=True)

st.header("Top 20 Players by Points")
points_data = filtered_players.nlargest(20, 'PTS')
points_chart = visualize.create_bar_chart(points_data, 'PLAYER_NAME', 'PTS')
st.altair_chart(points_chart, use_container_width=True)

st.header("Top 20 Players by Assists")
assists_data = filtered_players.nlargest(20, 'AST')
assists_chart = visualize.create_bar_chart(assists_data, 'PLAYER_NAME', 'AST')
st.altair_chart(assists_chart, use_container_width=True)

st.header("Top 20 Players by Rebounds")
rebounds_data = filtered_players.nlargest(20, 'REB')
rebounds_chart = visualize.create_bar_chart(rebounds_data, 'PLAYER_NAME', 'REB')
st.altair_chart(rebounds_chart, use_container_width=True)