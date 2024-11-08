from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd

from processing_helpers import *

def get_player_df():
    return pd.DataFrame(players.get_players())

def get_nba_player_id(player_df, player_name):
    return player_df.loc[player_df['full_name'] == player_name, 'id'].values[0]

def get_player_game_data(player_id, season_str):
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season_str)
    return game_log.get_data_frames()[0]

def get_player_game_ids(game_log_data):
    return game_log_data['Game_ID'].tolist()

def get_player_games(player_id, season_start_year, season_end_year):
    all_game_ids = []
    all_game_log_data = pd.DataFrame()

    for season_year in range(season_start_year, season_end_year + 1):
        season_str = get_season_str(season_year)
        game_log_data = get_player_game_data(player_id, season_str)
        all_game_log_data = pd.concat([all_game_log_data, game_log_data])

        game_ids = get_player_game_ids(game_log_data)
        all_game_ids.extend(game_ids)

    all_game_log_data = convert_date_to_datetime(all_game_log_data)
    all_game_log_data = all_game_log_data.sort_values(by='GAME_DATE').reset_index(drop=True)
    return all_game_log_data, all_game_ids