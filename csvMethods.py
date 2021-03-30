import csv

class Package:
    """
    Creates a package class that includes details of the package and destination
    """

    def __init__(self, ID, address, city, state, zipcode, deadline, weight, notes):
        """
        constructor for the package class
        :param ID: package ID
        :param address: delivery address for pckage
        :param deadline: time constraints for package
        :param city: city of address for delivery
        :param zipcode: zipcode of address for delivery
        :param weight: weight of package
        :param notes: special requirements for package
        """
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.notes = notes

    def __str__(self):
        """
        creates string method for package class
        :return: package info as string
        """
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.notes)


def loadPackages(file, hash):
    """
    loads packages into hash file
    :param file: csv file for packages
    :param hash: hashtable created to store package info
    :return: true
    """
    with open(file) as packageLoad:
        packageInfo = csv.reader(packageLoad, delimiter =",")
        for i in packageInfo:
            packageID = int(i[0])
            pAddress = i[1]
            pCity = i[2]
            pState = i[3]
            pZip = i[4]
            pDeadline = i[5]
            pWeight = i[6]
            pNotes = i[7]

            pack = Package(packageID, pAddress, pCity, pState, pZip, pDeadline, pWeight, pNotes)

            hash.insert(packageID, pack)


def loadDistances(file):
    """
    loads the distances csv information into a 2D array
    :param file: the distances.cvs file
    :return: 2D array of distances
    """
    data = []
    with open(file) as distanceRange:
        reader = csv.reader(distanceRange, delimiter = ",")
        for row in reader:
            data.append(row)

    print(data)



def loadAdresses(file):
    """
    loads the addresses from the imprted address csv file
    :param file: the csv file containing the addresses that are searchable
    :return: list of addresses
    """
    addresses = []

    with open(file) as addressList:
        reader = csv.reader(addressList, delimiter = ',')
        for row in reader:
            addresses.append(row)
    return addresses








