import timeit


class Solution:

    def __init__(self):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().splitlines()
        return data
    
    def find_largest_path(self, start, end, graph):
        visited = set()
        res = float('-inf')
        
        def dfs(cur, n):
            if cur == end:
                nonlocal res
                res = max(res, n)
                return
            
            visited.add(cur)
            for nxt, distance in graph[cur].items():
                if nxt in visited:
                    continue
                dfs(nxt, n + distance)
            visited.remove(cur)


        dfs(start, 0)

        return res


    def run(self):
        data = self.read_data()
        start = (0, data[0].index('.'))
        end = (len(data) - 1, data[-1].index('.'))
        
        points = [start, end]
        for r, row in enumerate(data):
            for c, ch in enumerate(row):
                if ch == "#":
                    continue
                
                neigh = 0
                for y, x in ([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]):
                    if y in range(len(data)) and x in range(len(data[0])) and data[y][x] != "#":
                        neigh += 1
                
                if neigh >= 3:
                    points.append((r, c))


        adj = {p: {} for p in points}

        for sr, sc in points:
            stack = [(sr, sc, 0)]
            visited = {(sr, sc)}

            while stack:
                r, c, n = stack.pop()

                if n != 0 and (r, c) in adj:
                    adj[(sr, sc)][(r, c)] = n
                    continue

                for dr, dc in self.directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(len(data)) and nc in range(len(data[0])) and (nr, nc) not in visited and data[nr][nc] != "#":
                        stack.append((nr, nc, n + 1))
                        visited.add((nr, nc))
        
        return self.find_largest_path(start, end, adj)
       



def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()