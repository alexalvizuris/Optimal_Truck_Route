from hash import *
from csvMethods import *
from packages import *
from graph import *
from truck import *
from algorithm import *
import re


class Main:
    """
    Main class for the Optimal_Truck_Route project. Initializes the Package hashtable and the Graph object.
    Then loads in the data from the distances csv file and creates vertices and edges with that data.
    """
    package_hash = HashTable()
    # Big O(N)
    loadPackages('packages.csv', package_hash)
    graph1 = Graph()
    # Big O(N)
    loadDistances_v('distances.csv', graph1)
    # Big O(N^2)
    loadDistances_e('distances.csv', graph1)


    while True:
        """
        Big O(N)
        This creates the User Interface. The user will have the opportunity to run the program when entering the number 1.
        After the program has been ran, inquiries to specified packages or all packages can be made by selecting either 2 or 3. 
        Entering the number 4 closes the program.
        """
        print('')
        print('Welcome to WGUPS: ')
        print('\nEnter 1 to Run Program\nEnter 2 for Package Inquiry\nEnter 3 for All Statuses\nEnter 4 to Exit.')
        menu_option = input('Please select an option (starting with option 1): ')

        if menu_option == '1':

            # Truck objects are created
            truck1 = Truck()
            truck2 = Truck()

            # Three package lists are created. Packages are then pre-assigned to the package lists using the
            # hashtable look-up function
            # Big O(N) to retrieve packages
            packages1 = [
                package_hash.lookup(1), package_hash.lookup(13), package_hash.lookup(14), package_hash.lookup(15),
                package_hash.lookup(16),
                package_hash.lookup(19), package_hash.lookup(20), package_hash.lookup(29), package_hash.lookup(30),
                package_hash.lookup(31),
                package_hash.lookup(34), package_hash.lookup(37), package_hash.lookup(39), package_hash.lookup(40)
            ]

            packages2 = [
                package_hash.lookup(2), package_hash.lookup(3), package_hash.lookup(4), package_hash.lookup(5),
                package_hash.lookup(6), package_hash.lookup(7),
                package_hash.lookup(8), package_hash.lookup(18), package_hash.lookup(25), package_hash.lookup(28),
                package_hash.lookup(32), package_hash.lookup(36),
                package_hash.lookup(38)
            ]

            packages3 = [
                package_hash.lookup(9), package_hash.lookup(10), package_hash.lookup(11), package_hash.lookup(12),
                package_hash.lookup(17), package_hash.lookup(19),
                package_hash.lookup(22), package_hash.lookup(23), package_hash.lookup(24), package_hash.lookup(26),
                package_hash.lookup(27), package_hash.lookup(33),
                package_hash.lookup(35)
            ]

            # Package lists are MANUALLY assigned to the package objects
            truck1.package_list = packages1
            truck2.package_list = packages2

            # 480 and 545 are minute representations for the times that the trucks will be departing from the hub.
            truck1_departed = 480
            truck2_departed = 545

            # In each of these upcoming For-Loops, a package object has its Departed and Delivery attributes set to the
            # time of departure of the truck that each package is assigned to. The truck object has its time set to the
            # time of departure as well.
            # Then the trucks package list, the graph of vertices and edged, and the truck object are used as arguments
            # in the Delivery Route method.
            for package in truck1.package_list:
                package.delivered_at = truck1_departed
                package.departed = truck1_departed
                package.status = "En Route"
            truck1.time = truck1_departed

            delivery_route(truck1.package_list, graph1, truck1)

            for package in truck2.package_list:
                package.delivered_at = truck2_departed
                package.departed = truck2_departed
                package.status = 'En Route'
            truck2.time = truck2_departed

            delivery_route(truck2.package_list, graph1, truck2)

            # Truck 1 returns back to the Hub
            hub_distance(truck1, graph1)

            # Truck 1 must wait for package 9 to have its address corrected. Truck 1 time is set to 10:25 AM and goes
            # back through the For-Loop with the leftover packages to be delivered.
            truck1.time = 615
            truck1.package_list = packages3

            for package in truck1.package_list:
                package_delivery = truck1.time
                package.departed = truck1.time
                package.status = "En Route"

            delivery_route(truck1.package_list, graph1, truck1)

            print('')
            print('Successfully delivered all packages!')
            print('')
            print('Mileage accrued: ' + str(truck1.mileage + truck2.mileage))
            # When successfully ran, the project's mileage accrued is --> 105.1 miles

        elif menu_option == "2":
            while True:
                # The user types in the ID of a package they would like to inquire about. Entering 0 exits the menu
                # option.
                ID = int(input("Type a Package ID between 1 - 40 (typing 0 Exits the program): "))
                inquiry = package_hash.lookup(int(ID))

                if ID == 0:
                    print('')
                    print('Exiting..')
                    print('')
                    break

                if inquiry is not None:
                    while True:
                        # The user must input a time in which they would like to check the delivery status of the
                        # package they are inquiring about
                        time = input('Enter a time in HH:MM AM/PM format to check package status: ')
                        format1 = re.match("[0-9][0-9]:[0-9][0-9] [A-Z][A-Z]", time)

                        if bool(format1):
                            time = reverse_min(time)
                            print('')
                            print(lookup(inquiry, time))
                            print('')
                            break
                        else:
                            print('')
                            print("Please enter a correct time.")
                            print('')
                else:
                    print('')
                    print('Type a Package ID between 1 - 40 (typing 0 Exits the program)')
                    print('')

        elif menu_option == "3":
            # 550 represents 09:16 AM, 610 represents 10:16 AM, 750 represents 12:30 PM (in minutes).
            # Print statements are then created for all packages to display the delivery status at the entered time.
            time1 = 550
            time2 = 610
            time3 = 750

            print('')
            print('--All Packages at ' + min_to_hour(time1) + ": \n")
            print('')

            for i in range(1, 41):
                print('')
                print(lookup(package_hash.lookup(i), time1))
                print('')
            print('')
            print('--All Packages at ' + min_to_hour(time2) + ': \n')
            print('')

            for i in range(1, 41):
                print('')
                print(lookup(package_hash.lookup(i), time2))
                print('')
            print('')
            print('--All Packages at ' + min_to_hour(time3) + ': \n')
            print('')

            for i in range(1, 41):
                print('')
                print(lookup(package_hash.lookup(i), time3))
                print('')

        elif menu_option == '4':

            # Selecting option 4 terminates the program
            print('')
            print('Exiting.')
            break

        else:
            # If anything else is typed into the program besides the numbers 1, 2, 3 or 4, a message displays for
            # the user to select a valid menu option.
            print('')
            print('Please select a valid option.')




