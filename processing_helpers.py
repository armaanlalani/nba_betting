import pandas as pd

def convert_date_to_datetime(df, column_name='GAME_DATE'):
    df[column_name] = pd.to_datetime(df[column_name], format='%b %d, %Y')
    return df


def get_season_str(season_year):
    return f"{season_year}-{(season_year + 1) % 100:02d}"