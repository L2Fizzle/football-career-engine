import random
from audioop import reverse


def points_calculation(min_points, max_points):
    '''
    calculates points based on range and gives random realistic value for goal difference based on points
    :param min_points: minimum number of points the specific team can earn
    :param max_points: maximum number of points the specific team can earn
    :return:
    '''
    team_points = random.randint(int(min_points),int(max_points))
    goal_difference = round(team_points*0.9 - 40)
    team_goal_difference = goal_difference + random.randint(-15,10)
    return team_points,team_goal_difference

def prem_table(unsorted_table):
    '''
    sorts table based on points and goal difference
    :param unsorted_table: unsorted list containing team names, points, and goal difference
    :return: None: sorts the list
    '''
    unsorted_table.sort(key=lambda team: (team["points"], team["goal_difference"]), reverse=True)

def display_table(table):
    print(f"{"Position":<8} {"Team Name":<25}  {"Points":>6}{"GD":>6}")
    for position in range(0,20):
        actual_position = position + 1
        print(f"{actual_position:<8}", f"{str(table[position]["name"]):<25}{str(table[position]["points"]):>6}{str(table[position]["goal_difference"]):>8}")


