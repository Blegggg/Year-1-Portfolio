Protagonist = input("Is your character a protagonist, Yes or no?")
if Protagonist == 'no':
    print("Your character is plankton") # Gives plankton
else:
    Protagonist == 'yes' #Saying yes brings to next question
    KrustyKrabWorker = input("Does your character work at the Krusty Krab?")
    if KrustyKrabWorker == 'no': 
        mainlyblue = input ("Is your character mainly blue?")   #Saying no leaves either gary or patrick
        if mainlyblue == 'yes': print("Your character is Gary.")
        else: print("Your character is patrick")
    if KrustyKrabWorker == 'yes':
        Rich = input ("Is your character rich?") #Saying yes leaves mr krabs only
        if Rich == 'yes':
            print("Your character is Mr Krabs.")
        else:
            enjoysjob = input("Does your character enjoy their job?") #Saying yes gives spongebob.
            if enjoysjob == 'yes':
                print("Your character is spongebob.")
    else: print("Your character is Squidward")

    


    