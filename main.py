from hash import *
from csvMethods import *

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







getPackageInfo()
loadDistances('distances.csv')
add_lookup()






