# template for Wyscout data

###
# importing libraries
###

from os import chdir
import pathlib
import os
import json
import pandas as pd

chdir("/Users/simpsonj/Documents/Soccermatics/Data/Wyscout/")

###
# competitions
###

competitions_path = os.path.join(str(pathlib.Path().resolve()),
                                 "competitions.json")

with open(competitions_path) as f:
    competitions_data = json.load(f)
    
df_competitions = pd.DataFrame(competitions_data)
df_competitions.info()

###
# matches
###

matches_path = os.path.join(str(pathlib.Path().resolve()),
                            "matches/matches_England.json")

with open(matches_path) as f:
    matches_data = json.load(f)
    
df_matches = pd.DataFrame(matches_data)
df_matches.info()

###
# players
###

players_path = os.path.join(str(pathlib.Path().resolve()), "players.json")

with open(players_path) as f:
    players_data = json.load(f)
    
df_players = pd.DataFrame(players_data)
df_players.info()

###
# events
###

events_path = os.path.join(str(pathlib.Path().resolve()),
                           "events/events_England.json")

with open(events_path) as f:
    events_data = json.load(f)
    
df_events = pd.DataFrame(events_data)
df_events.info()