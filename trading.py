import random

candies = ["starburst", "skittles", "milkyway", "jolly rancher", "Reese's", "Hershey's", "Snickers", "Kit Kat", "Twix", "Gummybears"]

class Student():
    # attributes
    name = ""
    preferences = {}
    candy = ""

    # constructor
    def __init__(self, my_list: list):
        self.name = random.choice(my_list)
        for i in candies:
            self.preferences[i] = random.randint(0, 10)
        self.candy = random.choice(candies)

    # getters
    def getPreferences(self):                              
        return self.preferences

    def getCandy(self):
        return self.candy
    
    # setters
    def setPreferences(self, preferences: dict):
        self.preferences = preferences

    def setCandy(self, candy: str):
        self.candy = candy

def read_file(filename: str):
    student_names = []
    classroom = []

    with open(filename, "r") as my_file:
        for line in my_file:
            student_names.append(line.strip())

    for i in range(30):
        classroom.append(Student(student_names))
    return classroom

def assign_pairs(classroom: list):
    shuffled_classroom = random.shuffle(classroom.copy())
    pairs = [(shuffled_classroom[i], shuffled_classroom[i+1]) for i in range(0, len(shuffled_classroom), 2)]    # Why use range() instead of just the shuffled classroom directly?
    return pairs

def tradingRound():
    classroom = read_file("students.txt")
    pairs = assign_pairs(classroom)

def main():
    pass


if __name__ == "__main__":
    main()

# Questions:
# Why do getters need an argument to self?
# How does an "if __name__ == "__main__" block work?
# Is random.choice() with or without replacement?

# Notes for future changes
# Make it so that classrooms can only have an even number of students since they trade in pairs.
# Think about the best way to implement the random pairing functionality. 