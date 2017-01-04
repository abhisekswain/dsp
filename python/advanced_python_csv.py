import csv
import re
f = open("faculty.csv")
csv_f = csv.reader(f)
email_address = []
firstline = True
for row in csv_f:
    if firstline:
        firstline = False
        continue
    else:
        email_address.append(row[3])
print email_address

with open('emails.csv', 'wb') as f1:
    writer = csv.writer(f1)
    for val in email_address:
        writer.writerow([val])

f.close()
f1.close()
