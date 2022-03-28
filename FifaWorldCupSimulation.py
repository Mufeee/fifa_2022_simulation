import FifaSimulationObjects as fso
import pandas as pd
import numpy as np
'''
creating a list of dataframes to hold the results of the group stage
'''
def initation_groups_results_lists(wc_groups_list):
    wc_group_results_dict = {}
    for group in wc_groups_list:
        wc_group_results_dict[group.name] = pd.DataFrame(columns=['Team', 'GF', 'GA', 'GD', 'YC', 'RC', 'Points'])
    return wc_group_results_dict

'''
defines the groups and each team in the group according to the business rules and the pots. 
The group order matters as the matches list in the brackets will depend on the order
'''
def simulate_group_stage_draw(wc_num_groups, wc_finals_team_list):
    wc_groups_list = []
    for i in range(wc_num_groups):
        #####
        #Simulate the draw from wc_finals_team_list
        #####
        ####Remove the below code and write simulation code
        t1 = fso.Team("Egypt", 33, 68)
        t2 = fso.Team("Canada",30,72)
        t3 = fso.Team("Belgium",1,91)
        t4 = fso.Team("Japan",24,80)
        ####### End of simulation code
        g = fso.Group(i,[t1,t2,t3,t4])
        wc_groups_list.append(g)
    return wc_groups_list

'''
Create the matches and the order of the matches for the group stage
'''
def get_group_games(wc_groups_list):
    matches_list = []
    #order of the game 
    game_num = 1
    #################################################################
    # Code block below needs to be changed. 
    # The actual order should be decided by the business rules
    #################################################################
    for group in wc_groups_list:
        for team1 in group.teams:
            for team2 in group.teams:
                if team1 != team2:
                    matches_list.append(fso.Game(game_num,team1,team2,team1,True))
                    game_num += 1
    return matches_list

'''
Create the brackets after the group stage
'''
def get_bracket_games(group_stage_results,games):
    bracket_matches_list = []
    for i in range(int(games+1)):
        #################################################################
        # Code block below needs to be changed. 
        # The actual order should be decided by the business rules
        #################################################################
        t1 = fso.Team("Canada",30,72)
        t2 = fso.Team("Belgium",1,91)
        bracket_matches_list.append(fso.Game(i,t1,t2,t1,False))
    return bracket_matches_list 

'''
How many groups
Which group have which teams
The results list of dataframes
'''
def simulate_group_stage(wc_groups_list, games_list):
    #create the list that will hold the results of the group stage
    wc_group_results_dict = initation_groups_results_lists(wc_groups_list)
    #################################################################
    #Simulate the group stage
    #################################################################

    qualified_teams = get_group_qualified_teams(wc_group_results_dict)
    t = fso.Team("Egypt", 33, 68)

    return qualified_teams

def simulate_round16(previous_stage_results):
    get_bracket_games(previous_stage_results,games=8)
    #################################################################
    # Code block below needs to be changed. 
    # The actual order should be decided by the business rules
    #################################################################
    pass

def simulate_quarterfinals(previous_stage_results):
    #################################################################
    # Code block below needs to be changed. 
    # The actual order should be decided by the business rules
    #################################################################
    get_bracket_games(previous_stage_results,games=4)
    pass

def simulate_semifinals(previous_stage_results):
    #################################################################
    # Code block below needs to be changed. 
    # The actual order should be decided by the business rules
    #################################################################
    get_bracket_games(previous_stage_results,games=2)
    pass

def simulate_3rdplace(previous_stage_results):
    #################################################################
    # Code block below needs to be changed. 
    #################################################################
    winner = 'Germany'
    loser = 'France'
    return (winner,loser)

def simulate_finals(previous_stage_results):
    #################################################################
    # Code block below needs to be changed. 
    #################################################################
    winner = 'Argentina'
    loser = 'Belgium'
    return (winner,loser)

'''
Look at the group results and calculate the qualifying teams
'''
def get_group_qualified_teams(wc_group_results_list):
    #################################################################
    # Update to include tie breaking rules
    #################################################################
    group_winners = {}
    for group_name, group_results in wc_group_results_list.items():
        #group_results.sort_values(by=['Points'], ascending=False,inplace=True)
        #group_winners[group_name] = (group_results.Team.values[0], group_results.Team.values[1])
        t1 = fso.Team("Canada",30,72)
        t2 = fso.Team("Belgium",1,91)
        group_winners[group_name] = (t1,t2)
    #every group has a tuple of the (winner,2ndplace)
    return group_winners

def get_bracket_winners(game_results_list):
    winners = []
    for game_result in game_results_list:
        if game_result.get_game_result() == 1:
            winners.append(game_result.game.home_team)
        else: 
            winners.append(game_result.game.away_team)