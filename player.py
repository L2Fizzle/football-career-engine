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
        self.season_dribbles = 0
        self.season_clean_sheets = 0
        self.season_rating = 0
        self.season_titles = 0



        self.transfer_value = 0 #transfer value in Millions
        #sets minimum and maximum value a club can offer
        self.min_value = 0
        self.max_value = 0

        self.career_goals = 0
        self.career_assists = 0
        self.career_clean_sheets = 0
        self.career_rating = 6.0
        self.prem_titles = 0

        self.highest_goals = 0 #highest goal season
        self.highest_assists = 0
        self.highest_value = 0


    def generate_attributes(self):
        """
        generates player attributes using random
        :return:
        """

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
        self.chance_per_created = self.playmaking_ability * 0.03 #chance of getting an assist per chance created

    def display_name(self):
        """
        displays player's name
        :return:
        """
        return self.name

    def display_age(self):
        """
        displays player age
        :return:
        """
        return self.age

    def display_career_length(self):
        """
        displays player career length
        :return:
        """
        return self.career_length

    def display_position(self):
        """
        displays player position
        :return:
        """
        return self.position

    def display_role(self):
        """
        displays player role based on position
        :return:
        """

        if self.position in ["LWB", "RWB", "LB", "RB", "CB"]:
            return "defender"
        elif self.position in ["LM", "RM", "CAM", "CM", "CDM"]:
            return "midfielder"
        else:
            return "attacker"

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
        self.season_dribbles = 0
        self.season_rating = 6.0
        self.season_clean_sheets = 0
        self.season_titles = 0
        self.transfer_value = 0
        self.min_value = 0
        self.max_value = 0

    def shot_attempt(self,opponent_defense,team_offence):
        chance = self.chance_per_shot

        modifier = 1
        modifier *= 1 - (opponent_defense - 5) * 0.08  # allows opponent's defence level to affect how great the chance is
        modifier *= 1 + (team_offence - 4) * 0.08

        chance *= modifier
        #balances chance
        chance = max(0.02,min(0.5,chance))

        if chance >= random.random():
            self.match_goals += 1
            self.season_goals += 1
            self.career_goals += 1

    def key_pass(self, opponent_defense,team_offence):
        assist_chance = self.chance_per_created

        modifier = 1
        # allows opponent defence level and team's attack level to affect the chance
        modifier *= 1 - (opponent_defense - 3.5) * 0.1
        modifier *= 1 + (team_offence/2 - 5) * 0.08
        assist_chance *= modifier

        # balances assist chance so it is not too extreme
        chance = max(0.01, min(0.17, assist_chance))

        if assist_chance >= random.random():
            self.match_assists += 1
            self.season_assists += 1
            self.career_assists += 1


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
            self.season_dribbles += 1

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
        attribute_list = ["pace", "shooting", "passing", "dribbling", "defending", "strength","iq"]


        if all(getattr(self,attribute) == 10 for attribute in attribute_list) and amount > 0: #checks if every attribute is maxxed out for upgrading
            return None

        if all(getattr(self,attribute) == 1 for attribute in attribute_list) and amount < 0: #checks if every attribute is minimum for downgrade
            return None


        #ensures chosen stat is not maxxed out for upgrade and not minimum for downgrade
        while True:
            changed_stat = random.choice(attribute_list)
            current = getattr(self,changed_stat) #gets attribute rating
            if amount > 0:
                if current < 10:
                    break
            elif amount < 0:
                if current > 1 :
                    break

        current += amount #increments the attribute rating by certain amount
        if current > 10:
            current = 10
            amount = 1

        if current < 1:
            current = 1
            amount = -1
        setattr(self,changed_stat, current) #changes the attribute rating by certain amount
        return changed_stat, amount

    def check_highest(self):
        """
        checks if any season stats are the user's highest
        :return: None: adjusts attributes
        """
        if self.season_goals > self.highest_goals:
            self.highest_goals = self.season_goals

        if self.season_assists > self.highest_assists:
            self.highest_assists = self.season_assists

        if self.transfer_value > self.highest_value:
            self.highest_value = self.transfer_value

    def calculate_transfer_value(self):
        """
        calculates player transfer value based on season stats and role
        :return: min_value: minimum possible value offered that would be looked at
        :return: max_value: maximum transfer value of player
        """
        min_value = 0
        max_value = 0
        if self.season_rating >= 8.5:
            min_value += 100000000
        elif self.season_rating >= 8.0:
            min_value += 70000000
        elif self.season_rating >= 7.5:
            min_value += 50000000
        elif self.season_rating >= 7.0:
            min_value += 30000000
        else:
            min_value += 10000000

        max_value += min_value
        if self.display_role() == "attacker":
            max_value += self.season_goals * 2000000
            max_value += self.season_assists * 1000000
            max_value += self.season_dribbles * 500000
        elif self.display_role() == "midfielder":
            max_value += self.season_goals * 2000000
            max_value += self.season_assists * 2000000
            max_value += self.season_dribbles * 500000
        elif self.display_role() == "defender":
            max_value += self.season_goals * 2000000
            max_value += self.season_assists * 2000000
            max_value += self.season_clean_sheets * 2000000

        self.transfer_value = (min_value + max_value) /2000000

        self.min_value, self.max_value = min_value, max_value



    def calculate_career_rating(self):
        average_career_rating = self.career_rating/(38*self.career_length)
        return average_career_rating







