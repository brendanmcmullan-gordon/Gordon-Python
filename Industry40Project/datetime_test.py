import datetime

teststr = "21/01:00pm"

today = str(datetime.date.today())
yrmonth = '{:.8}'.format(today)
print(yrmonth)

# today = datetime.date.today()
# today = str(today)
# print(today)

splitstr = teststr.split('/')
# print(splitstr)
day = splitstr[0]
# print(day)
# print(splitstr[1].split(':'))
# print(splitstr[1].endswith('pm'))
timelist = splitstr[1].split(':')
hrs = timelist[0]
min = timelist[1]
min = min.rstrip('apm')
# print(min)

if splitstr[1].endswith('pm') == True:
    hrs = int(hrs)
    hrs += 12
    hrs = str(hrs)
    print(hrs)

print(yrmonth+day+" "+hrs+":"+min+":00")


