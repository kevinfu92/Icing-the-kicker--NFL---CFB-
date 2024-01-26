from __future__ import print_function
import config
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
import pandas as pd

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = config.api_key
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.PlaysApi(cfbd.ApiClient(configuration))
start_year = 2001 # int | Year filter
end_year = 2024
weeks = 15 # int
season_type = 'regular' # str | Season type filter (optional) (default to regular)
team = 'team_example' # str | Team filter (optional)
offense = 'offense_example' # str | Offensive team filter (optional)
defense = 'defense_example' # str | Defensive team filter (optional)
conference = 'conference_example' # str | Conference filter (optional)
offense_conference = 'offense_conference_example' # str | Offensive conference filter (optional)
defense_conference = 'defense_conference_example' # str | Defensive conference filter (optional)
play_type = [59, 60, 18, 40, 41, 38, 61, 62, 43] # int

# Play types needed: 21 = Timeout, 59 = Field Goal Good, 60 = Field Goal Missed, 18 = Blocked Field Goal,
# 40 = Missed Field Goal Return, 41 = Missed Field Goal Return Touchdown, 38 = Blocked Field Goal Touchdown,
# 61 = Extra Point Good, 62 = Extra Point Missed, 43 = Blocked PAT


# Below used to pull play_type data
'''
try:
  # Play types
  api_response = api_instance.get_play_types()
  pprint(api_response)
except ApiException as e:
  print("Exception when calling PlaysApi->get_play_types: %s\n" % e)
'''


timeouts = {'away': [], 'clock': [], 'defense': [], 'defense_conference': [], 'defense_score': [],
'defense_timeouts': [], 'distance': [], 'down': [], 'drive_id': [], 'drive_number': [], 'game_id': [], 'home': [],
'id': [], 'offense': [], 'offense_conference': [], 'offense_score': [], 'offense_timeouts': [], 'period': [],
 'play_number': [], 'play_text': [], 'play_type': [], 'ppa': [], 'scoring': [], 'wallclock': [], 'yard_line': [],
'yards_gained': [], 'yards_to_goal': []}

kick_att = {'away': [], 'clock': [], 'defense': [], 'defense_conference': [], 'defense_score': [],
'defense_timeouts': [], 'distance': [], 'down': [], 'drive_id': [], 'drive_number': [], 'game_id': [], 'home': [],
'id': [], 'offense': [], 'offense_conference': [], 'offense_score': [], 'offense_timeouts': [], 'period': [],
 'play_number': [], 'play_text': [], 'play_type': [], 'ppa': [], 'scoring': [], 'wallclock': [], 'yard_line': [],
'yards_gained': [], 'yards_to_goal': []}


# Pull data for all timeouts called.
try:
    # Play by play data
    for year in range(start_year, end_year):
        for week in range(weeks):
            api_response = api_instance.get_plays(year=year, week=week, play_type=21)
            for response in api_response:
                for key in timeouts.keys():
                    timeouts[key].append(getattr(response, key))
except ApiException as e:
    print("Exception when calling PlaysApi->get_plays: %s\n" % e)

# Pull data for all field goal/extra points attempted
try:
    # Play by play data
    for year in range(start_year, end_year):
        for week in range(weeks):
            for plays in play_type:
                api_response = api_instance.get_plays(year=year, week=week, play_type=plays)
                for response in api_response:
                    for key in kick_att.keys():
                        kick_att[key].append(getattr(response, key))
except ApiException as e:
    print("Exception when calling PlaysApi->get_plays: %s\n" % e)



# Convert both data to csv for analysis
df_timeouts = pd.DataFrame(timeouts)
df_kick_att = pd.DataFrame(kick_att)
df_timeouts.to_csv('CFB_timeouts.csv', index=False)
df_kick_att.to_csv('CFB_kicking_attempt.csv', index=False)