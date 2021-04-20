from packages import *
from truck import *

def min_to_hour(minutes):
    """
    converts input minutes to HH:MM format
    :param minutes: input integer representative of minutes
    :return: HH:MM 12hr formatting
    """
    hour = int(minutes / 60)
    minute = minutes % 60
    if minutes < 720:
        ampm = "AM"
        time = "%d:%02d" % (hour, minute)
    else:
        ampm = "PM"
        time = '%d:%02d' % (hour - 12, minute)

    return time + ' ' + ampm


def reverse_min(time):
    """
    converts input HH:MM into minutes
    :param time: input HH:MM
    :return: HH:MM in minutes format
    """
    parse = time.split(':')
    hour = parse[0]
    splitting = parse[1].split(' ')
    minute = splitting[0]
    ampm = splitting[1]

    minutes = float(hour) * 60 + float(minute)

    if ampm.upper() == "AM":
        return minutes
    elif ampm.upper() == 'PM':
        return minutes + 720


def delivery_route(package_list, graph, truck):
    """
    BIG O(N^2) greedy algorithm takes input and determines route for package delivery
    :param package_list: list of package IDs that will be delivered during algorithm
    :param graph: representation for addresses to be visited
    :param truck: object carrying the packages.
    """
    while package_list:
        current_package = package_list[0]
        for package in package_list:
            if graph.dist(truck.current_node, package.current_node) < graph.dist(truck.current_node, current_package.current_node):
                current_package = package

        # distance variable representing distance between 2 nodes selected
        distance = float(graph.dist(truck.current_node, current_package.current_node))
        # incrementing the truck mileage by the amount of distance passed
        truck.mileage += distance
        # selected node will be trucks current node
        truck.current_node = current_package.current_node
        # incrementing the time passed for the truck object
        truck.time += distance / truck.speed
        # updating the delivery time of the package to the trucks current time
        current_package.delivered_at = truck.time

        # updating the status of the delivered package
        current_package.status = "Package has been delivered."



        # removing the current package from the truck object's list of packages
        package_list.remove(current_package)


def hub_distance(truck, graph):
    """
    increments the truck object with the miles and time passed by returning to the hub
    :param truck: truck object
    :param graph: nodes with distances between addresses
    :return:
    """
    distance = float(graph.dist(truck.current_node, 1))
    truck.mileage += distance
    truck.time += distance / truck.speed


def lookup(package, time):
    """
    takes a selected package ID and time as input and returns package information including delivery status
    :param package: input package
    :param time: input time of inquire
    :return: package details and delivery status
    """
    package_details = "\nPackage ID: " + str(package.ID) + " Address: " + str(package.address) + ", " + str(package.city) + \
                      ", " + str(package.zipcode) + " Deadline: " + str(min_to_hour(package.deadline)) + " Weight: " + \
                      str(package.weight) + ' Delivery Status: '

    if package is not None:
        if time < package.departed:
            status = package_details + 'At The Hub'
            return status
        elif package.delivered_at > time > package.departed:
            status = package_details + 'En Route'
            return status
        elif time >= package.delivered_at:
            return package_details + package.status + " at " + min_to_hour(package.delivered_at)











