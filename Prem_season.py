import random
import time
import math

from Prem_table import points_calculation
from Prem_table import prem_table
from Prem_table import display_table

def simulation_speed():
    """
    Asks the user whether they want the match results to slowly display, or all of the results immediately
    :return: sim_speed(int): the number of seconds it takes for each match to display.
    """
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

def matchday_team(teams, teams_played):
    """
    randomly chooses team to play
    Once the team is played, they cannot be played again until every team is played (later on)
    :param teams: list of every team that can be played. Used to be removed once played
    :param teams_played: list of every team played to be appended.
    :return: team: the team that the user will play against
    """
    team = random.choice(teams)
    teams.remove(team)
    teams_played.append(team)
    return team

def matchday_rating(team_attack, team_defense, consistency):
    """
    Adjusts the ratings for both teams based on consistency
    Allows for the unpredictability of the Premier League
    :param team_attack: team's attack rating
    :param team_defense: team's defense rating
    :param consistency: team's consistency
    :return: team_attack,team_defense: the updated attack and defense for the team
    """
    form = round(random.uniform(-consistency, consistency),1)
    team_attack += form
    team_defense += form
    if team_attack >= 9.9:
        team_attack = 9.9
    if team_defense >= 9.9:
        team_defense = 9.9
    return team_attack, team_defense

def attack_chance(team_goals, team_attack, opponent_defense):
    """
    calculates whether the attack chance can result in a goal
    uses the team's stats, the opponents data, and randomness to determine if the attack results in a goal
    the more goals a team has, the harder it is to score more. This can be due to respect, the other team adjusting, etc...
    :param team_goals: the amount of goals the team has scored
    :param team_attack: the team's attack rating
    :param opponent_defense: the team's defense rating
    :return: team_goals: the amount of goals scored by the team after that attack.
    """
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

def player_season(player):
    """
    prints player's end of season stats
    :param player: user's player
    :return: None: displays user's season and calculates their rating (added to attributes)
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
    :return: full info of teams
    """
    return {team["name"]:team for team in teams}

def get_relegated_info(teams,relegated_teams):
    """
    retrieves full info for relegated teams
    Used to remove relegated clubs from the premier league and add them to the EFL championship
    :param teams: list of all premier league teams
    :param relegated_teams: list of relegated team names
    :return: full_info: list of relegated teams' information
    """
    lookup = team_lookup(teams)
    full_info = []
    for team in relegated_teams:
        full_info.append(lookup[team])
    return full_info

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

def season_table(teams, user_team,user_team_points,user_team_gd):
    """
    Calculates the amount of points each team earns in the season
    :param teams: list containing all teams
    :param user_team: the user's team
    :param user_team_points: the amount of points earned by the user's team
    :param user_team_gd: the goal difference of the user's team
    :return: teams_and_points: list of every team, the number of points earned and goal difference
    """
    teams_and_points = []
    for prem_team in teams:
        min_points = prem_team["min_points"]
        max_points = prem_team["max_points"]
        team_points, team_goal_difference = points_calculation(min_points,max_points)
        teams_and_points.append({"name": prem_team["name"], "points": team_points, "goal_difference": team_goal_difference})
    teams_and_points.append({"name": f"{user_team["name"]}", "points": user_team_points, "goal_difference": user_team_gd})

    prem_table(teams_and_points)
    return teams_and_points

def simulate_season(full_teams,player,user_team):
    """
    simulates entire premier league season for the user
    determines entirety of player's season, relegated teams, and uses functions to obtain the table and champions of the season
    :param full_teams: full list of premier league teams
    :param player: user's player
    :param user_team: the user's team
    :return:
    """

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