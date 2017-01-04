import csv
import re
from collections import defaultdict
f = open("faculty.csv")
csv_f = csv.reader(f)
faculty_dict = {}
professor_dict = {}
firstline = True
for row in csv_f:
    if firstline:
        firstline = False
        continue
    else:
        name = row[0].split(" ")
        last_name = name[-1]
        details_list = [row[1], row[2], row[3]]
        if last_name not in faculty_dict.keys():
            faculty_dict[last_name] = [details_list]
        else:
            faculty_dict[last_name].append(details_list)

        new_name = (name[0], name[-1])
        if new_name not in professor_dict.keys():
            professor_dict[new_name] = details_list
#print faculty_dict
#print "\n"
#print professor_dict

sorted_prof_dict = sorted(professor_dict.items(), key = lambda t: t[0][-1])
print faculty_dict
print "\n"
print professor_dict
print "\n"
print sorted_prof_dict
