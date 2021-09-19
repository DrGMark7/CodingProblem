class Graph(object):
    def __init__(self, edge_list):
        self.edge_list = edge_list

    def add_edge(self, edge_list):
        self.edge_list.append(edge_list)

    def adj_mtx_diect(self):
        v = 0
        counter = set()
        for src, dest in self.edge_list:
            counter.add(src)
            counter.add(dest)

        v = len(counter)

        mtx = [[0 for y in range(v)]for x in range(v)]
        for e in self.edge_list:
            src, dest = e
            src = src - 1
            dest = dest - 1
            if src == dest:
                mtx[src][dest] = 2
            else:
                mtx[src][dest] = 1

        return mtx
    
    def adj_mtx_undiect(self):
        v = 0
        counter = set()
        for src, dest in self.edge_list:
            counter.add(src)
            counter.add(dest)

        v = len(counter)

        mtx = [[0 for y in range(v)]for x in range(v)]
        for e in self.edge_list:
            src, dest = e
            src = src - 1
            dest = dest - 1
            if src == dest:
                mtx[src][dest] = 2
                mtx[dest][src] = 2
            else:
                mtx[src][dest] = 1
                mtx[dest][src] = 1

        return mtx