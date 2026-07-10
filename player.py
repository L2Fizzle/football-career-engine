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
        self.career_length = 0

        self.pace = 0
        self.shooting = 0
        self.chance_per_shot = 0
        self.passing = 0
        self.dribbling = 0
        self.defending = 0
        self.strength = 0
        self.iq = 0
        self.playmaking_ability = 0

        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0
        self.match_passes = 0
        self.match_pass_accuracy = 0
        self.clean_sheet = 0
        self.match_rating = 6.0

        self.season_goals = 0
        self.season_assists = 0
        self.season_clean_sheets = 0
        self.season_rating = 0
        self.season_titles = 0

        self.career_goals = 0
        self.career_assists = 0
        self.career_clean_sheets = 0
        self.career_rating = 6.0
        self.prem_titles = 0


    def generate_attributes(self):

        self.position = random.choice(POSITIONS_LIST)

        self.age = random.randint(15,20)
        self.career_length = random.randint(15,25)

        self.pace = random.randint(1,10)
        self.shooting = random.randint(1,10)
        self.passing = random.randint(1,10)
        self.dribbling = random.randint(1,10)
        self.defending = random.randint(1,10)
        self.strength = random.randint(1,10)
        self.iq = random.randint(1,10)
        self.playmaking_ability = round((self.passing + self.iq)/2)

        self.chance_per_shot = self.shooting * 0.03

    def display_name(self):
        return self.name

    def display_age(self):
        return self.age

    def display_career_length(self):
        return self.career_length

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

    def increase_age(self):
        self.age += 1

    def clear_match_stats(self):
        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0
        self.match_passes = 0
        self.match_pass_accuracy = 0
        self.clean_sheet = 0
        self.match_rating = 6.0

    def clear_season_stats(self):
        self.season_goals = 0
        self.season_assists = 0
        self.season_rating = 6.0
        self.season_clean_sheets = 0
        self.season_titles = 0

    def shot_attempt(self,opponent_defense):
        chance = self.chance_per_shot
        chance *= (1 - (opponent_defense - 5) * 0.08) # allows opponent's defence level to affect how great the chance is

        #balances chance
        chance = max(0.02,chance)
        chance = min(0.45,chance)

        if chance >= random.random():
            self.match_goals += 1
            self.season_goals += 1
            self.career_goals += 1

    def key_pass(self, opponent_defense):
        assist_chance = round(self.passing - (opponent_defense / 2))

        odds_of_assisting = random.randint(10 - self.playmaking_ability, 10) #odds of assisting depends on player's playmaking ability stat

        if assist_chance >= odds_of_assisting:
            self.match_assists += 1

    def update_assists(self):
        self.season_assists += self.match_assists
        self.career_assists += self.match_assists

    def calculate_passes(self):
        if self.position in  ["ST", "CF", "LW", "RW"]:
            if self.passing <= 5:
                pass_attempts = random.randint(8,18)
            elif self.passing <= 7:
                pass_attempts = random.randint(15,27)
            else:
                pass_attempts = random.randint(25,40)

        elif self.position in  ["LM", "RM", "CAM", "CM", "CDM"]:
            if self.passing <= 5:
                pass_attempts = random.randint(15,30)
            elif self.passing <= 7:
                pass_attempts = random.randint(28,50)
            else:
                pass_attempts = random.randint(45,70)

        else:
            if self.passing <= 5:
                pass_attempts = random.randint(20,34)
            elif self.passing <= 7:
                pass_attempts = random.randint(30,54)
            else:
                pass_attempts = random.randint(50,80)

        if self.passing <= 5:
            accuracy = round(random.uniform(0.3,0.6),2)

        elif self.passing <= 7:
            accuracy = round(random.uniform(0.55,0.75),2)

        else:
            accuracy = round(random.uniform(0.7,0.95),2)

        self.match_passes = round(pass_attempts*accuracy)
        self.match_pass_accuracy = accuracy
    def dribble_attempt(self, opponent_defense):
        dribble_chance = self.dribbling - (opponent_defense / 2)

        successful_dribble_odds = random.randint(10 - self.dribbling, 10)

        if dribble_chance >= successful_dribble_odds:
            self.match_dribbles += 1

    def add_clean_sheet(self):
        self.clean_sheet += 1
        self.season_clean_sheets += 1
        self.career_clean_sheets += 1


    def calculate_match_rating(self):
        self.match_rating += self.match_goals
        self.match_rating += self.match_assists * 0.7
        self.match_rating += self.match_dribbles * 0.4
        self.match_rating += self.match_passes * 0.02
        self.match_rating += (self.match_pass_accuracy - 0.75)

        if self.position in ["CDM","LWB", "RWB","LB", "RB","CB"]:
            self.match_rating += self.clean_sheet


        if self.match_rating > 10:
            self.match_rating = 10.0
        self.season_rating += self.match_rating
        self.career_rating += self.match_rating

        return self.match_rating

    def calculate_season_rating(self):
        self.season_rating = round(self.season_rating/38,2)

    def premier_league_winner(self):
        self.prem_titles += 1
        self.season_titles = 1

    def change_player_stat(self,amount):
        attribute_list = ["pace", "shooting", "passing", "dribbling", "defending", "strength"]


        if all(getattr(self,attribute) == 10 for attribute in attribute_list): #checks if every attribute is maxxed out
            return None

        #ensures chosen stat is not maxxed out
        while True:
            changed_stat = random.choice(attribute_list)
            current = getattr(self,changed_stat) #gets attribute rating
            if current < 10:
                break

        current += amount #increments the attribute rating by certain amount
        if current > 10:
            current = 10
        setattr(self,changed_stat, current) #changes the attribute rating by certain amount
        return changed_stat

    def calculate_career_rating(self):
        average_career_rating = self.career_rating/(38*self.career_length)
        return average_career_rating







