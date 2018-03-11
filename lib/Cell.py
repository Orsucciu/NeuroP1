from lib.Connexion import Connexion

class Cell:
    cellCount = 0

    def __init__(self, capaId):
        #Neurons constructor

        self.name = "cell" + str(Cell.cellCount) #+ "->Capa" + str(capaId) #this is kinda useless. see later
        self.connexionsIn = []
        self.connexionsOut = []
        self.threshold = None
        self.state = 0  # this represent the "out" of cell, in the sense is it activated, what is it outputing

        Cell.cellCount += 1
        #Cell.cellCount = 1 + (capaId * 10)

    def toString(self):
        #prints out info about the neuron
        print("Cell " + self.name)
        for connexion in self.connexionsOut:
            print("To " + connexion.destination.name + " Weight : " + str(connexion.weight))
        for connexion in self.connexionsIn:
            print("From " + connexion.destination.name + " Weight : " + str(connexion.weight))

    def cell_InmcCP(self):
        # gets the sum of values "in" (c
        suma_In = 0
        for connexion in self.connexionsIn:
            if (connexion.destination is self):
                suma_In += connexion.weight * connexion.origin.state
        return suma_In

    def fdt_mcCP(self):
        #function de transferencia por mccullochs pitts
        #sets the cell value
        result = self.cell_InmcCP()
        if (result > self.threshold):
            self.salida = 1
        elif (result < self.threshold):
            self.salida = 0
        else:
            self.salida = 0

    def activate_mcCP(self):
        # used for the entry layer; simply set salida to 1
        self.salida = 1
