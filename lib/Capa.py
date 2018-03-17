from lib.Cell import Cell


class Capa:
    cellCount = 0
    capaCount = 0

    def __init__(self, id=None, cellNumber=0):
        # init with an id and the number of cells
        if id == None:
            self.name = "capa" + str(Capa.capaCount)
        else:
            self.name = "capa" + str(id)
        self.numCells = cellNumber
        if cellNumber != 0:
            self.cells = [None] * cellNumber  # this initiate an array full of nulls

            for i in range(0, cellNumber):
                self.cells[i] = Cell()
            Cell.cellCount = 0

        else:
            self.cells = []
        Capa.capaCount += 1

    def addSpecificCell(self, cell):
        self.cells.append(cell)
        self.numCells += 1

    def toString(self):
        print("Capa " + self.name)
        for cell in self.cells:
            print(cell.toString())
