import datetime
time = datetime.datetime.now()

print
print
print 
 
print ("Current Date =  %s/%s/%s" % (time.day, time.month, time.year) )
 
 
print ("Time = %s:%s:%s" % (time.hour, time.minute, time.second) )
print
print
print

while True && daysL != -1:

	dt  = datetime.datetime
	now = dt.now()
	# This gives timedelta in days
	delta = dt(year=2015,month=(8),day=12,hour=7,minute=0,second=0) - dt(year=now.year, month=now.month, day=now.day, hour = now.hour, minute = now.minute, second = now.second)
	alpha = str(delta).split(":")
	beta = str(alpha).split(" ")
	beta = str(beta).strip("[") #Take out the [ for every reading of 33
	daysL = beta[3] + beta[4]   #Number of days to event
	hoursL = beta[18] + beta[19]
	minutesL = beta[27] + beta[28]
	secondsL = beta[36] + beta[37]
	
	#print("Time Left: " int(daysL) + "Days, " + int(hoursL) + "Hours, " + int(minutesL) + "Minutes, " + int(secondsL) + "Seconds")
	print("Time Left: " + daysL + " Days, " + hoursL + " Hours, " + minutesL + "  Minutes, " + secondsL + " Seconds")
	# This gives timedelta in days & seconds


	#	startCounting = datetime.combine(now.date(), time(0))
	#	print (time - startCounting).seconds
