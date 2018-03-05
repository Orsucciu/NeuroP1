from lib.Connexion import Connexion
from lib.Cell import Cell
from lib.Capa import Capa

class Red:

    def __init__(self, name):
        self.name = name
        self.capas = []

    def initCapas(self, capas):
        #capas in an array of ints
        for index in range (0, len(capas)):
            self.capas.append(Capa(index+1, capas[index]))

    def addConnexionOut(self, destination):
        #add a connnexion from the cell to another one
        #take a cell as param (the destination)
        self.connexionsOut.append(Connexion(self, destination, 1))
        #destination.addConexionIn(self)
        destination.connexionsIn.append(Connexion(self, destination, 1))

    def addConnexionIn(self, origin):
        #add a connexion from another cell to this one
        #take a cell as param (the origin)
        self.connexionsIn.append(Connexion(origin, self, 1))
        #origin.addConnexionOut(self)
        origin.connexionsOut.append(Connexion(self, origin, 1))

    def createConnexion(self, origin, destination, peso):

        Connexion(origin, destination, peso)

        origin.connexionsOut.append()
        destination.connexionsIn.append(Connexion(origin, destination, peso))