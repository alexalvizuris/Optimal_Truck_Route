from hash import *
from csvMethods import *
from packages import *
from graph import *

packageHash = HashTable()
all_packages = loadPackages('packages.csv', packageHash)

graph1 = Graph()


def getPackageInfo():
    for i in range (len(packageHash.table) +1):
        print('Package: {}'.format(packageHash.lookup(i+1)))





































