import random
class Player:

    def __init__(self,name):
        self.name = name
        self.age = 18
        self.shooting = 60
        self.passing = 60
        self.dribbling = 60

        self.season_goals = 0
        self.season_assists = 0
        self.season_dribbles = 0

        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0
        self.match_rating = 6.0

        self.skill_points = 0

    def display_name(self):
        return self.name

    def display_age(self):
        return self.age

    def display_shooting(self):
        return self.shooting

    def display_passing(self):
        return self.passing

    def display_dribbling(self):
        return self.dribbling

    def display_season_goals(self):
        return self.season_goals

    def display_season_assists(self):
        return self.season_assists

    def display_match_goals(self):
        return self.match_goals

    def display_match_assists(self):
        return self.match_assists

    def clear_match_stats(self):
        self.match_goals = 0
        self.match_assists = 0
        self.match_dribbles = 0

    def display_skill_points(self):
        return self.skill_points

    def skill_point_collection(self,points):
        self.skill_points += points

    def remove_skill_point(self):
        self.skill_points -= 1

    def clear_points(self):
        self.skill_points = 0


    def clear_player_rating(self):
        self.match_rating = 6.0


    def update_stats(self,choice):
        if choice.lower() == "p":
            self.passing += 5
        elif choice.lower == "s":
            self.shooting += 5
        elif choice.lower == "d":
            self.dribbling += 5
        else:
            return None
        return 1

    def shot_attempt(self,opponent_defense):
        goal_chance = self.shooting - (opponent_defense/2)

        odds_of_scoring = random.randint(1,100)

        if goal_chance >= odds_of_scoring:
            self.match_goals += 1
            self.season_goals += 1

    def key_pass(self, opponent_defense):
        assist_chance = self.passing - (opponent_defense / 2)

        odds_of_assisting = random.randint(1, 100)

        if assist_chance >= odds_of_assisting:
            self.match_assists += 1
            self.season_assists += 1

    def dribble_attempt(self, opponent_defense):
        dribble_chance = self.passing - (opponent_defense / 2)

        successful_dribble_odds = random.randint(1, 100)

        if dribble_chance >= successful_dribble_odds:
            self.match_dribbles += 1
            self.season_dribbles += 1

    def calculate_match_rating(self):
        self.match_rating += self.match_goals
        self.match_rating += self.match_assists * 0.7
        self.match_rating += self.match_dribbles * 0.3

        return self.match_rating






