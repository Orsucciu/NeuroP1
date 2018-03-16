from lib.Red import Red
import sys

retu = Red("Adaline")
retu.initCapas([3, 1])
# we have 2 neurons in + bias, and one neurons out
retu.connectOneToAll(0)
retu.setAllThresholdTo(0.2)
retu.generateGraph()

retu.trainAdaline(retu.processText("and.txt"), 0.1, 2)
retu.exploitAdaline(retu.processText("and.txt"))
