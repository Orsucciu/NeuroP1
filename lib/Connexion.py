class Connexion:

    def __init__(self, origin, destination, weight):
        #constructor for a connexion

        self.origin = origin
        self.destination = destination
        self.weight = weight
        self.value = 0
        self.name = origin.name + " " + destination.name

    def toString(self):
        print("From " + self.origin.name + " To " + self.destination.name + " Weight : " + str(
            self.weight) + " Value : " + str(self.value))

    def resetValue(self):
        self.value = 0

    def setValue(self):
        self.value = self.origin.salida * self.weight

    def updateWeight(self, weight):
        self.weight = weight
