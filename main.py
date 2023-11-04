
import pandas as pd
import streamlit as st
import pages.player_dashboard as player_dashboard
import pages.team_dashboard as team_dashboard


def main():
    app_pages = {
        "Player Statistics": player_dashboard,
        "Team Statistics": team_dashboard,
    }
    
    # Display the selected app page
    app_pages[0]()

if __name__ == "__main__":
    main()