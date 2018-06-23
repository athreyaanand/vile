class DirectedGraph(object):

    #initializes graph object with default empty dictionary
    #takes in dictionary
    def __init__(self, graph_dict={}):
        self.__graph_dict = graph_dict
    
    #returns a list of nodes
    def nodes(self):
        return list(self.__graph_dict.keys())
    
    #returns list of edges
    def edges(self):
        return self.__generate_edges()

    def add_node(self, edge):
        #edge should be set, tuple, or list
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
    def __generate_edges(self):
        edges = []
        for vertex in self.__graph_dict:
            for neighbor in self.__graph_dict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


