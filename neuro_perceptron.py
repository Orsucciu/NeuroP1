from lib.Red import Red
import sys

retu = Red("perceptron")
retu.initCapas([2, 2])
retu.connectOneToAll(0)
retu.addCell(0, "bias0", 1)
retu.addCell(0, "bias1", 1)
retu.createConnexion([0, 2], [1, 0], 0)
retu.createConnexion([0, 3], [1, 1], 0)
# we have 2 neurons in + bias, and two neurons out
retu.setAllThresholdTo(0.2)
retu.generateGraph()

retu.trainPerceptron(retu.processText("and.txt"), 1)
retu.exploitPerceptron(retu.processText("and.txt"))
retu.generateGraph()
