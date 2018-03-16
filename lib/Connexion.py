class Connexion:

    def __init__(self, origin, destination, weight=0):
        #constructor for a connexion

        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.name = str(origin.name) + " " + str(destination.name)

    def toString(self):
        print("From " + self.origin.name + " To " + self.destination.name + " Weight : " + str(
            self.weight) + " Value : " + str(self.value))

    def updateWeight(self, weight):
        self.weight = weight
