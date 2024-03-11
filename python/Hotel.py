import time
import csv

def Book():
    print("Work")
def Room_info():
    with open("Rooms.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[1])
def Service():
    print("Work")
def Payments():
    print("Work")
def Records():
    print("Work")


def Home():
    Option = input("Pick a Option \n1.Book\n2.Room info\n3.Service\n4.Payment\n5.Record\nOption: ")

    if Option == "1":
        Book()
    elif Option == "2":
        Room_info()
    elif Option == "3":
        Service()
    elif Option == "4":
        Payments()
    elif Option == "5":
        Records()
    else:
        print("Invalid Option")
        time.sleep(1)
        Home()

Home()
