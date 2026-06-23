import random

POSITIONS_LIST = [
    "ST", "CF",
    "LW", "RW",
    "LM", "RM",
    "CAM", "CM", "CDM",
    "LWB", "RWB",
    "LB", "RB",
    "CB"]
class Player:

    def __init__(self,name):
        self.name = name

        self.position = ""

        self.age = 0
        self.pace = 0
        self.shooting = 0
        self.passing = 0
        self.dribbling = 0
        self.defending = 0
        self.strength = 0
        self.iq = 0
        self.playmaking_ability = 0

        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0
        self.match_rating = 6.0

        self.season_goals = 0
        self.season_assists = 0
        self.season_dribbles = 0

        self.career_goals = 0
        self.career_assists = 0
        self.career_rating = 6.0


    def generate_attributes(self):

        self.position = random.choice(POSITIONS_LIST)

        self.age = random.randint(15,20)
        self.pace = random.randint(1,10)
        self.shooting = random.randint(1,10)
        self.passing = random.randint(1,10)
        self.dribbling = random.randint(1,10)
        self.defending = random.randint(1,10)
        self.strength = random.randint(1,10)
        self.iq = random.randint(1,10)
        self.playmaking_ability = round((self.passing + self.iq)/2)

    def display_name(self):
        return self.name

    def display_age(self):
        return self.age

    def display_position(self):
        return self.position

    def display_pace(self):
        return self.pace

    def display_shooting(self):

        return self.shooting

    def display_passing(self):
        return self.passing

    def display_dribbling(self):
        return self.dribbling

    def display_defending(self):
        return self.defending

    def display_strength(self):
        return self.strength

    def display_iq(self):
        return self.iq

    def display_season_goals(self):
        return self.season_goals

    def display_season_assists(self):
        return self.season_assists

    def display_season_dribbles(self):
        return self.season_dribbles

    def display_match_goals(self):
        return self.match_goals

    def display_match_assists(self):
        return self.match_assists

    def display_match_dribbles(self):
        return self.match_dribbles

    def display_career_goals(self):
        return self.career_goals

    def display_career_assists(self):
        return self.career_assists

    def clear_match_stats(self):
        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0

    def clear_player_rating(self):
        self.match_rating = 6.0


    def shot_attempt(self,opponent_defense):
        goal_chance = self.shooting - (opponent_defense/2)

        odds_of_scoring = random.randint(10-self.shooting,10)

        if goal_chance >= odds_of_scoring:
            self.match_goals += 1
            self.season_goals += 1

    def key_pass(self, opponent_defense):
        assist_chance = round(self.passing - (opponent_defense / 2))

        odds_of_assisting = random.randint(10 - self.playmaking_ability, 10) #odds of assisting depends on player's playmaking ability stat

        if assist_chance >= odds_of_assisting:
            self.match_assists += 1
            self.season_assists += 1

    def dribble_attempt(self, opponent_defense):
        dribble_chance = self.dribbling - (opponent_defense / 2)

        successful_dribble_odds = random.randint(10 - self.dribbling, 10)

        if dribble_chance >= successful_dribble_odds:
            self.match_dribbles += 1
            self.season_dribbles += 1

    def calculate_match_rating(self):
        self.match_rating += self.match_goals
        self.match_rating += self.match_assists * 0.7
        self.match_rating += self.match_dribbles * 0.3
        if self.match_rating > 10:
            self.match_rating = 10.0

        return self.match_rating






