import numpy as np
stepsize = 100


class Team:
    def __init__(self, posession=.5, hits=.1, team_name='teamx'):
        # Initialization of team
        self.posession = posession
        self.hits = hits
        self.team_name = team_name



def monte_carlo_run(team1, team2):
    posession_team = 0
    goals = [0, 0]
    for i in range(0,90):
        #print('Simulating one minute of game')
        rand = np.random.random()
        chance = np.random.random()
        # chance to switch posession
        if chance < .5:
            if rand < team1.posession:
                posession_team = 0
        else: 
            if rand < team2.posession:
                posession_team = 1
        # chance to hit goal:
        rand = np.random.random()
        chance = np.random.random()
        if chance < .5:
            if rand < [team1.hits, team2.hits][posession_team]:
                goals[posession_team] += 1
    return goals


def simulate(nrOfRuns, team1, team2):
    results = []
    for i in range(nrOfRuns):
        [res1, res2] = monte_carlo_run(team1, team2)
        results.append([res1, res2])
        if not i % stepsize:
            print('Monte Carlo run: {}%; team1: {}, team2: {}'.format(i/nrOfRuns, res1, res2))
    results = np.array(results)
    mean = results.mean(axis=0)
    print('The prediction made by Monte-Carlo is {} - {}'.format(round(mean[0])\
          , round(mean[1])))
    return results, results.mean(axis=0), np.std(results, axis=0)



def ask_user():
    team_name = input("Enter Team_name:")
    hits = float(input("Enter Hit Percentage of"+team_name))
    posession = float(input("Enter Posession of"+team_name))
    return Team(hits,posession, team_name)

def menu():
    print("First Team:")
    team_1 = ask_user()
    print("Second Team:")
    team_2 = ask_user()
    runs = int(input("Enter Number of Runs:"))
    (result,mean,std) = simulate(runs,team_1,team_2)
    print(result)
    print(mean)
    print(std)
    
menu()