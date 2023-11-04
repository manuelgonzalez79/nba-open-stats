from nba_api.stats.endpoints import leaguedashplayerstats, leaguedashplayerbiostats
import pandas as pd

# Define the current NBA season (you may need to update this)
current_season = "2023-24"

# Function to get player statistics
def get_player_stats(season=current_season):
    player_stats = leaguedashplayerstats.LeagueDashPlayerStats(
        season=season
    )
    player_stats_data = player_stats.get_data_frames()[0]

    return player_stats_data

# Function to get player bio stats
def get_player_bio_stats(season=current_season):
    player_bio_stats = leaguedashplayerbiostats.LeagueDashPlayerBioStats(
        season=season
    )
    player_bio_stats_data = player_bio_stats.get_data_frames()[0]

    return player_bio_stats_data

def calculate_mpg(row):
    games_played = row['GP']
    total_minutes = row['MIN']
    if games_played > 0:
        return total_minutes / games_played
    else:
        return 0


# Get player statistics and player bio stats
def get_player_combined_stats():
    player_stats_data = get_player_stats(current_season)
    player_bio_stats_data = get_player_bio_stats(current_season)

    combined_data = pd.merge(player_stats_data, player_bio_stats_data, how='inner', suffixes=['ST', 'BIO'])
    combined_data['MPG'] = combined_data.apply(calculate_mpg, axis=1)
    
    # Replace '-' with '.'
    combined_data['PLAYER_HEIGHT'] = combined_data['PLAYER_HEIGHT'].str.replace('-', '.', regex=False)

    return combined_data
