import time

def final():
    Q5 = input("Can it walk on both 2 and 4 legs?\nAnswer:")
    if Q5 == "yes":
        print("Your dinosaur is the Parasauolophus!")
        A = input("Again?\nAnswer:")
        if A == "yes":
            time.sleep(1)
            game()
        elif A == "no":
            print("Bye!!")
    elif Q5 == "no":
        Q6 = input("Does it have a long neck?\nAnswer:")
        if Q6 == "yes":
            print("Your dinosaur is the Diplodocus!")
            A = input("Again?\nAnswer:")
            if A == "yes":
                time.sleep(1)
                game()
            elif A == "no":
                print("Bye!!")
        elif Q6 == "no":
            print("Your dinosaur is the Oviraptor!")
            A = input("Again?\nAnswer:")
            if A == "yes":
                time.sleep(1)
                game()
            elif A == "no":
                print("Bye!!")
    

def game():
    print("This is the dinosaour guessing game!!\nAnswer all questions with a yes or no in lowercase!!")
    time.sleep(3)
    Q1 = input("Does it walk on 2 legs?\nAnswer:")
    if Q1 == "yes":
        final()
    elif Q1 == "no":
        Q2 = input("Does it eat fish?\nAnswer:")
        if Q2 == "yes":
            print("your dinosaur is the Baryonyx!")
            A = input("Again?\nAnswer:")
            if A == "yes":
                time.sleep(1)
                game()
            elif A == "no":
                print("Bye!!")
        elif Q2 == "no":
            Q3 = input("Does it have an oversized head?\nAnswer:")
            if Q3 == "yes":
                print("Your dinosaur is a T-rex!")
                A = input("Again?\nAnswer:")
                if A == "yes":
                    time.sleep(1)
                    game()
                elif A == "no":
                    print("Bye!!")
            elif Q3 == "no":
                Q4 = input("Is it feathered?\nAnswer:")
                if Q4 == "yes":
                    print("Your dinosaur is the Velociraptor!")
                    A = input("Again?\nAnswer:")
                    if A == "yes":
                        time.sleep(1)
                        game()
                    elif A == "no":
                        print("Bye!!")
                    
                elif Q4 == "no":
                    final()
               
    
                
    

game()
                
            
