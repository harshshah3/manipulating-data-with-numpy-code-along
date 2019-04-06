# --------------
import numpy as np
# Not every data format will be in csv there are other file formats also.
# This exercise will help you deal with other file formats and how to read it.

#reading the data
data = np.genfromtxt(path, delimiter = ",", skip_header = 1, dtype=str)

# Number of unique matches 
len(set(data[:, 0]))
print(np.unique(data[:, 0]).size)

# How many matches were held in total we need to know so that we can analyze further       statistics keeping that in mind.
# Number of unique teams
unique_teams = np.unique(data[:, 3:5])
print(unique_teams)

# this exercise deals with you getting to know that which are all those six teams that   played in the tournament.

# Sum of all extras

extras = data[:, 17]
extras_int = extras.astype('int16')
sum_extras = np.sum(extras_int)
print(sum_extras)

# An exercise to make you familiar with indexing and slicing up within data.
# Delivery number when a given player got out
#concept used: filter
batsman = 'SR Tendulkar'
#wickets_mask = data[:, 11][data[:, 20] == batsman]
player_out_mask = data[:, 20] == batsman
wickets_arr = data[player_out_mask]
wickets_arr[:, 11] #delivery

# Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
  
wickets_arr[:, 21] #wicket_kind

# Number of times Mumbai Indians won the toss
'''
logic breakdown: GET ALL MATCHES WON BY MI, GET THE UNIQUE_CODE AND COUNT THEM 
toss_winner = "Mumbai Indians"
toss_winner_mask  = data[:, 5] == toss_winner
np.unique(data[:, 0][toss_winner_mask]).size
'''

team_toss_won = data[data[:, 5] == 'Mumbai Indians']
count_toss_won = np.unique(team_toss_won[:,0]).size

#HOW MANY MATCHES DID MI PLAYED
team = 'Mumbai Indians'
team_mask = np.logical_or(data[:, 3] == team, data[:, 4] == team)
total_matches = np.unique(data[:, 0][team_mask]).size
print("MI won toss in ", count_toss_won, "out of", total_matches)

# this exercise will help you get the statistics on one particular team
# Filter record where batsman scored six and player with most number of sixex

#logic breakdown: get all deliveries, then count the sixes, then find most number
sixer_mask = data[:, 16] == '6'
sixer_deli = data[sixer_mask]

#---------------
from collections import Counter

count_batsman = Counter(sixer_deli[:, 13])
print(count_batsman.most_common(2))




