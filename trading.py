import random

candies = ["starburst", "skittles", "milkyway", "jolly rancher", "Reese's", "Hershey's", "Snickers", "Kit Kat", "Twix", "Gummybears"]

class student():
    # attributes
    preferences = {}
    candy = ""

    # constructor
    def __init__(self):
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

# def main():
#     for i in range(30):

# if __name__ == "__main__":
#     main()

# Questions:
# Why do getters need an argument to self?
# How does an "if __name__ == "__main__" block work?
