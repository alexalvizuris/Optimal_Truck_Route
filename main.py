from hash import *
from csvMethods import *
from algorithm import *

packageHash = HashTable()
loadPackages('packages.csv', packageHash)
loadAdresses('addresses.csv')


def getPackageInfo():
    for i in range (len(packageHash.table) +1):
        print('Package: {}'.format(packageHash.lookup(i+1)))



def add_lookup():
    add_list = loadAdresses('addresses.csv')
    search = input("Type an address: ")
    count = 0

    for i in add_list:
         if search == i:
            count += 1
            return add_list.index(i)


truck1 = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
truck2 = [2, 3, 4, 5, 6, 7, 8, 9, 18, 25, 28, 32, 36, 38]
truck3 = [10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]

# distanceMatrix = loadDistances('distances.csv')









