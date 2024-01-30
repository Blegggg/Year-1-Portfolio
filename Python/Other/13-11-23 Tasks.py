print("The speed limit is 59.")
Limit = 0<59
Distance = int(input("What was the distance the vehicle travelled in miles?"))
Time = int(input("How long did it take for the vehicle to reach that distance in hours?"))
Speed = Distance / Time
print(Speed)
if Speed >= 59:
    print("This vehicle exceeds speed limit")
else: print("Car was within speed limit")

NumberPlate = str(input("What is the number plate of the vehicle?"))
