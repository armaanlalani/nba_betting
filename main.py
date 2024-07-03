from player_utils import *
from team_utils import *
from game_utils import *

if __name__ == '__main__':
    nba_players = get_player_df()
    nba_teams = get_team_df()
    start_year, end_year = 2010, 2024

    while True:
        try:
            player_name = input("Enter the player's name: ")
            player_id = get_nba_player_id(nba_players, player_name)
            print(f"You have selected {player_name} with player_id {player_id}")
            break
        except:
            print("You have entered an invalid player. Please try again.")
    
    opponent = input("Enter the opposing team: ")
    statistic = input("Enter the player's primary statistic [MIN/FGM/FGA/FG_PCT/FG3M/FG3A/FTM/FTA/OREB/DREB/REB/AST/STL/BLK/TOV/PF/PTS]: ")
    stat_number = float(input("Enter the value of the player's statistic: "))
    over_under = input("Enter whether you're checking over or under the primary statistic [over/under]: ")
    
    # lal_id = get_nba_team_id(nba_teams, 'Los Angeles Lakers')

    player_game_log, player_game_ids = get_player_games(player_id, start_year, end_year)
    player_game_log_filtered = filter_games_by_opponent(player_game_log, opponent)
    num_games_satisfying_constraint, num_games = get_stat_from_games(player_game_log_filtered, statistic, stat_number, over_under)
    print(f'In his last {num_games} games against {opponent}, {player_name} has recorded {over_under} {stat_number} {statistic} in {num_games_satisfying_constraint} games')    
