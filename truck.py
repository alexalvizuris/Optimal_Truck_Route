class Truck:
    """
    Creates a truck class that includes information regarding the truck and its contents
    """

    def __init__(self, location, time, departure, mileage):
        """
        constructor for the truck class
        :param location: trucks current location
        :param time: timestamp
        :param departure: time of departure from Hub
        :param mileage: mileage consumed by truck en route
        """

        self.location = location
        self.time = time
        self.departure = departure
        self.mileage = mileage

    # possible string method here