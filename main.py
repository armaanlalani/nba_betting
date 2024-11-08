from player_utils import *
from team_utils import *
from game_utils import *
from gpt import *

if __name__ == '__main__':
    nba_players = get_player_df()
    nba_teams = get_team_df()
    player_columns = nba_players.columns.tolist()
    team_columns = nba_teams.columns.tolist()

    user_query = 'How many times has Anthony Davis scored over 40 points over the last 10 years'

    gpt_query = f'From the user query: "{user_query}", can you extract the name of the NBA player we are interested in (only provide the name, no other text)?'
    client, conversation_history, player_name = make_a_query(client, conversation_history, gpt_query)
    print(player_name)

    gpt_query = f'Using the players name: "{player_name}" and the dataframe "nba_players" with columns: "{player_columns}", write me a query that gets the associated player id for the player? (only return the code, no other text)'
    client, conversation_history, player_id_query = make_a_query(client, conversation_history, gpt_query)
    print(player_id_query)

    gpt_query = f'Based on the user query: "{user_query}", can you return a list of years that should be queried? (only return the list)'
    client, conversation_history, years = make_a_query(client, conversation_history, gpt_query)
    print(years)
    exit(0)

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
