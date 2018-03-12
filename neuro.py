from lib.Red import Red
import sys

retu = Red("UpOrDown")
retu.initCapas([3, 3, 6, 2])
retu.setAllThresholdTo(2)
retu.createConnexion([0, 0], [1, 0], 2)
retu.createConnexion([0, 1], [1, 1], 2)
retu.createConnexion([0, 2], [1, 2], 2)

retu.createConnexion([0, 0], [2, 0], 1)
retu.createConnexion([1, 1], [2, 0], 1)

retu.createConnexion([0, 1], [2, 1], 1)
retu.createConnexion([1, 2], [2, 1], 1)

retu.createConnexion([0, 2], [2, 2], 1)
retu.createConnexion([1, 0], [2, 2], 1)

retu.createConnexion([0, 2], [2, 3], 1)
retu.createConnexion([1, 1], [2, 3], 1)

retu.createConnexion([0, 1], [2, 4], 1)
retu.createConnexion([1, 0], [2, 4], 1)

retu.createConnexion([0, 0], [2, 5], 1)
retu.createConnexion([1, 2], [2, 5], 1)

retu.createConnexion([2, 0], [3, 0], 2)
retu.createConnexion([2, 1], [3, 0], 2)
retu.createConnexion([2, 2], [3, 0], 2)

retu.createConnexion([2, 3], [3, 1], 2)
retu.createConnexion([2, 4], [3, 1], 2)
retu.createConnexion([2, 5], [3, 1], 2)
retu.generateGraph()

a = []
file = open(sys.argv[1], "r")
line = file.readline()
while line:
    temp = []
    for i in range(0, 2):
        temp.append(line[i])

    a.append(line)
    line = file.readline()
file.close()

retu.resetStates()
retu.activateMcCP(a, sys.argv[2])
