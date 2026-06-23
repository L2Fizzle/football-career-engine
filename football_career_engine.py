import random
import time
from player import Player


def enter_information():
    while True:
        player_name = input("Enter your player's name: ").strip()

        if player_name == "":
            print("Name cannot be empty. Try again.")
        else:
            break

    player = Player(player_name)
    print(f"\nWelcome {player.display_name()}!\n"
          f"\nHere are your current attributes:\n")
    player.generate_attributes()
    show_stats(player)
    return player

def show_stats(player):
    print("Generating player...")
    time.sleep(2)

    print(f"Position: {player.display_position()}")
    time.sleep(2)

    print("Pace: ", end = "")
    time.sleep(2)
    print(player.display_pace())

    time.sleep(1)

    print("Shooting: ", end = "")
    time.sleep(2)
    print(player.display_shooting())

    time.sleep(1)

    print("Passing: ", end = "")
    time.sleep(2)
    print(player.display_passing())

    time.sleep(1)

    print("Dribbling: ", end = "")
    time.sleep(2)
    print(player.display_dribbling())

    time.sleep(1)

    print("Defending: ", end = "")
    time.sleep(2)
    print(player.display_defending())

    time.sleep(1)

    print("Strength: ", end = "")
    time.sleep(2)
    print(player.display_strength())

    time.sleep(1)

    print("Football IQ: ", end = "")
    time.sleep(2)
    print(player.display_iq())

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
                    "reputation":float(parts[3])}
            teams.append(team)
    return teams

def check_ready(player):
    while True:
        begin_message = input("\nAre you ready to begin the match (y/n)?: ")
        if begin_message.lower() == "y":
            return
        else:
            print("Whenever you're ready!")

def matchday_team(teams, teams_played):
    team = random.choice(teams)
    teams.remove(team)
    teams_played.append(team)
    return team

def match(player, opponent_name, opponent_defense):
    print(f"Opponent: {opponent_name}")
    print("\nThe referee blows the whistle and the match begins!")
    shot_attempts = random.randint(0,int(player.shooting/2))
    key_pass_attempts = random.randint(0,int(player.playmaking_ability/2))
    dribble_attempts = random.randint(0,int(player.dribbling/2))


    for shot in range(shot_attempts):
        player.shot_attempt(opponent_defense)

    for ball in range(key_pass_attempts):
        player.key_pass(opponent_defense)

    for dribble in range(dribble_attempts):
        player.dribble_attempt(opponent_defense)

    print(f"{player.name} scored {player.match_goals} goals")

    print(f"{player.name} assisted {player.match_assists} goals")

    print(f"{player.name} made {player.match_dribbles} successful dribbles")

    player_rating = player.calculate_match_rating()
    print(f"\nFinal match rating: {player_rating}")

    player.clear_match_stats()
    player.clear_player_rating()


def main():

    teams = get_league_data("PL_teams.txt")
    teams_played = []
    player = enter_information()

    while teams:
        check_ready(player)
        opponent = matchday_team(teams, teams_played)
        opponent_name, opponent_defense = opponent["name"], opponent["defense"]
        match(player,opponent_name, opponent_defense)


if __name__ == "__main__":
    main()



