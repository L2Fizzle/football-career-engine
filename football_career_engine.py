import math
import random
import time

from player import Player
from Prem_table import points_calculation
from Prem_table import prem_table
from Prem_table import display_table


def enter_information(team_name):
    while True:
        player_name = input("Enter your player's name: ").strip()

        if player_name == "":
            print("Name cannot be empty. Try again.")
        else:
            break

    player = Player(player_name)
    print(f"\nWelcome {player.display_name()}!")
    time.sleep(1)
    print(f"Here are your current attributes:\n")
    time.sleep(1)
    player.generate_attributes()
    show_initial_stats(player,team_name)

    return player,player.display_career_length()


def choose_user_team(teams):
    user_team = teams[19]

    return user_team

def show_initial_stats(player,team_name):
    """
    Shows stats of player at the beginning of career
    :param player: user's player
    :param team_name: name of user's team
    :return: None: prints attributes and descriptions
    """
    #desc = description
    player.stat_description()
    non_desc_attributes = [("Starting Age", player.display_age()),
             ("Career Length", player.display_career_length()),
             ("Team", team_name),("Position", player.display_position())]

    attributes_with_desc = [("Height", player.display_height(),player.height_desc),
             ("Pace", player.display_pace(), player.pace_desc),
             ("Shooting", player.display_shooting(),player.shooting_desc),
             ("Passing", player.display_passing(),player.passing_desc),
             ("Dribbling", player.display_dribbling(),player.dribbling_desc),
             ("Defending", player.display_defending(),player.defending_desc),
             ("Strength", player.display_strength(),player.strength_desc),
             ("Football IQ", player.display_iq(),player.iq_desc)
             ]


    print("Generating player...")
    time.sleep(2)

    for attribute, value in non_desc_attributes:

        if attribute != "Career Length":
            print(f"{str(attribute) + ":":<15}", end="")
            time.sleep(1)
            print(f"{value}")
            time.sleep(1)
        else:
            print(f"{str(attribute) + ":":<15}", end="")
            time.sleep(1)
            print(f"{value} years")
            time.sleep(1)
    print()


    for attribute,value,description in attributes_with_desc:
        if attribute != "Height":
            print(f"{str(attribute) + ":": <15}", end="")
            time.sleep(1)
            print(f"{value:<20}",end="")
            time.sleep(1)
            print(description)
            time.sleep(1)
        else:
            print(f"{str(attribute) + ":":<15}",end="")
            time.sleep(1)
            print(f"{str(value) + "cm":<20}",end="")
            time.sleep(1)
            print(description)
            time.sleep(1)


def show_stats(player):
    """
    Shows stats after every few seasons
    :param player: the user's player
    :return: None: prints attributes and description
    """
    player.stat_description()
    attributes_with_desc = [
             ("Pace", player.display_pace(), player.pace_desc),
             ("Shooting", player.display_shooting(),player.shooting_desc),
             ("Passing", player.display_passing(),player.passing_desc),
             ("Dribbling", player.display_dribbling(),player.dribbling_desc),
             ("Defending", player.display_defending(),player.defending_desc),
             ("Strength", player.display_strength(),player.strength_desc),
             ("Football IQ", player.display_iq(),player.iq_desc)
             ]

    for attribute, value, description in attributes_with_desc:
        print(f"{str(attribute) + ":":<15}", end="")
        time.sleep(0.5)
        print(f"{value:<20}",end="")
        time.sleep(0.5)
        print(description)
        time.sleep(0.5)


def get_league_data(filename):
    prem_teams = [] #teams in premier league
    efl_teams = [] #teams in english 2nd division
    with open(filename, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")

            team = {"name":parts[0],
                    "attack":float(parts[1]),
                    "defense":float(parts[2]),
                    "consistency":float(parts[3]),
                    "min_points":float(parts[4]),
                    "max_points":float(parts[5]),"league":str(parts[6])}
            if team["league"] == "prem":
                prem_teams.append(team)
            else:
                efl_teams.append(team)
    return prem_teams,efl_teams


def matchday_team(teams, teams_played):
    team = random.choice(teams)
    teams.remove(team)
    teams_played.append(team)
    return team

def matchday_rating(team_attack, team_defense, consistency):
    form = round(random.uniform(-consistency, consistency),1)
    team_attack += form
    team_defense += form
    if team_attack >= 9.9:
        team_attack = 9.9
    if team_defense >= 9.9:
        team_defense = 9.9
    return team_attack, team_defense

def attack_chance(team_goals, team_attack, opponent_defense):
    if team_goals <= 3:
        goal_chance = team_attack - (opponent_defense / 2.5)

        odds_of_scoring = random.randint(round(10 - team_attack/0.8), 10)

    elif team_goals <= 5:
        goal_chance = (team_attack - opponent_defense/1.25)

        odds_of_scoring = random.randint(round((10 - team_attack/1.8)),10)
    else:
        goal_chance = (team_attack - opponent_defense)

        odds_of_scoring = random.randint(round((10 - team_attack / 2)), 10)


    if goal_chance >= odds_of_scoring:
        team_goals += 1

    return team_goals

def display_player_match(player):
    """
    Displays players match results
    :param player: the users player
    :return: None: prints results.
    """
    print(f"{player.name} match stats:")
    print(f"{player.match_goals} Goals,  {player.match_assists} Assists,  "
          f"{player.match_dribbles} successful dribbles")
    print(f"{player.match_passes} passes completed with {player.match_pass_accuracy:.0%} accuracy")
    if player.display_position() in ["CDM","LWB", "RWB", "LB", "RB","CB"] and player.clean_sheet == 1:
        print(f"Clean Sheet")

    player_rating = player.calculate_match_rating()
    print(f"Final match rating: {player_rating:.1f}")

    player.clear_match_stats()

def generate_events(user_shots, team_chances,user_passes):
    """
    generates a list of events to allow for a different number of team and user goals every game
    :param user_shots: the number of shots taken by the user
    :param team_chances: the number of chances for the team
    :param user_passes: the amount of user key passes that can result in goals (or assists for the user)
    :return: events: randomized list of the order of events
    """

    events = []

    for index in range(team_chances):
        events.append("Team")
    for index in range(user_shots):
        events.append("Player")
    for index in range(user_passes):
        events.append("Chance")

    random.shuffle(events)
    return events

def check_clean_sheet(player,opponent_goals):
    """
    checks if a clean sheet was earned
    :param player: users player
    :param opponent_goals: the amount of goals the opponent scored
    :return: None: adds clean sheet to the player's results
    """
    if opponent_goals == 0:
        player.add_clean_sheet()


def match(player, team_name, team_attack, team_defense, opponent_name, opponent_attack, opponent_defense):
    """
    Simulates an entire match
    :param player: the users player
    :param team_name: name of users team
    :param team_attack: attack rating of user team
    :param team_defense: defense rating of user team
    :param opponent_name: name of opponent team
    :param opponent_attack: attack rating of opponent
    :param opponent_defense: defense rating of opponent
    :return: points gained: number of points gained from the match
    :return: goal difference: goal difference of the match
    """

    team_goals = 0
    opponent_goals = 0

    user_shot_attempts = random.randint(0,int(team_attack/2)) #makes shooting opportunities based on team's attacking threat
    user_key_pass_attempts = random.randint(0,math.ceil(int(player.playmaking_ability/2)))
    dribble_attempts = random.randint(0,int(player.dribbling/2))

    team_chances = random.randint(round(team_attack/2.5),round(team_attack/1.5)) #team chances (excluding user chances)

    events = generate_events(user_shot_attempts, team_chances,user_key_pass_attempts)

    for chance in range(len(events)):
        if events[chance] == "Team":
            team_goals = attack_chance(team_goals, team_attack, opponent_defense)
        elif events[chance] == "Player":
            player_goals = player.match_goals
            player.shot_attempt(opponent_defense,team_attack)
            if player_goals < player.match_goals:
                team_goals += 1
        else:
            player_assists = player.match_assists
            player.key_pass(opponent_defense, team_attack)
            if player_assists < player.match_assists:
                team_goals += 1

    for dribble in range(dribble_attempts):
        player.dribble_attempt(opponent_defense)


    opponent_chances = random.randint(round(opponent_attack/2.5),round(opponent_attack/1.5)) #opponent chances

    for chance in range(opponent_chances):
        opponent_goals = attack_chance(opponent_goals, opponent_attack, team_defense)


    player.calculate_passes()

    print(f"\nScore: {team_name}  {team_goals} - {opponent_goals}  {opponent_name}\n")

    goal_difference = team_goals - opponent_goals

    check_clean_sheet(player, opponent_goals)

    display_player_match(player)

    if team_goals > opponent_goals:
        points_gained = 3
    elif team_goals == opponent_goals:
        points_gained = 1
    else:
        points_gained = 0

    return points_gained,goal_difference

def simulation_speed():
    while True:
        sim_type = input("\nWould you like a quick sim or slow sim for this season? (type q for quick and s for slow): ")
        if sim_type.lower() == "q":
            sim_speed = 0
            return sim_speed
        elif sim_type.lower() == "s":
            sim_speed = 5
            return sim_speed
        else:
            print("Please type either q or s")

def season_table(teams, user_team,user_team_points,user_team_gd):
    teams_and_points = []
    for prem_team in teams:
        min_points = prem_team["min_points"]
        max_points = prem_team["max_points"]
        team_points, team_goal_difference = points_calculation(min_points,max_points)
        teams_and_points.append({"name": prem_team["name"], "points": team_points, "goal_difference": team_goal_difference})
    teams_and_points.append({"name": f"{user_team["name"]}", "points": user_team_points, "goal_difference": user_team_gd})

    prem_table(teams_and_points)
    return teams_and_points

def player_season(player):
    """
    prints player's end of season stats
    :param player:
    :return:
    """
    print("⚽" * 50)
    print("END OF SEASON STATS".center(100, " "))
    print("⚽" * 50)
    print()

    print(f"{player.name}".center(100, " "))
    print(f"⚽Season Goals: {player.season_goals}⚽".center(100, " "))
    print(f"🎯Season Assists: {player.season_assists}🎯".center(100, " "))
    print(f"💪Clean Sheets: {player.season_clean_sheets}💪".center(99, " "))

    player.calculate_season_rating()

    print(f"📋Average Rating: {player.season_rating:.1f}📋".center(100, " "))

def team_lookup(teams):
    """
    returns full lookup for prem teams
    :param teams: full list of teams
    :return: full info of team
    """
    return {team["name"]:team for team in teams}

def get_relegated_info(teams,relegated_teams):
    lookup = team_lookup(teams)
    full_info = []
    for team in relegated_teams:
        full_info.append(lookup[team])
    return full_info


def simulate_season(full_teams,player,user_team):

    all_teams = full_teams.copy()
    sim_speed = simulation_speed()

    teams_played_once = []
    teams_played_twice = []
    team_name, team_attack, team_defense, team_consistency = (user_team["name"], user_team["attack"],
                                                             user_team["defense"], user_team["consistency"])

    matchday = 1
    team_points = 0
    team_gd = 0 #gd = goal difference
    team_wins = 0
    team_draws = 0
    team_losses = 0
    while all_teams:
        opponent = matchday_team(all_teams, teams_played_once)
        opponent_name, opponent_attack, opponent_defense, opponent_consistency = (opponent["name"],
                                                                                                       opponent["attack"],
                                                                                                       opponent["defense"],
                                                                                                       opponent["consistency"])

        opponent_attack, opponent_defense = matchday_rating(opponent_attack, opponent_defense, opponent_consistency)
        team_attack, team_defense = matchday_rating(team_attack, team_defense, team_consistency)

        print("⚽" * 20)
        print(f"\nMatchday {matchday}")
        print(f"\nOpponent: {opponent_name}")
        match_and_points, goal_difference = match(player, team_name, team_attack, team_defense,
              opponent_name, opponent_attack, opponent_defense)
        if match_and_points == 3:
            print(f"3 points earned by {team_name}")
            team_wins += 1
        elif match_and_points == 1:
            print(f"1 point earned by {team_name}")
            team_draws += 1
        else:
            print(f"0 points earned by {team_name}")
            team_losses += 1
        team_points += match_and_points
        team_gd += goal_difference
        matchday += 1
        print()
        team_attack, team_defense = user_team["attack"], user_team["defense"]
        time.sleep(sim_speed)

    while teams_played_once:
        opponent = matchday_team(teams_played_once, teams_played_twice)
        opponent_name, opponent_attack, opponent_defense, opponent_consistency = (opponent["name"],
                                                                                 opponent["attack"],
                                                                                 opponent["defense"],
                                                                                 opponent["consistency"])
        opponent_attack, opponent_defense = matchday_rating(opponent_attack, opponent_defense, opponent_consistency)
        team_attack, team_defense = matchday_rating(team_attack, team_defense, team_consistency)

        print("⚽" * 20)
        print(f"\nMatchday {matchday}")
        print(f"\nOpponent: {opponent_name}")
        match_and_points, goal_difference = match(player, team_name, team_attack, team_defense,
                                 opponent_name, opponent_attack, opponent_defense)
        if match_and_points == 3:
            print(f"3 points earned by {team_name}")
            team_wins += 1
        elif match_and_points == 1:
            print(f"1 point earned by {team_name}")
            team_draws += 1
        else:
            print(f"0 points earned by {team_name}")
            team_losses += 1

        team_points += match_and_points
        team_gd += goal_difference

        matchday += 1
        print()
        team_attack, team_defense = user_team["attack"], user_team["defense"]
        time.sleep(sim_speed)

    player_season(player)

    print(f"{team_name} Record: {team_wins}W {team_draws}D {team_losses}L".center(102, " "))
    print(f"{team_name} finishes the season with {team_points} points".center(100, " "))

    print()
    print("🦁"*50)
    print("Season Table".center(100," "))
    print("🦁"*50)
    table = season_table(teams_played_twice,user_team,team_points,team_gd)
    winner = table[0]["name"]
    if winner == user_team["name"]:
        player.premier_league_winner()
    print()
    print(f"🏆{winner} are Premier League Champions!🏆 ".center(100, " "))
    print()

    relegated_teams = display_table(table)


    player.calculate_transfer_value()

    print(f"\n{player.display_name()} Transfer value: £{round(player.transfer_value,1)}M")

    return relegated_teams


def player_improvement(player):
    """
    Determines if a player improved or not after the season
    :param player: the user's player
    :return: None: adjusts player rating in function
    """
    improved = random.choice([True,False])
    print(f"\nDid {player.name} improve?", end = " ")
    time.sleep(3)

    if improved:
        print("Yes")
        time.sleep(2)
        changes = random.randint(2,4)
        print("How many attributes:", end=" ")
        time.sleep(1)
        print(changes)
        time.sleep(1)

        while changes > 0:
            amount = random.randint(1,2)
            attribute_improved, final_amount = player.change_player_stat(amount)

            #checks if there is an attribute to be improved
            if attribute_improved is not None:
                print(f"Attribute Improved: {attribute_improved} +{final_amount} ")
                time.sleep(2)
                changes -= 1

            else:
                print("max reached for every stat")
                break

    else:
        print("No")
        time.sleep(2)
        player_downgrade(player)


def player_downgrade(player):
    """
    determines if the player downgrades in any attribute
    :param player:
    :return:
    """
    worsened = random.choice([True, False])
    print(f"\nDid {player.name} downgrade?", end=" ")

    time.sleep(3)

    if worsened:
        print("Yes")
        time.sleep(2)
        changes = random.randint(2, 4)
        print("How many attributes:", end=" ")
        time.sleep(1)
        print(changes)
        time.sleep(1)

        while changes > 0:
            amount = random.randint(-3, -1)
            attribute_downgraded, final_amount = player.change_player_stat(amount)

            # checks if there is an attribute to be downgraded
            if attribute_downgraded is not None:
                print(f"Attribute downgraded: {attribute_downgraded}  {final_amount}")
                time.sleep(2)
                changes -= 1

            else:
                print("min reached for every stat")
                break
    else:
        print("No")
        time.sleep(2)



def transfer_options(player,teams,min_value,max_value):
    """
    provides options for player to transfer to depending on their average rating for the season.
    Also provides transfer offer based on player's transfer value
    :param player: user's player
    :param teams: every team in the league
    :param min_value: minimum transfer value of player
    :param max_value: maximum transfer value of player
    :return: teams_offering(list): list of the teams offering a transfer
    """
    elite_teams = teams[0:5]
    mid_table_teams = teams[5:11]
    lower_teams = teams[11:20]

    num_interested = random.randint(1,2) #randomizes number of interested teams from each category

    teams_offering = []
    clubs_seen = set()

    #teams offering depends on player's season. Better season = better teams calling
    for team_offering in range(num_interested):

        if player.season_rating >= 7.4:
            club = random.choice(elite_teams)
            price = ((int(random.triangular(min_value, max_value + 1, max_value)))/1000000)
            if club["name"] not in clubs_seen:
                teams_offering.append([club, price])
                clubs_seen.add(club["name"])

        if player.season_rating < 7.4:
            club = random.choice(mid_table_teams)
            price = ((int(random.randint(min_value, max_value + 1)))/1000000)
            if club["name"] not in clubs_seen:
                teams_offering.append([club, price])
                clubs_seen.add(club["name"])

        if player.season_rating <= 7.0:
            club_one = random.choice(mid_table_teams)
            price_one = ((int(random.randint(min_value, max_value + 1)))/1000000)


            if club_one["name"] not in clubs_seen:
                teams_offering.append([club_one,price_one])
                clubs_seen.add(club_one["name"])

        if player.season_rating < 6.8:
            club = random.choice(lower_teams)
            price = ((int(random.triangular(min_value, max_value + 1, min_value))) / 1000000)
            if club["name"] not in clubs_seen:
                teams_offering.append([club,price])
                clubs_seen.add(club["name"])

    return teams_offering

def display_career_stats(player, clubs_played):
    """
    displays player's career stats
    :param player: user's player
    :param clubs_played: clubs the user played for in their career
    :return: None: prints career stats
    """
    print()
    print("⭐"*50 ,"\n")
    print(f"{player.name} Career Stats: ".center(105, " "))
    print()

    played_for = ",".join(clubs_played)
    print(f"Clubs Played for: {played_for}".center(100, " "))
    print(f"👕{player.career_length*38} appearances👕".center(100, " "))
    print(f"⚽Career Goals: {player.career_goals}⚽".center(100, " "))
    print(f"🎯Career Assists: {player.career_assists}🎯".center(100, " "))
    print(f"💪Career Clean Sheets: {player.career_clean_sheets}💪".center(100, " "))
    print(f"🏆Premier League Titles won: {player.prem_titles}🏆".center(100," "))
    print()

    print(f"⚽Most Goals in a Season: {player.highest_goals}⚽".center(100, " "))
    print(f"🎯Most Assists in a Season: {player.highest_assists}🎯".center(100, " "))
    print(f"🏆Highest Transfer Value: £{player.highest_value}M🏆".center(100, " "),"\n")

    print("⭐"*50)

def choose_transfer(options,relegated):
    possible_choice = ["0","1","2","3","4","5","6","7"]
    if relegated:
        possible_choice.remove("0")
    num_of_options = len(options)
    print(f"\n{num_of_options} clubs want to sign you!")
    time.sleep(2)
    for club in options:
        print(f"{club[0]["name"]} wants to sign you for £{round(club[1],1)}M")
        time.sleep(2)

    while True:
        print("\nEnter ",end="")
        if not relegated:
            print(f"0 to stay at your current club,",end="")

        for option in range(num_of_options):
            print(f"   {option+1} to join {options[option][0]["name"]}",end="")

        user_choice = input(": ")

        if user_choice in possible_choice:
            return user_choice
        else:
            print("Please enter one of the following choices")

def relegation_and_promotion(prem_teams,efl_teams,relegated_teams,user_team):
    relegated = False
    clubs_promoted = 0
    print()
    while clubs_promoted < 3:
        promoted_club = random.choice(efl_teams)
        print(f"{promoted_club["name"]} has been promoted")
        efl_teams.remove(promoted_club)
        prem_teams.append(promoted_club)
        clubs_promoted += 1
        time.sleep(0.5)

    print()
    for team in relegated_teams:

        print(f"{team["name"]} has been Relegated")
        time.sleep(0.5)
        prem_teams.remove(team)
        efl_teams.append(team)
        if team == user_team:
            relegated = True


    return relegated



def career(teams,efl_teams):
    """
    simulates entire player career and transfers
    :param teams: dictionary containing all premier league teams
    :param efl_teams: dictionary containing a select few efl teams that can get promoted and relegated
    :return:
    """


    prem_teams = teams.copy()

    user_team = choose_user_team(teams)

    clubs_played_for = [user_team["name"]]

    player,career_length = enter_information(user_team["name"])

    prem_teams.remove(user_team)

    for season in range(career_length):
        actual_season_num = season+1
        print(f"\n🦁Season {actual_season_num}🦁")
        relegated_clubs = simulate_season(prem_teams,player,user_team)
        prem_teams.append(user_team)
        full_relegated_info = get_relegated_info(prem_teams,relegated_clubs)
        user_relegated = relegation_and_promotion(prem_teams,efl_teams,full_relegated_info,user_team)

        if (actual_season_num % 3 == 0 and actual_season_num != career_length) or user_relegated:
            options = transfer_options(player,prem_teams,player.min_value, player.max_value)
            user_choice = choose_transfer(options,user_relegated)

            if user_choice != "0":

                user_team = options[int(user_choice)-1][0]

                clubs_played_for.append(user_team["name"])

            player_improvement(player)
            print(f"\nAttributes after season {actual_season_num}:")
            time.sleep(1)
            print(f"Team: {user_team["name"]}")
            show_stats(player)

        prem_teams.remove(user_team)
        player.check_highest()
        player.clear_season_stats()


    time.sleep(2)
    display_career_stats(player,clubs_played_for)




def main():

    prem_teams,efl_teams = get_league_data("PL_teams.txt")

    career(prem_teams,efl_teams)


if __name__ == "__main__":
    main()



