import datetime


class Truck:
    """
    Creates a truck class that includes information regarding the truck and its contents
    """

    def __init__(self):
        """
        constructor for the truck class
        :param location: trucks current location
        :param time: timestamp
        :param departure: time of departure from Hub
        :param mileage: mileage consumed by truck en route
        """

        self.location = "HUB"
        self.time = datetime.datetime(2021, 4, 15, 8, 1, 1)
        self.departure = datetime.datetime(2021, 4, 15, 8, 1, 1)
        self.mileage = 0
        self.package_list = []







