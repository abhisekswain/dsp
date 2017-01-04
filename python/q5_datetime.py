# Hint:  use Google to find python function

from datetime import datetime
####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'
date_format = '%m-%d-%Y'
start = datetime.strptime(date_start, date_format)
end = datetime.strptime(date_stop, date_format)
print "\na. The number of days between %s and %s is %d days \n" % (date_start, date_stop, (end - start).days)

####b)

date_format1 = '%m%d%Y'
date_start1 = '12312013'
date_stop1 = '05282015'
start1 = datetime.strptime(date_start1, date_format1)
end1 = datetime.strptime(date_stop1, date_format1)
print "\nb. The number of days between %d-%d-%d and %d-%d-%d is %d days \n" % (start1.month, start1.day, start1.year, end1.month, end1.day, end1.year, (end1 - start1).days)


####c)
date_start2 = '15-Jan-1994'
date_stop2 = '14-Jul-2015'
date_format2 = '%d-%b-%Y'
start2 = datetime.strptime(date_start2, date_format2)
end2 = datetime.strptime(date_stop2, date_format2)
print "\nc. The number of days between %s and %s is %d days \n" % (date_start2, date_stop2, (end2 - start2).days)
