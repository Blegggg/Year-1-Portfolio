print ("Insert Username.")   #inputting a name will greet you.
username = input()
print ("Hello,",username)

print ("Please provide your mobile phone's network.")
network = input()
print ("Your details are:",username,network)   #Will print out their username and their network that they have typed out

minutespermonth = ("How many minutes have you used this app for this month?")
minutestotal = minutespermonth * 0.10
textspermonth = ("How many texts have you sent for this month?")
texttotal = textspermonth * 0.05
print ("Your total charge is", minutestotal + texttotal) #should show your total bill for your amount