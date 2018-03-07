from lib.Red import Red

rede = Red("r1")
rede.initCapas([2, 3, 3, 2])
rede.connectOneToAll(2)
rede.toString()

