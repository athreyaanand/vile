class DiGraph(object):

    def __init__(self, graph_dict={}):
        #initializes graph object with default None dictionary
        self.__graph_dict = graph_dict
    
    def nodes(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__create_edges()

    def add_node(self, edge):
        #edge should be set, tuple, or list
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vetex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]
    
#    def __generate_edges











directed_graph = {'Parent1':['Child1', 'Child2'],
                  'Parent2':['Child1', 'Child2', 'Child6'],
                  'Parent3':['Child3', 'Child4', 'Child5'],
                  'Parent4':['Child3', 'Child4', 'Child5'],
                  'Parent5':['Child6'],
                  'Child1':[],
                  'Child2':[],
                  'Child3':[],
                  'Child4':[],
                  'Child5':[],
                  'Child6':[]}

def print_graph(graph, start, end, path = []):
    path =  path + [start]
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = print_graph(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

print(print_graph(directed_graph, 'Parent1', 'Child6'))
