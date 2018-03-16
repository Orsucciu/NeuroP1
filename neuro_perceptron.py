from lib.Red import Red
import sys

retu = Red("perceptron")
retu.initCapas([2, 2])
retu.connectOneToAll(0)
retu.addCell(0, "bias1", 1)
retu.addCell(0, "bias2", 1)
retu.createConnexion(retu.capas[0].cells[2], retu.capas[1].cells[0])
retu.createConnexion(retu.capas[0].cells[2], retu.capas[1].cells[1])
# we have 2 neurons in + bias, and two neurons out
retu.setAllThresholdTo(0.2)
retu.generateGraph()

retu.trainPerceptron(retu.processText("and.txt"), 1)
retu.exploitPerceptron(retu.processText("and.txt"))
