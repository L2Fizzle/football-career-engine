import random
import math
from player import Player


def enter_information():
    while True:
        player_name = input("Enter your player's name: ").strip()

        if player_name == "":
            print("Name cannot be empty. Try again.")
        else:
            break

    player = Player(player_name)
    print(f"Welcome {player.display_name()}!\n"
          f"\nHere are your current stats:\n")
    show_stats(player)
    return player

def show_stats(player):
    print(f"Shooting: {player.display_shooting()}\n"
          f"Passing: {player.display_passing()}\n"
          f"Dribbling: {player.display_dribbling()}\n"
          f"Season Goals: {player.display_season_goals()}\n"
          f"Season Assists: {player.display_season_assists()}")

def match(player, opponent_defense):
    print("\nThe referee blows the whistle and the match begins!")
    shot_attempts = random.randint(2,8)
    pass_attempts = random.randint(2,8)
    dribble_attempts = random.randint(2,8)


    for shot in range(shot_attempts):
        player.shot_attempt(opponent_defense)

    for ball in range(pass_attempts):
        player.key_pass(opponent_defense)

    for dribble in range(dribble_attempts):
        player.dribble_attempt(opponent_defense)

    print(f"{player.name} scored {player.match_goals} goals")

    print(f"{player.name} assisted {player.match_assists} goals")

    print(f"{player.name} made {player.match_dribbles} successful dribbles")

    player_rating = player.calculate_match_rating()
    print(f"\nFinal match rating: {player_rating}")

    added_skill_points = math.floor(player_rating)
    player.skill_point_collection(added_skill_points)


    player.clear_match_stats()

def post_match(player):
    print(f"Congrats! You earned {player.display_skill_points()} skill points!")

    while player.skill_points > 0:
        print("\nUpgrade shooting (s), passing (p), dribbling (d)?")
        choice = input("Choose stat: ").lower()

        if choice == "s":
            player.shooting += 1
        elif choice == "p":
            player.passing += 1
        elif choice == "d":
            player.dribbling += 1
        else:
            print("Sorry, that was not one of the options. Try again.")
            continue

        player.remove_skill_point()
        print(f"Remaining points: {player.skill_points}")

    print("\nHere are your stats after today's match:\n")
    show_stats(player)


def main():
    player = enter_information()
    opponent_defense = 75
    match(player,opponent_defense)
    post_match(player)


if __name__ == "__main__":
    main()



