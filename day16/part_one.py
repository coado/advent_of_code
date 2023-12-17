import timeit
from collections import deque

class Solution:

    def __init__(self):
        self.directions = {
            "N": (0, -1),
            "E": (1, 0),
            "S": (0, 1),
            "W": (-1, 0)
        }
        self.mirrors = {
            ".": {
                "N": ["N"],
                "E": ["E"],
                "S": ["S"],
                "W": ["W"]
            },
            "/": {
                "N": ["E"],
                "E": ["N"],
                "S": ["W"],
                "W": ["S"]
            },
            "\\": {
                "N": ["W"],
                "E": ["S"],
                "S": ["E"],
                "W": ["N"]
            },
            "-":{
                "N": ["W", "E"],
                "S": ["W", "E"],
                "W": ["W"],
                "E": ["E"]
            },
            "|":{
                "N": ["N"],
                "S": ["S"],
                "W": ["N", "S"],
                "E": ["N", "S"]
            },
        }

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip()
        
        return data
    
    def convert_to_coords(self, data):
        data = data.split("\n")
        ROWS, COLS = len(data), len(data[0])
        coords = {}

        for y in range(ROWS):
            for x in range(COLS):
                coords[(x, y)] = data[y][x]

        return coords, (ROWS, COLS)
                

    def run(self):
        data = self.read_data()
        coords, size = self.convert_to_coords(data)

        ROWS, COLS = size
        energized = coords.copy()
        for x in range(COLS):
            for y in range(ROWS):
                energized[(x, y)] = "."

        queue = deque([(0, 0, "E")])
        visited = set()

        while queue:
            cur = queue.popleft()
            x, y, direction = cur
            point = coords[(x, y)]

            if (x, y, direction) in visited:
                continue

            visited.add((x, y, direction))
            energized[(x, y)] = "#"

            for new_direction in self.mirrors[point][direction]:
                dx, dy = self.directions[new_direction]
                if x + dx in range(COLS) and y + dy in range(ROWS):
                    queue.append((x + dx, y + dy, new_direction))


        grid = ''
        for y in range(ROWS):
            for x in range(COLS):
                grid += energized[(x, y)]
            grid += "\n"

        print(grid)

        visited_coords = set()
        for x, y, _ in visited:
            visited_coords.add((x, y))

        return len(visited_coords)




def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()