### Project Overview

 

## IPL Data Analysis

#### Dataset used from :  [(https://cricsheet.org/)] - IPL Data

### Problem Statement
We want to know as to what happens during an IPL match which raises several questions in our mind with our limited knowledge about the game called cricket on which it is based. This analysis is done to know as which factors led one of the team to win and how does it matter.

### About the Dataset :
The Indian Premier League (IPL) is a professional T20 cricket league in India contested during April-May of every year by teams representing Indian cities. It is the most-attended cricket league in the world and ranks sixth among all the sports leagues. It has teams with players from around the world and is very competitive and entertaining with a lot of close matches between teams.

The IPL and other cricket related datasets are available at cricsheet.org. Feel free to visit the website and explore the data by yourself as exploring new sources of data is one of the interesting activities a data scientist gets to do.

The dataset 1452 data points and 23 features:

| Features | Description |
| --- | --- |
| match_code | Code pertaining to individual match |
| date | Date of the match played |
| city | Location where the match was played |
| team1 | team1 |
| team2 | team2 |
| toss_winner | Who won the toss out of two teams |
| toss_decision | toss decision taken by toss winner |
| winner | Winner of that match between two teams |
| win_type | How did the team won(by wickets or runs etc.) |
| win_margin| difference with which the team won |
| inning | inning type(1st or 2nd) |
| delivery | ball delivery |
| batting_team | current team on batting |
| batsman | current batsman on strike |
| non_striker | batsman on non-strike |
| bowler | Current bowler |
| runs | runs scored |
| extras | extra run scored |
| total | total run scored on that delivery including runs and extras |
| extras_type	| extra run scored by wides or no ball or legby |
| player_out | player that got out |
| wicket_kind	| How did the player got out |
| wicket_fielders | Fielder who caught out the player by catch |


Questions : 

1. Calculate the unique no. of matches in the provided dataset ?
2. Find the set of all unique teams that played in the matches in the data set.
3. Find sum of all extras in all deliveries in all matches in the dataset
4. Get the array of all delivery numbers when a given player got out. Also mention the wicket type.
5. How many matches the team Mumbai Indians has won the toss?
6. Create a filter that filters only those records where the batsman scored 6 runs. Also who has scored the maximum no. of sixes overall ?


### Learnings from the project

 This project gives hands on excercise manipulation data with Numpy.


