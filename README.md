## Predict total wins on the season for an NBA team
The goal of this project is an initial attempt to examine the impact of a star player on an NBA team's regular season performance. I decided to try utilizing multiple linear regression to analyze this relationship. Important features to include were the Minutes Played (MP), Value Over Replacement-level Player (VORP), & Player Efficiency Rating (PER) of each team's best player (which was determined based on highest Usage%), along with each team's adusted offensive & defensive ratings. If the common school of thought - that the team goes as their key player goes - the trained model should reflect a heavier influence from the star player's stats compared to the overall team stats. 

## Training 
The chosen sample set included all season stats from the 2017-18 through 2021-2022 seasons. Features were limited to the chosen 5 to limit collinearity from other descriptors of performance and avoid overfitting to patterns due to many predictors vs a smaller data sample.  

### Conclusion
The model is a decent predictor of total wins on a season, with 76.7% of predictions falling within 5 wins of the actual total (cross val score = 85.4%). Distribution & scatter plots show that the model often overshoots the actual win total, and is better at predicting high win totals than low ones.  

<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/nba_dist.png?raw=true" width=300 align=left>
<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/Tr_wins.png?raw=true" width=300 align=center>
<img src="https://github.com/djolaleye/NBA-wins-predictor/blob/main/Data_vis/Ts_wins.png?raw=true" width=300 align=center>  



<br> Features: MP, VORP, PER, ORtg/A, DRtg/A  
Weights: 0.54, 0.50, -0.82, 7.95, -7.28  
  
From this summary, we see that the overall offensive and defensive proficiency of a team have a far greater effect on wins than the value brought by one star player on their own, failing to reject the null hypotheis.


The main drawback of this analysis is the inherent collinearity between a star player's performance on the court and the team's offensive/defensive ratings. Future iterations of this project could improve on this by using better game-by-game metrics to isolate a star player's performance and availability compared to their team's performance when that player is not on the court. This change's impact would be twofold, as it would also increase our sample size and improve our ability to generalize results. The model could also further be improved by accounting for a 2nd or 3rd 'star' quality player(s). 
