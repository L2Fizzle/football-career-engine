import random
import time
from player import Player


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
    show_stats(player,team_name)

    return player,player.display_career_length()


def choose_user_team(teams):
    user_team = random.choice(teams)

    return user_team

def show_stats(player,team_name):
    attributes = [("Starting Age", player.display_age()),
             ("Career Length", player.display_career_length()),
             ("Team", team_name),("Position", player.display_position()),
             ("Pace", player.display_pace()),
             ("Shooting", player.display_shooting()),
             ("Passing", player.display_passing()),
             ("Dribbling", player.display_dribbling()),
             ("Defending", player.display_defending()),
             ("Strength", player.display_strength()),
             ("Football IQ", player.display_iq())]


    print("Generating player...")
    time.sleep(2)

    for attribute, value in attributes:
        print(f"{attribute}: ",end="")
        time.sleep(1)
        print(f"{value}")
        time.sleep(1)


def get_league_data(filename):
    teams = []
    with open(filename, "r") as file:
        lines = file.readlines()[1:]
        for line in lines:
            parts = line.strip().split(",")

            team = {"name":parts[0],
                    "attack":float(parts[1]),
                    "defense":float(parts[2]),
                    "reputation":float(parts[3]),
                    "consistency":float(parts[4])}
            teams.append(team)
    return teams

def check_ready():
    while True:
        begin_message = input("\nAre you ready to begin the season (y/n)?: ")
        if begin_message.lower() == "y":
            return
        else:
            print("Whenever you're ready!")

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
    goal_chance = team_attack - (opponent_defense / 2)

    odds_of_scoring = random.randint(round(10 - team_attack), 10)

    if goal_chance >= odds_of_scoring:
        team_goals += 1

    return team_goals

def display_player_match(player):
    print(f"{player.name} match stats:")
    print(f"{player.match_goals} Goals,  {player.match_assists} Assists,  "
          f"{player.match_dribbles} successful dribbles")
    print(f"{player.match_passes} passes completed with {player.match_pass_accuracy:.0%} accuracy")

    player_rating = player.calculate_match_rating()
    print(f"Final match rating: {player_rating:.1f}")

    player.clear_match_stats()
    player.clear_player_rating()

def match(player, team_name, team_attack, team_defense, opponent_name, opponent_attack, opponent_defense):


    team_goals = 0
    opponent_goals = 0

    user_shot_attempts = random.randint(0,int(team_attack/2)) #makes shooting opportunities based on team's attacking threat
    user_key_pass_attempts = random.randint(0,int(player.playmaking_ability/2))
    dribble_attempts = random.randint(0,int(player.dribbling/2))

    team_chances = random.randint(round(team_attack/2),round(team_attack)) #team chances (excluding user chances)
    for chance in range(team_chances):
        team_goals = attack_chance(team_goals, team_attack,opponent_defense)

    opponent_chances = random.randint(round(opponent_attack/2),round(opponent_attack)) #opponent chances
    for chance in range(opponent_chances):
        opponent_goals = attack_chance(opponent_goals, opponent_attack, team_defense)

    for shot in range(user_shot_attempts):
        player.shot_attempt(opponent_defense)

    for ball in range(user_key_pass_attempts):
        player.key_pass(opponent_defense)

    for dribble in range(dribble_attempts):
        player.dribble_attempt(opponent_defense)

    player.calculate_passes()

    player.match_assists = min(player.match_assists, team_goals) #reduces over inflating of goals and allows more realistic match simulations

    player.update_assists()
    total_team_goals = team_goals + player.match_goals

    print(f"\nScore: {team_name}  {total_team_goals} - {opponent_goals}  {opponent_name}\n")

    display_player_match(player)

    if total_team_goals > opponent_goals:
        points_gained = match_result_points("W")
    elif total_team_goals == opponent_goals:
        points_gained = match_result_points("D")
    else:
        points_gained = match_result_points("L")
    return points_gained

def match_result_points(result):
    if result == "W":
        return 3
    elif result == "D":
        return 1
    else:
        return 0

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

def simulate_season(full_teams,player,user_team):

    sim_speed = simulation_speed()

    teams_played_once = []
    teams_played_twice = []
    team_name, team_attack, team_defense, team_reputation, team_consistency = (user_team["name"], user_team["attack"],
                                                             user_team["defense"], user_team["reputation"], user_team["consistency"])

    check_ready()
    matchday = 1
    team_points = 0
    team_wins = 0
    team_draws = 0
    team_losses = 0
    while full_teams:
        opponent = matchday_team(full_teams, teams_played_once)
        opponent_name, opponent_attack, opponent_defense, opponent_reputation, opponent_consistency = (opponent["name"],
                                                                                                       opponent["attack"],
                                                                                                       opponent["defense"],
                                                                                                       opponent["reputation"],
                                                                                                       opponent["consistency"])
        opponent_attack, opponent_defense = matchday_rating(opponent_attack, opponent_defense, opponent_consistency)
        team_attack, team_defense = matchday_rating(team_attack, team_defense, team_consistency)

        print("⚽" * 20)
        print(f"\nMatchday {matchday}")
        print(f"\nOpponent: {opponent_name}")
        match_and_points = match(player, team_name, team_attack, team_defense,
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
        matchday += 1
        print()
        team_attack, team_defense = user_team["attack"], user_team["defense"]
        time.sleep(sim_speed)

    while teams_played_once:
        opponent = matchday_team(teams_played_once, teams_played_twice)
        opponent_name, opponent_attack, opponent_defense, opponent_reputation, opponent_consistency = (opponent["name"],
                                                                                 opponent["attack"],
                                                                                 opponent["defense"],
                                                                                 opponent["reputation"],
                                                                                 opponent["consistency"])
        opponent_attack, opponent_defense = matchday_rating(opponent_attack, opponent_defense, opponent_consistency)
        team_attack, team_defense = matchday_rating(team_attack, team_defense, team_consistency)

        print("⚽" * 20)
        print(f"\nMatchday {matchday}")
        print(f"\nOpponent: {opponent_name}")
        match_and_points = match(player, team_name, team_attack, team_defense,
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

        matchday += 1
        print()
        team_attack, team_defense = user_team["attack"], user_team["defense"]
        time.sleep(sim_speed)


    print("⚽"*26)
    print("🦁"*8, "END OF SEASON STATS", "🦁"*8)
    print("⚽"*26)
    print()

    print(f"{player.name}")
    print(f"Season Goals: {player.season_goals}")
    print(f"Season Assists: {player.season_assists}")

    player.calculate_season_rating()

    print(f"Average Rating: {player.season_rating:.1f}")
    print(f"{team_name} Record: {team_wins}W {team_draws}D {team_losses}L")
    print(f"{team_name} finishes the season with {team_points} points")

def career(teams):

    prem_teams = teams.copy()

    user_team = choose_user_team(teams)

    player,career_length = enter_information(user_team["name"])

    prem_teams.remove(user_team)

    simulate_season(prem_teams,player,user_team)

def main():

    full_teams = get_league_data("PL_teams.txt")

    career(full_teams)


if __name__ == "__main__":
    main()



