hourspernight = input("How many hours per night do you sleep? ")
hoursperweek = int(hourspernight) * 7              #Multiplies by 7 to show you how many hors a week you sleep
print ("You sleep",hoursperweek,"hours per week")
hourspermonth = float(hoursperweek) * 4.35                #Average of 4.35 weeks in a month so value is multiplied by this value to get hours in a month
print ("You sleep",hourspermonth,"hours per month")
dayspermonth = float(hourspermonth) / 24
print ("This is",dayspermonth,"days per month that you have slept for")  #shows how many days in a month you have slept for