from lib.Connexion import Connexion

class Cell:
    cellCount = 0

    def __init__(self, capaId):
        #Neurons constructor

        self.name = "cell" + str(Cell.cellCount) #+ "->Capa" + str(capaId) #this is kinda useless. see later
        self.connexionsIn = []
        self.connexionsOut = []
        self.salida = 0
        self.threshold = 0.2
        #self.state = 0

        Cell.cellCount += 1
        #Cell.cellCount = 1 + (capaId * 10)

    def updateSalida(self, value):
        self.salida += value

    def toString(self):
        #prints out info about the neuron
        print("Cell " + self.name)
        for connexion in self.connexionsOut:
            print("To " + connexion.destination.name + " Weight : " + str(connexion.weight))
        for connexion in self.connexionsIn:
            print("From " + connexion.destination.name + " Weight : " + str(connexion.weight))

    def cell_In(self):
        suma_In = 0
        for connexion in self.connexionsIn:
            if (connexion.destination == self):
                suma_In += connexion.value
                connexion.resetValue()
        return suma_In

    def cell_fdt(self):
        #function de transferencia por mccullochs pitts
        #sets the cell value
        result = self.cell_In()
        if (result > self.threshold):
            self.salida = 1
        elif (result < self.threshold):
            self.salida = -1
        else:
            self.salida = 0

'''
    def init_Connexion(self):
        for connexion in self.connexionsOut:
            connexion.value = self.cell_Out() * connexion.weight
'''
