from nba_api.stats.static import players

def get_nba_player_id(player_df, player_name):
    return player_df.loc[player_df['full_name'] == player_name, 'id'].values[0]

def get_nba_team_id(team_df, team_name):
    return team_df.loc[team_df['full_name'] == team_name, 'id'].values[0]