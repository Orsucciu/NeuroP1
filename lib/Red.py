from __future__ import print_function

from lib.Connexion import Connexion
from lib.Cell import Cell
from lib.Capa import Capa
import pickle  # will later be used to save and load the network
import os, sys
from PIL import Image, ImageDraw, ImageFont, ImageOps


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
        # this create a create a connexion from each cell from each layer to each cell from the next layer
        # (except the last layer of course)
        # the weight will be the same everywhere

        for capa in range(0, len(self.capas) - 1):
            for cell in self.capas[capa].cells:
                for cell2 in self.capas[(capa + 1)].cells:
                    self.cr(cell, cell2, weight)

    def cr(self, cellOrigin, cellDestination, weight):
        # not destined to be used by human
        # made for connecToAll
        # this create a connexion between two given cells
        connexion = Connexion(cellOrigin, cellDestination, weight)
        cellOrigin.connexionsOut.append(connexion)
        cellDestination.connexionsIn.append(connexion)

    def createConnexion(self, origin, destination, peso):
        # create a connexion from a cell to another, and sets the weight of said connexion
        # this is for a given network, so origin is an array [int, int] with [capa num, cell num], and same for destination.
        connexion = Connexion(self.capas[origin[0]].cells[origin[1]], self.capas[destination[0]].cells[destination[1]], peso)

        self.capas[origin[0]].cells[origin[1]].connexionsOut.append(connexion)
        self.capas[destination[0]].cells[destination[1]].connexionsIn.append(connexion)

    def setAllThresholdTo(self, value):
        # this is a function to change the threshold of all the cells at once
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

    def resetStates(self):
        # reset all states to 0
        for capa in self.capas:
            for cell in capa.cells:
                cell.state = 0

    def activeCells(self):
        # return all cells with state = 1
        for capa in self.capas:
            for cell in capa.cells:
                if cell.state == 1:
                    print(capa.name + " " + cell.name)

    def activateMcCP(self, values, outname):
        # [value] is, an array representing the neurons from first layer to trigger.
        # this function is kinda specific, because we needed to retain the second layers values
        result = ""
        for value in values:

            for i in range(0, len(self.capas[1].cells)):
                self.capas[1].cells[i].state = int(self.capas[0].cells[i].state)

            for i in range(0, len(self.capas[0].cells)):
                # init first layer
                self.capas[0].cells[i].state = int(value[i])

            for i in range(2, len(self.capas)):
                # main loop filling other layers
                for cell in self.capas[i].cells:
                    total_in = 0
                    for connexion in cell.connexionsIn:
                        if connexion.origin.state == 1:
                            total_in += connexion.weight * connexion.origin.state

                    if total_in >= cell.threshold:
                        cell.state = 1
                    else:
                        cell.state = 0

            for cell in self.capas[len(self.capas) - 1].cells:
                result += str(cell.state)
            result += "\n"

        text_file = open(outname + ".txt", "w")
        text_file.write(result)
        text_file.close()
        print(result)

    ####
    #
    # The following is ONLY about graph making
    #
    ####

    def getBiggestCells(self):
        # this is only useful for the graph drawing
        # it returns the numbers of cells from the biggest layer
        biggest = 0
        for capa in self.capas:
            if(len(capa.cells) > biggest):
                biggest = len(capa.cells)
        return biggest

    def getCellColumn(self, cell):
        # util for the graph making, used when drawing line between cells
        # returns an int representing the cell's capa number (and thus how far the drawn line must go)
        for num in range(0, len(self.capas)):
            for Ccell in self.capas[num].cells:
                if cell is Ccell:
                    return num

    def generateGraph(self, fileName=None):
        # BUGGY AS HELL
        # Doing this kind of thing without any library is kinda diffcult
        if(fileName == None):
            fileName = self.name
        # this will generate an image representing the network at the current state
        im = Image.new('RGB', (len(self.capas) * 300, self.getBiggestCells() * 200), "white") # creates a white image of given size
        draw = ImageDraw.Draw(im)

        x = 30
        y = 30
        for capa in self.capas:
            # we first draw the capas as rectangles
            draw.rectangle(((x, y), (x + 180, y + 45)), None, "black")
            draw.text((x + 7, y + 7), capa.name, fill="black", font=ImageFont.truetype("arial", 18))

            circleY = y
            for cell in capa.cells:
                # we draw the cells as circles with their name and threshold
                draw.ellipse(((x, circleY + 60), (x + 120, circleY + 150)), outline="black")
                draw.text((x + 30, circleY + 68), cell.name, fill="black", font=ImageFont.truetype("arial", 18))
                draw.text((x + 30, circleY + 98), "<" + str(cell.threshold) + ">", fill="black", font=ImageFont.truetype("arial", 18))

                connexionY = circleY + 105
                altPos = 0
                for connexion in cell.connexionsOut:
                    # we finally draw the connexion between each cells, as lines, along with the weight

                    # for the line drawing logic, we have a problem to draw a vertical one so we need this
                    if self.getCellColumn(connexion.origin) == self.getCellColumn(connexion.destination):

                        draw.line(((x + 105, connexionY), (90 + x,
                                                           (1 + abs(int(connexion.destination.name[-1]) - int(connexion.origin.name[-1])) * 150))),
                                  fill='black', width=1)
                        draw.ellipse(((x + 80, (1 + abs(int(connexion.destination.name[-1]) - int(connexion.origin.name[-1])) * 70)), (x + 90, (1 + int(connexion.destination.name[-1]) * 70) + 10)), fill='black', outline='black')

                    else:
                        draw.line(((x + 105, connexionY), ((self.getCellColumn(connexion.destination) - self.getCellColumn(connexion.origin)) * 315 + x, (1 + int(connexion.destination.name[-1])) * 150)), fill="black", width=1)
                        draw.ellipse(((x + ((self.getCellColumn(connexion.destination) - self.getCellColumn(connexion.origin)) * 310), ((1 + int(connexion.destination.name[-1])) * 150) - 5), (x + ((self.getCellColumn(connexion.destination) - self.getCellColumn(connexion.origin)) * 320), ((1 + int(connexion.destination.name[-1])) * 150) + 10)), fill="black", outline="black") # this is meant to represent the destination

                circleY = circleY + 150

            x = x + 300

        del draw
        # write to stdout
        im.save(str(fileName) + ".png")