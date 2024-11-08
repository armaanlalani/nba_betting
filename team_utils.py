from nba_api.stats.static import players
from nba_api.stats.static import teams
from nba_api.stats.endpoints import playergamelog
import pandas as pd

from processing_helpers import *

def get_team_df():
    return pd.DataFrame(teams.get_teams())

def get_nba_team_id(team_df, team_name):
    return team_df.loc[team_df['full_name'] == team_name, 'id'].values[0]