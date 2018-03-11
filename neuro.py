from lib.Red import Red

# redeTemp = Red("temperature")
# redeTemp.initCapas([2, 2, 2])
# redeTemp.setAllThresholdTo(2)
# redeTemp.createConnexion([0, 0], [2, 0], 2)
#
# redeTemp.createConnexion([0, 1], [1, 0], -1)
# redeTemp.createConnexion([0, 1], [1, 1], 2)
# redeTemp.createConnexion([0, 1], [2, 1], 1)
#
# redeTemp.createConnexion([1, 0], [2, 0], 2)
#
# redeTemp.createConnexion([1, 1], [1, 0], 2)
# redeTemp.createConnexion([1, 1], [2, 1], 1)
# redeTemp.generateGraph()

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
a = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
for i in range(0, len(a)):
    retu.activateMcCP(a[i])
