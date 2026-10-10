# -----------------------------------------------------------
#  Name: Homework2
#  By:Brynn
#  Learning how to print the length of an object in a class
#       1.) Option 1, counting with a variable
#       2.) Option 2, using the python len() function
# -------------------------------------------------------------


class Human:
    def __init__(self, name="Human"):
        self.name = name

class Auto:
    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passengers(self,human):
        self.passengers.append(human)

    def print_passengers_names(self):
        if self.passengers!= []:
            passenger_counter = 0
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
                passenger_counter += 1

        else:
            print("There are no passengers in {self.brand}")
        print(f"The number of passengers added to {self.brand} is {passenger_counter}")
        print("Another way to print the counts is to use the length function")
        print(f"{len(self.passengers)} passengers")





nick = Human("Nick")
kate = Human("Kate")
car = Auto("Mercedes")


car.add_passengers(nick)
car.add_passengers(kate)
car.print_passengers_names()