#define Team class with ranking and strength properties
class Team:

    def __init__(self, name, ranking, total_strength):
        self.name = name
        self.ranking = ranking
        self.total_strength = total_strength
        #those variables are future extensions to extend the class for more complex predictions
        self.region = None
        self.attack_strength = 0
        self.midfield_strength = 0
        self.defence_strength = 0
        self.team_form = 0
        self.Roster = {}

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
    def __init__(self, home_team, away_team, home_advantage):
        self.home_team = home_team
        self.away_team = away_team
        self.home_advantage = home_advantage
    
    def simulate():
        pass


class Player:
    def __init__(self, name, position, strength):
        self.name = name
        self.position = position
        self.strength = strength

'''
create a group object that holds 4 teams
'''        
class Group:
    def __init__(self, group_name, teams):
        self.group_name = group_name
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