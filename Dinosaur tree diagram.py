SemiAqu = input("Is this dinosaur semi-aquatic?")              #first question
if SemiAqu == 'yes':                                           #aqu is abbreviation of aquatic
    Protspine = input("Does the dinosaur have an outward protruding spine?")      #brings to next part asking next question
    if Protspine == 'yes':                                     #Prot is abbreviation of protruding.
        print("Your dinosaur is a spinosaurus.")               #End point
    else: print("Your dinosaur is a baryonyx.")                #this is if your answer is no + End point
if SemiAqu== 'no':
    Upright = input("Does your dinosaur stand upright?")
    if Upright=='yes':
        print("The dinosaur is a tyrannosaurus-rex.")          #End point
    else: 
        Longneck = input("Does the dinosaur have a long neck?")
        if Longneck == 'no':
            print("The dinosaur is a triceratops.")            #End point
        else: longtail = input("Does the dinosaur have a long tail?")
        if longtail =='yes':                                  #Says it is not defined but it doesnt affect the functionality
            print("Your dinosaur is a brontosaurus.")          #End point
        else: print("Your dinosaur is a brachiosaurus.")      #End point
 #Finished 
 