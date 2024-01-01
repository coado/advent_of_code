import timeit
from collections import deque

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().split("\n")
        # return [i.split("") for i in data]
        return [list(i) for i in data]
    
    def parse_data(self, data):
        ROWS, COLS = len(data), len(data[0])
        points = {}
        start = (0, 0)

        for y in range(ROWS):
            for x in range(COLS):
                points[(x, y)] = data[y][x]

                if data[y][x] == "S":
                    start = (x, y)
        
        return points, (ROWS, COLS), start
    


    def run(self):
        data = self.read_data()
        points, sizes, start = self.parse_data(data)
        ROWS, COLS = sizes

        def traverse(sx, sy, s):
            res = set()
            visited = {(sx, sy)}
            
            queue = deque([(sx, sy, s)])

            while queue:
                x, y, steps  = queue.popleft()

                if steps % 2 == 0:
                    res.add((x, y))
                
                if steps == 0:
                    continue
                

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if nx < 0 or nx >= COLS or ny < 0 or ny >= ROWS or points[(nx, ny)] == "#" or (nx, ny) in visited:
                        continue
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps - 1))

            return len(res)
    
        assert ROWS == COLS
        size = ROWS
        steps = 26501365
        grid_length = steps // size - 1

        odds = (grid_length // 2 * 2 + 1) ** 2
        evens = ((grid_length + 1) // 2 * 2) ** 2

        odd_steps = traverse(start[0], start[1], size * 2 + 1)
        even_steps = traverse(start[0], start[1], size * 2)

        top_corner_steps = traverse(size // 2, size - 1, size - 1)
        right_corner_steps = traverse(0, size // 2, size - 1)
        bottom_corner_steps = traverse(size // 2, 0, size - 1)
        left_corner_steps = traverse(size - 1, size // 2, size - 1)

        sm_tr = traverse(0, size - 1, size // 2 - 1)
        sm_tl = traverse(size - 1, size - 1, size // 2 - 1)
        sm_br = traverse(0, 0, size // 2 - 1)
        sm_bl = traverse(size - 1, 0, size // 2 - 1)


        lg_tr = traverse(0, size - 1, size * 3 // 2 - 1)
        lg_tl = traverse(size - 1, size - 1, size * 3 // 2 - 1)
        lg_br = traverse(0, 0, size * 3 // 2 - 1)
        lg_bl = traverse(size - 1, 0, size * 3 // 2 - 1)


        res = sum([
            odds * odd_steps,
            evens * even_steps,
            top_corner_steps,
            right_corner_steps,
            bottom_corner_steps,
            left_corner_steps,
            (grid_length + 1) * (sm_tr + sm_tl + sm_bl + sm_br),
            grid_length * (lg_tr + lg_bl + lg_br + lg_tl)

        ])

        print(res)
        # return traverse(start[0], start[1], 64)

def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()