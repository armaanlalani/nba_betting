from player_utils import *
from team_utils import *

if __name__ == '__main__':
    nba_players = get_player_df()
    nba_teams = get_team_df()

    anthony_davis_id = get_nba_player_id(nba_players, 'Anthony Davis')
    lal_id = get_nba_team_id(nba_teams, 'Los Angeles Lakers')

    anthony_davis_game_log, anthony_davis_game_ids = get_player_games(anthony_davis_id, 2015, 2020)

    print(anthony_davis_game_log)
    
