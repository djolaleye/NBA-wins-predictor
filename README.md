## Predict total wins on the season for an NBA team
The goal of this project is an initial attempt to examine the impact of a star player on an NBA team's regular season performance. To try and capture this, a multiple linear regression can be created featuring the Minutes Played (MP), Value Over Replacement-level Player (VORP), & Player Efficiency Rating (PER) of each team's best player (determined by highest Usage%), along with each team's adusted offensive & defensive ratings. If the common school of thought - that the team goes as their key player goes - the trained model should weigh that player's stats more heavily than the team stats. 

### Conclusion
The model is a decent predictor of total wins on a season, with 76.7% of predictions falling within 5 wins of the actual total (cross val score = 85.4%). Distribution & scatter plots show that the model often overshoots the actual win total, and is better at preddicting high win totals than low ones.  

<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/nba_dist.png?raw=true" width=300 align=left>
<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/Tr_wins.png?raw=true" width=300 align=center>
<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/Ts_wins.png?raw=true" width=300 align=center>  



<br> Features: MP, VORP, PER, ORtg/A, DRtg/A  
Weights: 0.54, 0.50, -0.82, 7.95, -7.28  
  
From this summary , we see that the overall offensive and defensive proficiency of a team have a far greater effect on wins than the value brought by one star player on their own.


The main drawback of this analysis is the inherent collinearity between a star player's performance on the court and the team's offensive/defensive ratings. Future iterations of this project could improve on this by using better metrics to isolate a star player's performance and availability compared to the team's value when that player is not on the court. The model could further be improved by accounting for 2nd and 3rd 'star' quality players. Other worthwile alternatives of this project would be to have a playoff-centric version, as well as a team-specific version involving certain lineup combinations.
