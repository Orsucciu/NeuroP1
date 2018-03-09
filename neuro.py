from lib.Red import Red

rede = Red("r1")
rede.initCapas([2, 3, 3, 2])
rede.connectOneToAll(2)
rede.toString()

redeTemp = Red("temperature")
redeTemp.initCapas([2, 2, 2])
redeTemp.setAllThresholdTo(2)
redeTemp.createConnexion([0, 0], [2, 0], 2)

redeTemp.createConnexion([0, 1], [1, 0], -1)
redeTemp.createConnexion([0, 1], [1, 1], 2)
redeTemp.createConnexion([0, 1], [2, 1], 1)

redeTemp.createConnexion([1, 0], [2, 0], 2)

redeTemp.createConnexion([1, 1], [1, 0], 2)
redeTemp.createConnexion([1, 1], [2, 1], 1)
redeTemp.generateGraph()

