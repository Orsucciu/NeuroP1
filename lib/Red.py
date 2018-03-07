from lib.Connexion import Connexion
from lib.Cell import Cell
from lib.Capa import Capa
import pickle # will later be used to save and load the network

class Red:

    def __init__(self, name):
        self.name = name
        self.capas = []

    def initCapas(self, capas):
        # this creates the number of layers we want, and fill them with cells
        # capas is an array of ints
        for index in range(0, len(capas)):
            self.capas.append(Capa(index + 1, capas[index]))

    def connectOneToAll(self, weight):
        # this create a create a connexion from each cell from each layer to each cell from the next layer (except the last layer of course
        # the weight will be the same everywhere

        for capa in range(0, len(self.capas) - 1):
            for cell in self.capas[capa].cells:
                for cell2 in self.capas[(capa + 1)].cells:
                    self.createConnexion(cell, cell2, weight)


    # def addConnexionOut(self, destination):
    #     # add a connnexion from the cell to another one
    #     # take a cell as param (the destination)
    #     self.connexionsOut.append(Connexion(self, destination, 1))
    #     # destination.addConexionIn(self)
    #     destination.connexionsIn.append(Connexion(self, destination, 1))
    #
    # def addConnexionIn(self, origin):
    #     # add a connexion from another cell to this one
    #     # take a cell as param (the origin)
    #     self.connexionsIn.append(Connexion(origin, self, 1))
    #     # origin.addConnexionOut(self)
    #     origin.connexionsOut.append(Connexion(self, origin, 1))

    def createConnexion(self, origin, destination, peso):
        #create a connexion from a cell to another, and sets the weight of said connexion
        connexion = Connexion(origin, destination, peso)

        origin.connexionsOut.append(connexion)
        destination.connexionsIn.append(connexion)

    def setAllThresholdTo(self, value):
        #this is a function to change the threshold of all the cells at once
        for capa in self.capas:
            for cell in capa.cells:
                cell.threshold = value

    def toString(self):
        # this will display the network in line (not as good as an image tho)
        for capa in self.capas:
            final = str(capa.name) + "[ "
            for cell in capa.cells:
                final += " " + str(cell.name)
            final += " ]\n"
            print(final)
