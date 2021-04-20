class Package:
    """
    Creates a package class that includes details of the package and destination
    """

    def __init__(self, ID, current_node, address, city, state, zipcode, deadline, weight, status):
        """
        Constructor for the package class
        :param ID: package ID
        :param address: delivery address for package
        :param deadline: time constraints for package
        :param city: city of address for delivery
        :param zipcode: zipcode of address for delivery
        :param weight: weight of package
        :param status: current status of package
        """
        self.ID = ID
        self.current_node = current_node
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.departed = 0.0
        self.delivered_at = 0.0

    def __str__(self):
        """
        Creates string method for package class
        :return: package info as string
        """
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.ID, self.current_node, self.address, self.city, self.state, self.zipcode, self.deadline, self.weight, self.status, self.departed, self.delivered_at)
