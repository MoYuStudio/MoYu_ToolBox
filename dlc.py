import requests

# Your app ID and DLC ID
app_id = 2384480
dlc_id = 2384490

# The player's Steam ID
steam_id = 'STEAM_ID_HERE'

# Construct the URL for retrieving the player's achievements
url = f'http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={app_id}&key=STEAM_API_KEY&steamid={steam_id}'

# Make the API request
response = requests.get(url)

# Parse the response JSON and check for the DLC achievement
json_data = response.json()
if 'playerstats' in json_data and 'achievements' in json_data['playerstats']:
    for achievement in json_data['playerstats']['achievements']:
        if achievement['apiname'] == f'dlc{dlc_id}_achievement_name':
            print('Player has purchased the DLC')
            break
    else:
        print('Player has not purchased the DLC')
else:
    print('Failed to retrieve player achievements')
