from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.endpoints import boxscoretraditionalv2

# Specify the Game ID for the desired game
game_id = '0022000001'  # Replace with the actual Game ID

# Retrieve the boxscore data
boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=game_id)
boxscore_data = boxscore.get_data_frames()

# Display the boxscore information
print(boxscore_data)

# # Anthony Davis
# career = playercareerstats.PlayerCareerStats(player_id="203076")
# data = career.get_data_frames()[0]

# print(data)