print("VS Code test!")

###
# import libraries
###

import os
# for importing
from mplsoccer import Sbopen

os.chdir("/Users/simpsonj/Documents/Soccermatics/Data/StatsBomb/")

###
# get all passes across England's matches
###

parser = Sbopen()

df_match = parser.match(competition_id = 72,
                        season_id = 30)

print("Will this print?")

print("This one won't...")