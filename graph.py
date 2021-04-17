class Vertex:
    """
    creates Vertex class
    """
    def __init__(self, id, name, address, city, state, zipcode):
        """
        Constructor for the Vertex class. Takes in attributes for the Vertex as arguments
        :param id: Vertex id
        """
        self.id = id
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode


class Graph:
    """
    creates Graph class
    """
    vertex_list = []
    edge_list = []

    def add_v(self, vertex):
        """
        method to add vertex to graph instance
        :param vertex: vertex being added
        """
        self.vertex_list.append(vertex)
        for edge in self.edge_list:
            edge.append(0)
        self.edge_list.append([0] * len(self.edge_list) + 1)


    def add_e(self, id1, id2, weight):
        """
        method to set weight between to vertices
        :param id1: first vertex
        :param j: second vertex
        :param weight: weight being added
        """
        self.edge_list[id1 - 1][id2 - 1] = weight
        self.edge_list[id2 - 1][id1 - 1] = weight


    def dist(self, current, next):
        """
        method to retrieve distance between to vertices
        :param current: current vertex
        :param next: next index
        :return: edge weight
        """
        return float(self.edge_list[current - 1][next - 1])






