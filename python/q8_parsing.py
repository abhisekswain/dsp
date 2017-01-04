# The football.csv file contains the results from the English Premier League.
# The columns labeled Goals and Goals Allowed contain the total number of
# goals scored for and against each team in that season (so Arsenal scored 79 goals
# against opponents, and had 36 goals scored against them). Write a program to read the file,
# then print the name of the team with the smallest difference in for and against goals.
import csv
f = open("football.csv")
csv_f = csv.reader(f)
firstline = True
goal_diff = {}
for row in csv_f:
    if firstline:
        firstline = False
        continue
    else:
        goal_diff[row[0]] = abs(int(row[5]) - int(row[6]))

#print goal_diff
min_goal_diff_team = min(goal_diff, key = goal_diff.get)
print "\nThe team with min goal difference is %s\n" %min_goal_diff_team


f.close()
