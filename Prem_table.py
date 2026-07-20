import random


def points_calculation(min_points, max_points):
    """
    calculates points based on range and gives random realistic value for goal difference based on points
    :param min_points: minimum number of points the specific team can earn
    :param max_points: maximum number of points the specific team can earn
    :return:
    """
    team_points = random.randint(int(min_points),int(max_points))
    #two statements allows for more realistic goal difference calculations based on team position
    if team_points <= 70:
        goal_difference = round(team_points*0.9 - 50)
        team_goal_difference = goal_difference + random.randint(-10,10)
    else:
        goal_difference = round(team_points * 0.9 - 35)
        team_goal_difference = goal_difference + random.randint(-10, 10)
    return team_points,team_goal_difference

def prem_table(unsorted_table):
    """
    sorts table based on points and goal difference
    :param unsorted_table: unsorted list containing team names, points, and goal difference
    :return: None: sorts the list
    """
    unsorted_table.sort(key=lambda team: (team["points"], team["goal_difference"]), reverse=True)

def display_table(table):
    """
    displays full premier league table
    :param table: the table in dictionary form
    :return: relegated_teams: list of relegated teams (18th and below)
    """
    relegated_teams = []
    print(f"{"Position":<15} {"Team Name":<25}  {"Points":>8}{"GD":>10}")
    for position in range(0,20):
        actual_position = position + 1
        print(f"{actual_position:<15}", f"{str(table[position]["name"]):<25}{str(table[position]["points"]):>8}{str(table[position]["goal_difference"]):>12}")
        if actual_position >= 18:
            relegated_teams.append(table[position]["name"])
    return relegated_teams


