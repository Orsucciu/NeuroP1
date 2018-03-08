from __future__ import print_function

from lib.Connexion import Connexion
from lib.Cell import Cell
from lib.Capa import Capa
import pickle  # will later be used to save and load the network
import os, sys
from PIL import Image, ImageDraw, ImageFont


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
        # create a connexion from a cell to another, and sets the weight of said connexion
        connexion = Connexion(origin, destination, peso)

        origin.connexionsOut.append(connexion)
        destination.connexionsIn.append(connexion)

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

    def generateGraph(self, fileName):
        # this will generate an image representing the network at the current state
        im = Image.new('RGB', (1000, 400), "white") # creates a white image of given size
        draw = ImageDraw.Draw(im)

        x = 20
        y = 20
        for capa in self.capas:
            # we first draw the capas as rectangles
            draw.rectangle(((x, y), (x + 120, y + 30)), None, "black")
            draw.text((x + 5, y + 5), capa.name, fill="black", font=ImageFont.truetype("arial", 18))

            circleY = y
            for cell in capa.cells:
                # we draw the cells as circles with their name and threshold
                draw.ellipse(((x, circleY + 40), (x + 80, circleY + 100)), outline="black")
                draw.text((x + 20, circleY + 45), cell.name, fill="black", font=ImageFont.truetype("arial", 18))
                draw.text((x + 20, circleY + 65), "<" + str(cell.threshold) + ">", fill="black", font=ImageFont.truetype("arial", 18))

                connexionY = circleY + 70
                for connexion in cell.connexionsOut:
                    # we finalle draw the connexion between each cells, as lines
                    # draw.text((x + 20, circleY + 65), "<To : " + str(connexion.destination.name) + " Weight : " + str(connexion.weight) + ">", fill="black", font=ImageFont.truetype("arial", 10))
                    draw.line(((x + 70, connexionY), (x + 210, (1 + int(connexion.destination.name[-1])) * 100)), fill="black", width=1)
                    draw.ellipse(((x + 205, (1 + int(connexion.destination.name[-1])) * 100), (x + 210, ((1 + int(connexion.destination.name[-1])) * 100)) + 5), fill="black", outline="black")

                circleY = circleY + 100

            x = x + 200

        del draw
        # write to stdout
        im.save(str(fileName) + ".png")