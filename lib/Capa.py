from lib.Cell import Cell

class Capa:
    cellCount = 0
    capaCount = 0

    def __init__(self):
        #init without params
        self.name = "capa" + str(Capa.capaCount)
        self.numCells = 0
        self.cells = []

        Capa.capaCount += 1

    def __init__(self, id, cellNumber):
        #init with an id and the number of cells
        self.name = id
        self.numCells = cellNumber
        self.cells[cellNumber]

        for i in range(0, cellNumber):
            self.cells[i] = Cell(id)

        Capa.capaCount += 1

    def addSpecificCell(self, cell):
        self.cells.append(cell)
        self.numCells +=1

    def toString(self):
        print("Capa " + self.name)
        for cell in self.cells:
            print(cell.toString())

    '''
        def __init__(self, cells):
            #init with a list of cells
            self.name = "capa" + str(Capa.capaCount)
            self.cells = []

            for cell in cells:
                self.addCell(cell)

            Capa.cellCount += 1
    '''

