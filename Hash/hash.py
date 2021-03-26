import csv

class HashTable:
    """
    Creates a hash table that allows inserting and updating functions
    """


    def __init__(self, size = 40):
        """
        Constructor for the hash table.
        :param size: Set to 40, the amount of addresses packages will be delivered to
        """
        self.table = []
        for i in range(size):
            self.table.append([])



    def insert(self, key, item):
        """
        Allows items to be inserted into the hash table, and chained to other items if collisions occur
        :param key: The desired placement for the item
        :param item: The item being placed into the hash table. In this case, packages.
        :return: True
        """

        placement = hash(key) % len(self.table)
        list = self.table(placement)


        for kv in list:
            if kv[0] == key:
                kv[1] == item
                return True

        kValue = [key, item]
        list.append(kValue)
        return True


    def lookup(self, key):
        """
        Searches the hash for an item via the input key
        :param key: The location being searched
        :return: item or None
        """

        placement = hash(key) % len(self.table)
        list = self.table(placement)

        for kValue in list:
            if kValue[0] == key:
                return kValue[1]
            return None




