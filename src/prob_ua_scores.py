#Copyright 2021 John Penuel. All rights reserved.
import numpy as np



mu = 184.43 #seconds
sd = 60.0 #seconds

#For the purposes of simulation, if the drive concludes after the 30 minute timer for the half, there is no score.  Simulation does not account for strategic behavior such as taking a knee or longshot passes.

#For the purposes of simulation, do not distinguish between a turnover and a punt... basically just a non-scoring drive.
probability_score = [ 5.15/9.49 , 4.75/10.03 ]


np.random.seed(17)#Fix the random seed for consistent results.
num_simulations = 50000

results_2ua_scores = np.zeros(num_simulations)
results_3ua_scores = np.zeros(num_simulations)
results_4ua_scores = np.zeros(num_simulations)

for simulation in range(num_simulations):
    if (simulation % 100)==0:
        print("running simulation ",simulation,"/",num_simulations)
    clock = 0.0#reset at beginning of game
    possession_scores = []
    possession_times = []
    token = np.random.randint(2)#coin flip at beginning of game.. result is 0 or 1
    while clock < 3600:
        t = [0,0]
        s = [0,0]
        t[token] = max(0,np.random.normal(mu,sd))
        if clock < 1800:#clock runs out, no score on drive
            if clock + t[token] > 1800:
                t[token] = 1800 - clock
                clock = 1800
            else:
                clock = clock + t[token]
                u = np.random.rand()
                if u < probability_score[token]:#probablistically score
                    s[token] = 1
        else:#we are past halftime...
            if clock + t[token] > 3600:#clock runs out, no score on drive.
                t[token] = 3600 - clock
                clock = 3600
            else:
                clock = clock + t[token]
                u = np.random.rand()
                if u < probability_score[token]:#probablistically score
                    s[token] = 1
        possession_times.append(t)
        possession_scores.append(s)
        token = (token + 1) % 2#change possession
    unanswered_score_count = 1
    score_token = -1
    for p in range(len(possession_times)):
        s = possession_scores[p]
        if sum(s):
            if score_token == -1:#first score of the game
                if s[0]:
                    score_token = 0
                else:
                    score_token = 1
            else:#not the first score of the game
                if s[0]:
                    next_score_token = 0
                else:
                    next_score_token = 1
                if next_score_token == score_token:
                    unanswered_score_count = unanswered_score_count + 1
                    if unanswered_score_count >= 2:
                        results_2ua_scores[simulation] = 1
                        if unanswered_score_count >= 3:
                            results_3ua_scores[simulation] = 1
                            if unanswered_score_count >= 4:
                                results_4ua_scores[simulation] = 1
                else:
                    unanswered_score_count = 1#reset
                    score_token = next_score_token
                    
                
                

print("Results:")
print("Probability there are 2x unanswered scores:",sum(results_2ua_scores)/num_simulations)
print("Probability there are 3x unanswered scores:",sum(results_3ua_scores)/num_simulations)
print("Probability there are 4x unanswered scores:",sum(results_4ua_scores)/num_simulations)


#Hopefully he can find the tickets with positive expected value given the calculated probabilities.
