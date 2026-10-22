import random

candies = ["starburst", "skittles", "milkyway", "jolly rancher", "Reese's", "Hershey's", "Snickers", "Kit Kat", "Twix", "Gummybears"]

class Student():
    # attributes
    name = ""
    candy = ""

    # constructor
    def __init__(self, my_list: list):
        self.preferences = {}
        self.name = random.choice(my_list)
        for i in candies:
            self.preferences[i] = random.randint(0, 10)
        self.candy = random.choice(candies)

    # getters
    def get_preferences(self):                              
        return self.preferences

    def get_candy(self):
        return self.candy
    
    # setters
    def set_preferences(self, preferences: dict):
        self.preferences = preferences

    def set_candy(self, candy: str):
        self.candy = candy

    # trading behavior
    def trade(self, peer: "Student"):
        print(f"{self.name} {self.candy} {self.preferences[self.candy]} - {self.name} {peer.candy} {self.preferences[peer.candy]}")
        if self.preferences[peer.candy] > self.preferences[self.candy]:
            print(f"{self.name} trade: TRUE")
            return True
        else:
            print(f"{self.name} trade: FALSE")
            return False


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
    shuffled_classroom = classroom.copy()
    random.shuffle(shuffled_classroom)
    pairs = [(shuffled_classroom[i], shuffled_classroom[i+1]) for i in range(0, len(shuffled_classroom), 2)]    # Why use range() instead of just the shuffled classroom directly?
    return pairs

def run_trading_round(classroom: list):
    # segment into pairs
    pairs = assign_pairs(classroom)

    # trading functionality
    for pair in pairs:
        print("-------------------------------------------------------------\n")
        if pair[0].trade(pair[1]) and pair[1].trade(pair[0]):
            # swap candies
            placeholder = pair[0].candy
            pair[0].set_candy(pair[1].candy)
            pair[1].set_candy(placeholder)

def main():
    total_utility = 0
    classroom = read_file("students.txt")

    for student in classroom:
        total_utility += student.preferences[student.candy]
    print(f"Total Utility: {total_utility}")
    run_trading_round(classroom)
    total_utility = 0
    for student in classroom:
            total_utility += student.preferences[student.candy]
    print("-------------------------------------------------------------\n")
    print(f"Total Utility: {total_utility}")


if __name__ == "__main__":
    main()

# Questions:
# Why do getters need an argument to self?
# How does an "if __name__ == "__main__" block work?
# Is random.choice() with or without replacement?

# Notes for future changes
# Make it so that classrooms can only have an even number of students since they trade in pairs.
# Think about the best way to implement the random pairing functionality. 

# Debugging
# Candies are not switching. Why?
# It looks like the trade's are not executing because both trading conditions are not returning True.
# Why is each trading partner's candy preference the inverse of the other? This should not be the case?
# It looks like the issue is that all of the students have the same preferences. Why is this?
# Gemini says this could be because I defined the dictionary as a class attribute. Interesting, I didn't know that. 
# That seems to have been it. The dictionary must be declared within the constructor. How strange.