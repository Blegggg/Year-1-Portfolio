file = open("shop1.csv", "r")
line = file.readline()
while (line) :                              #sets up a variable
    data =line.split(",")
    
    Search = input("What detail?: ")
    if Search== "location":
        location = input("enter location of person")
        if location==data[1]:
               while(line):
                    print ("Name= ", data[0],"Location= ", data[1],"City= ", data[2],"Number= ", data[3]) 
                    file.close()

    if Search== "city":
        city = input("Put city they are in")
        if city==data[2]:
            print ("Name= ", data[0],"Location= ", data[1],"City= ", data[2],"Number= ", data[3])
            file.close()
    
    if Search=="number":
        number=int(input("Put in persons number"))
        if number==data[3]:
             print ("Name= ", data[0],"Location= ", data[1],"City= ", data[2],"Number= ", data[3])
             file.close()

line=file.readline()                #it produces a list of data and then goes to next line

file.close()    