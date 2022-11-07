#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:00:35 2022

@author: deji
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

sns.set()

pd.options.display.max_columns = None


team_21 = pd.read_csv('nba-team-stats21.csv')
team_20 = pd.read_csv('nba-team-stats20.csv')
team_19 = pd.read_csv('nba-team-stats19.csv')
team_18 = pd.read_csv('nba-team-stats18.csv')
team_17 = pd.read_csv('nba-team-stats17.csv')

player_21 = pd.read_csv('nba-stats21.csv')
player_20 = pd.read_csv('nba-stats20.csv')
player_19 = pd.read_csv('nba-stats19.csv')
player_18 = pd.read_csv('nba-stats18.csv')
player_17 = pd.read_csv('nba-stats17.csv')


player_stats_list = [player_21, player_20, player_19, player_18, player_17]
team_stats_list = [team_21, team_20, team_19, team_18, team_17]


year = 21
for i in player_stats_list:
    i['Year'] = year
    year -= 1

year = 21 
for i in team_stats_list:
    i['Year'] = year
    year -= 1


player_data = pd.concat([player_21, player_20, player_19, player_18, player_17])
player_data = player_data.reset_index()
player_data.drop(columns=['Unnamed: 24', 'Unnamed: 19', 'Player-additional'], inplace=True)
player_data = player_data[player_data.Tm != 'TOT']

team_data = pd.concat([team_21, team_20, team_19, team_18, team_17])
team_data = team_data.reset_index()


final_df = team_data.copy()
final_df = final_df.drop(columns=['Rk', 'Conf', 'Div', 'L', 'W/L%', 'MOV', 'ORtg', 'DRtg','NRtg', 'MOV/A', 'NRtg/A'])


keys = final_df.Team.unique()
values = player_data.Tm.unique()
values = [tm.replace('CHO', 'CHA') for tm in values]

keys.sort()
values.sort()

remap_teams = dict(zip(keys, values))

final_df['Team'] = final_df['Team'].map(remap_teams)



needed_stats = player_data[['Tm', 'Player', 'MP', 'PER', 'USG%', 'VORP', 'Year']]


def get_top_player_stats(data):
    df_list = []
    adv_stats = {team:{21: 0.0, 20: 0.0, 19: 0.0, 18: 0.0, 17: 0.0} for team in player_data['Tm']}
    
    for team in adv_stats:
        df = data[data['Tm']==team][['Tm', 'MP', 'PER', 'USG%', 'VORP', 'Year', 'Player']]
        df = df[df['MP'] >= 1200]
        df_list.append(df)
        
    return df_list


player_data_ready = get_top_player_stats(needed_stats)

final_player = pd.DataFrame(columns=['Tm', 'Player', 'MP', 'PER', 'VORP', 'Year'])
for df in player_data_ready:
    i = 1
    while i < 6:
        minutes, per, vorp = 0, 0, 0
        max_x = df['USG%'].max()
        max_index = df['USG%'].idxmax()
        team = df.loc[max_index]['Tm']
        player = df.loc[max_index]['Player']
        year = df.loc[max_index]['Year']
        minutes = df.loc[max_index]['MP']
        per = df.loc[max_index]['PER']
        vorp = df.loc[max_index]['VORP']

        df = df[df['Year'] != year]
        final_player = final_player.append({'Tm' : team, 'Player': player, 'MP': minutes, 'PER': per, 'VORP': vorp, 'Year': year}, ignore_index =True)
        i += 1
    
    
    
    
final_player = final_player.rename(columns={'Tm':'Team'})
keys = player_data.Tm.unique()
remap_teams = dict(zip(keys, values))
remap_teams['CHI'] = 'CHI'
remap_teams['CHO'] = 'CHA'


final_player['Team'] = final_player['Team'].map(remap_teams)

nba_data = pd.merge(final_player, final_df, on=['Team', 'Year'])
nba_data = nba_data.loc[:, nba_data.columns != 'index']
    
   
    
y = nba_data['W']
x = nba_data[['MP', 'VORP', 'PER', 'ORtg/A', 'DRtg/A']]
  
scaler = StandardScaler()
scaler.fit(x)
scaled_inputs = scaler.transform(x)  

x_train, x_test, y_train, y_test = train_test_split(scaled_inputs, y, test_size=0.2, random_state=20)
    
reg = LinearRegression()
scores = cross_val_score(reg, x_train, y_train, scoring='r2', cv=5)

reg.fit(x_train, y_train)
y_hat = reg.predict(x_train)

reg_summary = pd.DataFrame(x.columns.values, columns=['Features'])
reg_summary['Weights'] = reg.coef_


plt.scatter(y_train, y_hat)
plt.xlabel('Wins', size=10)
plt.ylabel('Predicted Wins', size=10)
plt.show()
    
sns.distplot(y_train - y_hat)
  


  
y_hat_test = reg.predict(x_test)

plt.scatter(y_test, y_hat_test)
plt.xlabel('Wins', size=10)
plt.ylabel('Predicted Wins', size=10)
plt.show()

sns.distplot(y_test - y_hat_test)
    
    

reg_test_summary = pd.DataFrame(y_hat_test, columns=['Predicted Wins'])
y_test = y_test.reset_index(drop=True)
reg_test_summary['Target'] = y_test
reg_test_summary['Residual'] = reg_test_summary['Target'] - reg_test_summary['Predicted Wins']
reg_test_summary['Difference in %'] = np.absolute(reg_test_summary['Residual'] / reg_test_summary['Target']*100)

    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
