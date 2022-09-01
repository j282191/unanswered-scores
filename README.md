# unanswered-scores
Python script to calculate "unanswered scores" in a football game.




A friend of mine goes by @EdTeach23 and he gets into some interesting sports betting.

He asked me about the probability of there being 2, 3, or 4 "Unanswered Scores" in an upcoming Football game.  I threw this simulation together to answer the question.

Given data from EdTeach:

* KC: 9.49 Possessions, 5.15 Scores, 3.44 Punts, 0.9 Turnovers
* TB: 10.03 Possessions, 4.75 Scores, 3.89 Punts, 1.39 Turnovers

* Note: 30 minutes in a half. 1800 seconds.
* 60 minutes total, 3600 seconds.
* Simulation does not account for overtime.


Assumption/derivation: Total possessions (by either team) 9.49+10.03 =  19.52

Average time of possession (by either team) 3600/19.52 = 184.43 (seconds)

This is a simple conclusion based on the stats provided.  

This may be improved with better stats on duration of possession.


We have the average, but we need the variance of the distribution.

I have to just totally make this up, so I'm going with a standard deviation of 60 seconds.  That doesn't seem too unreasonable; 2/3 of all drives between 2 minutes and 4 minutes.