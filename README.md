# bkref
Functions to pull data from www.basketball-reference.com

Basketball reference contains rich data on every basketball game played to date. It is beneficial for one to be able to pull this data into their own database to conduct analysis. The functions in this library aid in pulling the data via web scraping with Beautiful Soup in python.

Function list:
get_active - returns a list of of player information and url for active nba players
create_season - returns a list of season stats for a given player url and season
create_gamelog - returns a list of game log stats for a given player url and season
