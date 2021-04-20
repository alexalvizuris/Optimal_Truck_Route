import csv
from graph import *
from packages import *

def loadPackages(file, hash):
    """
    Loads package data from the csv file into the hash file passed as an argument
    :param file: csv file for packages
    :param hash: hashtable created to store package info
    """
    with open(file) as packageLoad:
        packageInfo = csv.reader(packageLoad, delimiter =",")
        for i in packageInfo:
            packageID = int(i[0])
            pCurrent_Node = int(i[1])
            pAddress = i[2]
            pCity = i[3]
            pState = i[4]
            pZip = i[5]
            pDeadline = int(i[6])
            pWeight = int(i[7])
            pStatus = "At Hub"

            pack = Package(packageID, pCurrent_Node, pAddress, pCity, pState, pZip, pDeadline, pWeight, pStatus)

            hash.insert(packageID, pack)


def loadDistances_v(file, graph):
    """
    Loads the distance data from the csv file into the matrix as vertices
    :param file: the distances.cvs file
    :param graph: graph instance
    """

    with open(file) as distanceRange:
        reader = csv.reader(distanceRange, delimiter = ",")
        for row in reader:
            id = int(row[0])

            address = row[2]
            city = row[3]
            state = row[4]
            zip = row[5]

            vertex = Vertex(id, address, city, state, zip)
            graph.add_v(vertex)

    return graph



def loadDistances_e(file, graph):
    """
    Takes in the distances csv file and loads the edge weights between vertices into the matrix
    :param file: the distances.csv file
    :param graph: graph instance
    """

    with open(file) as distanceRange:
        reader = csv.reader(distanceRange, delimiter = ",")
        for row in reader:
            v1 = int(row[0])
            for x in range(27):
                v2 = x
                weight = row[x]
                graph.add_e(v1, v2, weight)

    return graph






