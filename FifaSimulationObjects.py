#define Team class with ranking and strength properties
class Team:

    def __init__(self, name, ranking, total_strength, group, group_position):
        self.name = name
        self.ranking = ranking
        self.total_strength = total_strength
        self.group = group
        self.group_position = group_position
        #those variables are future extensions to extend the class for more complex predictions
        #self.region = None
        #self.attack_strength = 0
        #self.midfield_strength = 0
        #self.defence_strength = 0
        #self.team_form = 0
        #self.Roster = {}

    def get_confederation(self):
        confederation_dict = {'South Korea':'AFC','Japan':'AFC','Saudi Arabia':'AFC','Iran':'AFC','UAE':'AFC','Iraq':'AFC','Lebanon':'AFC',
        'Canada':'CONCACAF',
        'United States':'CONCACAF',
        'Mexico':'CONCACAF',
        'Costa Rica':'CONCACAF',
        'Panama':'CONCACAF',
        'Serbia':'UEFA',
        'Spain':'UEFA',
        'Switzerland':'UEFA',
        'France':'UEFA',
        'Belgium':'UEFA',
        'Denmark':'UEFA',
        'Netherlands':'UEFA',
        'Croatia':'UEFA',
        'England':'UEFA',
        'Germany':'UEFA',
        'Portugal':'UEFA',
        'Sweden':'UEFA',
        'Italy':'UEFA',
        'Ukraine':'UEFA',
        'Wales':'UEFA',
        'Turkey':'UEFA',
        'Russia':'UEFA',
        'Poland':'UEFA',
        'North Macedonia':'UEFA',
        'Brazil':'CONMEBOL',
        'Argentina':'CONMEBOL',
        'Ecuador':'CONMEBOL',
        'Uruguay':'CONMEBOL',
        'Peru':'CONMEBOL',
        'Colombia':'CONMEBOL',
        'Chile':'CONMEBOL',
        'Egypt':'CAF',
        'Senegal':'CAF',
        'Cameroon':'CAF',
        'Algeria':'CAF',
        'Ghana':'CAF',
        'Nigeria':'CAF',
        'DR Congo':'CAF',
        'Morocco':'CAF',
        'Tunisia':'CAF',
        'Mali':'CAF',
        'Australia':'OFC',
        'New Zealand':'OFC',
        'Tahiti':'OFC',
        'Solomon Islands':'OFC',
        'Papua New Guinea':'OFC'
        }

        return confederation_dict[self.name]


#define a Game class with 2 teams, home and away, home advantage and prediction
class Game:
    def __init__(self, game_number, home_team, away_team, home_advantage,is_group_stage):
        self.game_number = game_number
        self.home_team = home_team
        self.away_team = away_team
        self.home_advantage = home_advantage
        self.is_group_stage = is_group_stage
    
    def simulate(self):
        import numpy as np
        if self.is_group_stage:
            return GameResult(self,np.random.randint(0,5),np.random.randint(0,5),np.random.randint(0,5),np.random.randint(0,5),0,0)
        else:
            res = GameResult(self,np.random.randint(0,5),np.random.randint(0,5),np.random.randint(0,5),np.random.randint(0,5),0,0)
            ## Random code just to avoid draw for now if it is not a group stage game
            if res.home_goals == res.away_goals:
                res.home_goals += 1

class Player:
    def __init__(self, name, position, strength):
        self.name = name
        self.position = position
        self.strength = strength

'''
create a group object that holds 4 teams
'''        
class Group:
    def __init__(self, name, teams):
        self.name = name
        self.teams = teams
        
'''
create a game result object that holds the result and cards of the football game
'''
class GameResult:
    def __init__(self, game, home_goals, away_goals, home_yellow_cards, away_yellow_cards, home_red_cards, away_red_cards):
        self.game = game
        self.home_goals = home_goals
        self.away_goals = away_goals
        self.home_yellow_cards = home_yellow_cards
        self.away_yellow_cards = away_yellow_cards
        self.home_red_cards = home_red_cards
        self.away_red_cards = away_red_cards

    def get_game_result(self):
        if self.home_goals > self.away_goals:
            return 1
        elif self.home_goals < self.away_goals:
            return -1
        else:
            return 0
'''
Worldcup final results class that holds the final results of the world cup
'''
class WorldcupFinalResults:
    def __init__(self, winner, runner_up, third_place, fourth_place, quarter_finalists, r16s):
        self.winner = winner
        self.runner_up = runner_up
        self.third_place = third_place
        self.fourth_place = fourth_place
        self.quarter_finalists = quarter_finalists
        self.r16s = r16s