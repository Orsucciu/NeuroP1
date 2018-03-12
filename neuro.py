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

if(sys.argv[1] == "mp_help"):
    print("This program is desgined to be used this way : 'program.py [name of the file to read the data from] [name of the file to output the data]'")
    print("This program output the data as .txt, no need to specify it")

elif(sys.argv[1] == "mp_exec"):
    print("This program will now work with a preexisting set of data (it will be outputed as ex1.txt, and the results as ex1_result.txt)")

    text_file = open("ex1.txt", "w")
    text_file.write("100\n010\n001\n000\n001\n001\n010\n100\n")
    text_file.close()

    a = []
    file = open("ex1.txt", "r")
    line = file.readline()
    while line:
        temp = []
        for i in range(0, 3):
            temp.append(int(line[i]))

        a.append(temp)
        line = file.readline()
    file.close()

    retu.resetStates()
    retu.activateMcCP(a, "ex1_result")

else:
    a = []
    file = open(sys.argv[1], "r")
    line = file.readline()
    while line:
        temp = []
        for i in range(0, 3):
            temp.append(int(line[i]))

        a.append(temp)
        line = file.readline()
    file.close()

    retu.resetStates()
    retu.activateMcCP(a, sys.argv[2])
