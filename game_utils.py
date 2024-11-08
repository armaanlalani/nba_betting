from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd

from processing_helpers import *

def filter_games_by_opponent(game_log, opponent):
    return game_log[game_log['MATCHUP'].str[-3:] == opponent]

def get_stat_from_games(game_log, stat_category, stat_value, over_under):
    num_games = len(game_log)
    if over_under == 'over':
        games_satisfying_constraint = game_log[game_log[stat_category] > stat_value]
    elif over_under == 'under':
        games_satisfying_constraint = game_log[game_log[stat_category] < stat_value]
    num_games_satisfying_constraint = len(games_satisfying_constraint)
    return num_games_satisfying_constraint, num_games