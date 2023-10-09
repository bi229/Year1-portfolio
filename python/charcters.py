import time

def game():
    print("You are going to be asked multiple yes or no question, put Y or N for you answer")
    time.sleep(2)
    Q1 = input("Is your character male\nAnswer:")
    if Q1 == "Y" or Q1 == "y":
        Q5 = input("Can your chacter disable abilities\nAnswer:")
        if Q5 == "Y" or Q5 == "y":
            print("Your character is Kay/O")
            time.sleep(3)
            game()
        elif Q5 == "N" or Q5 == "n":
            print("Your character is phoenix")
            time.sleep(3)
            game()
    elif Q1 == "N" or Q1 == "n":
        Q2 = input("Is Your character a dualist\nAnswer:")
        if Q2 == "Y" or Q2 == "y":
            print("Your character is Reyna")
            time.sleep(3)
            game()
        elif Q2 == "N" or Q2 =="n":
            Q3 = input("Is youre character a smoke\nAnswer:")
            if Q3 == "Y" or Q3 == "y":
                print("Your character is Viper")
                time.sleep(3)
                game()
            elif Q3 == "N" or Q3 == "n":
                Q4 = input("Can youre character heal\nAnswer:")
                if Q4 == "Y" or Q4 == "y":
                    print("Your character is sage")
                    time.sleep(3)
                    game()
                elif Q4 == "N" or Q4 == "n":
                    print("Your character is Killjoy")
                    time.sleep(3)
                    game()
        
game()
