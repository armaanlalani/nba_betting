from nba_api.stats.static import players
from nba_api.stats.static import teams
import pandas as pd

from utils import *

if __name__ == '__main__':
    nba_players = pd.DataFrame(players.get_players())
    nba_teams = pd.DataFrame(teams.get_teams())

    anthony_davis_id = get_nba_player_id(nba_players, 'Anthony Davis')
    lal_id = get_nba_team_id(nba_teams, 'Los Angeles Lakers')

    print(anthony_davis_id)
    print(lal_id)
    
