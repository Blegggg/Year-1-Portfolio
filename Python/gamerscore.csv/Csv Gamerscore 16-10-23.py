file = open("gamerscore.csv", "r")   #r oppens up file
line = file.readline()
Searchname = input("Enter name: ")


while (line) :                              #sets up a variable
    data =line.split(",")
    if data[0]==Searchname:
        print("Name:  ",data[0])
        print ("Gamerscore: ",data[1])
    line=file.readline()                #it produces a list of data and then goes to next line

file.close()    