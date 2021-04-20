class Vertex:
    """
    Creates Vertex class
    """
    def __init__(self, id, address, city, state, zipcode):
        """
        Constructor for the Vertex class. Takes in attributes for the Vertex as arguments
        """
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode


class Graph:
    """
    Creates Graph class and instantiates an empty vertex list and an empty edge list
    """
    vertex_list = []
    edge_list = []

    def add_v(self, vertex):
        """
        Big O(N)
        Method to add vertex to graph instance.
        Appends input vertex element to a 2D matrix. Then appends edge weights to zero to fill in the graph.
        :param vertex: vertex being added
        """
        self.vertex_list.append(vertex)
        for edge in self.edge_list:
            edge.append(0)
        self.edge_list.append([0] * (len(self.edge_list) + 1))


    def add_e(self, id1, id2, weight):
        """
        Big O(N)
        Method takes in two vertices and adds in the correct edge weight between the vertices.
        :param id1: first vertex
        :param j: second vertex
        :param weight: weight being added
        """
        self.edge_list[id1 - 1][id2 - 1] = weight
        self.edge_list[id2 - 1][id1 - 1] = weight


    def dist(self, current, next):
        """
        Big O(N)
        Method to retrieve distance between two vertices
        :param current: current vertex
        :param next: next index
        :return: edge weight
        """
        return float(self.edge_list[current - 1][next - 1])






