from hash import *
from csvMethods import *

packageHash = HashTable()
loadPackages('packages.csv', packageHash)


def getPackageInfo():
    for i in range (len(packageHash.table) +1):
        print('Package: {}'.format(packageHash.lookup(i+1)))


getPackageInfo()

