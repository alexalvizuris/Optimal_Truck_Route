from hash import *
from csvMethods import *
from algorithm import *
from truck import *

packageHash = HashTable()
all_packages = loadPackages('packages.csv', packageHash)




def getPackageInfo():
    for i in range (len(packageHash.table) +1):
        print('Package: {}'.format(packageHash.lookup(i+1)))


truck1 = Truck()
truck2 = Truck()
truck3 = Truck()


def load_truck():
    truck1.package_list = [1, 13, 14, 15, 16, 19, 20, 29, 30, 31, 34, 37, 40]
    truck2.package_list = [2, 3, 4, 5, 6, 7, 8, 9, 18, 25, 28, 32, 36, 38]
    truck3.package_list = [10, 11, 12, 17, 21, 22, 23, 24, 26, 27, 33, 35, 39]


load_truck()































