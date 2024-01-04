import timeit
import networkx as nx

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().splitlines()
        data = [connection.split(":") for connection in data]
        return data
    
    def run(self):
        data = self.read_data()
        g = nx.Graph()
        
        for left, right in data:
            for node in right.strip().split():
                g.add_edge(left, node)
        
        edges_to_remove = nx.minimum_edge_cut(g)
        g.remove_edges_from(edges_to_remove)
        a, b = nx.connected_components(g)
        return len(a) * len(b)

def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()