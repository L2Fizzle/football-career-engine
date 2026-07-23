import random
import time
import Prem_season

from player import Player


def enter_information(team_name):
    """
    allows user to enter their name and generates their attributes
    :param team_name: name for user's team (randomly chosen)
    :return: player,player.display_career_length()(tuple): contains the player's information and their career length
    """
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
    """
    randomly chooses user's team based on the premier league teams for that season
    :param teams: list containing all premier league teams
    :return: user_team(dict): contains users team's information
    """
    user_team = random.choice(teams)

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
    """
    Retrieves data from PL teams txt file
    :param filename: name of league txt file
    :return: prem_teams,elf_teams: two lists containing information about premier league teams and efl teams for future use
    """
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
                    "max_points":float(parts[5]),"league":str(parts[6]),"european_reputation":float(parts[7])}
            if team["league"] == "prem":
                prem_teams.append(team)
            else:
                efl_teams.append(team)
    return prem_teams,efl_teams


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
    print(f"Clubs Played for: {played_for}".center(102, " "))
    print(f"👕{player.career_length*38} appearances👕".center(100, " "))
    print(f"⚽Premier League Goals: {player.prem_goals}⚽".center(100, " "))
    print(f"🎯Premier League Assists: {player.prem_assists}🎯".center(100, " "))
    print(f"💪Career Clean Sheets: {player.career_clean_sheets}💪".center(100, " "))
    print()

    print(f"⚽Most Goals in a Season: {player.highest_goals}⚽".center(100, " "))
    print(f"🎯Most Assists in a Season: {player.highest_assists}🎯".center(100, " "))
    print(f"🏆Highest Transfer Value: £{player.highest_value}M🏆".center(100, " "),"\n")

    print(" European Competitions".center(100," "))
    time.sleep(1)
    print()
    print(f"Seasons in the Champions League: {player.ucl_seasons}".center(100," "))
    time.sleep(2)
    print(f"⚽UCL Goals: {player.ucl_goals}⚽".center(100, " "))
    time.sleep(2)
    print(f"🎯UCL Assists: {player.ucl_assists}🎯".center(100, " "))
    time.sleep(1)
    print()

    print(f"Seasons in the Europa League: {player.europa_seasons}".center(100," "))
    time.sleep(2)
    print(f"⚽Europa League Goals: {player.europa_goals}⚽".center(100, " "))
    time.sleep(2)
    print(f"🎯Europa League Assists: {player.europa_assists}🎯".center(100, " "))
    time.sleep(1)
    print()
    print(f"Seasons in the Conference League: {player.conf_seasons}".center(100," "))
    time.sleep(2)

    print(f"⚽Conference League Goals: {player.conf_goals}⚽".center(100, " "))
    time.sleep(2)

    print(f"🎯Conference League Assists: {player.conf_assists}🎯".center(100, " "))


    print()
    time.sleep(1)



    print(" Trophy Cabinet".center(100," "))
    time.sleep(1)
    print()
    print(f"🏆Premier League Titles won: {player.prem_titles}🏆".center(100," "))
    print(f"🏆Champions League Titles won: {player.ucl_titles}🏆".center(100," "))
    print(f"🏆Europa League Titles won: {player.europa_titles}🏆".center(100," "))
    print(f"🏆Conference League Titles won: {player.conf_titles}🏆".center(100," "))

    print()
    time.sleep(2)
    print(f"⚽Career Goals: {player.career_goals}⚽".center(100," "))
    print(f"🎯Career Assists: {player.career_assists}🎯".center(100, " "))
    print(f"Career Rating: {round(player.calculate_career_rating(),1)}".center(100," "))
    print()


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
        relegated_clubs = Prem_season.simulate_season(prem_teams,player,user_team)
        prem_teams.append(user_team)
        full_relegated_info = Prem_season.get_relegated_info(prem_teams,relegated_clubs)
        user_relegated = Prem_season.relegation_and_promotion(prem_teams,efl_teams,full_relegated_info,user_team)
        print(f"\n{player.display_name()} Transfer value: £{round(player.transfer_value, 1)}M")


        if (actual_season_num % 3 == 0 and actual_season_num != career_length) or user_relegated:
            options = transfer_options(player,prem_teams,player.min_value, player.max_value)
            user_choice = choose_transfer(options,user_relegated)

            if user_choice != "0":

                user_team = options[int(user_choice)-1][0]

                clubs_played_for.append(user_team["name"])

            player.player_improvement()
            print(f"\nAttributes after season {actual_season_num}:")
            time.sleep(1)
            print(f"Team: {user_team["name"]}")
            show_stats(player)

        prem_teams.remove(user_team)
        player.check_highest()
        player.clear_season_stats()


    time.sleep(2)
    player.european_success()
    display_career_stats(player,clubs_played_for)

def main():

    prem_teams,efl_teams = get_league_data("PL_teams.txt")

    career(prem_teams,efl_teams)


if __name__ == "__main__":
    main()



