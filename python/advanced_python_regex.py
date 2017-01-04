import csv
import re
f = open("faculty.csv")
csv_f = csv.reader(f)
degree_count = {}
prof_title = {}
email_address = []
firstline = True
for row in csv_f:
    if firstline:
        firstline = False
        continue
    else:
        #print row[1]
        qual = row[1].split()
        #print qual
        for qual1 in qual:
            q1 = qual1.replace(".","")
            #print q1
            if q1 in degree_count:
                degree_count[q1] += 1
            else:
                degree_count[q1] = 1

        title = re.search("(\w+ )?Professor", row[2])
        #print title.group()
        if title.group() in prof_title:
            prof_title[title.group()] += 1
        else:
            prof_title[title.group()] = 1

        email_address.append(row[3])
#print email_address
domain_list = []
for email in email_address:
    domain_name = re.search(r'@[\w.-]+', email)
    if domain_name.group() not in domain_list:
        domain_list.append(domain_name.group())

print degree_count
print "\n"
print prof_title
print "\n"
print email_address
print "\n"
print domain_list
f.close()
