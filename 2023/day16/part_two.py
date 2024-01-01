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
    

    def energize(self, coords, size, start, direction):
        x, y = start
        queue = deque([(x, y, direction)])
        visited = set()
        ROWS, COLS = size

        while queue:
            cur = queue.popleft()
            x, y, direction = cur
            point = coords[(x, y)]

            if (x, y, direction) in visited:
                continue

            visited.add((x, y, direction))
            for new_direction in self.mirrors[point][direction]:
                dx, dy = self.directions[new_direction]
                if x + dx in range(COLS) and y + dy in range(ROWS):
                    queue.append((x + dx, y + dy, new_direction))

        visited_coords = set()
        for x, y, _ in visited:
            visited_coords.add((x, y))

        return len(visited_coords)

    def run(self):
        data = self.read_data()
        coords, size = self.convert_to_coords(data)

        ROWS, COLS = size
        top_row = [(x, 0) for x in range(COLS)]
        bottom_row = [(x, ROWS - 1) for x in range(COLS)]
        left_col = [(0, y) for y in range(ROWS)]
        right_col = [(COLS - 1, y) for y in range(ROWS)]

        max_energized = 0

        for start in top_row:
            max_energized = max(max_energized, self.energize(coords, size, start, "S"))
        for start in bottom_row:
            max_energized = max(max_energized, self.energize(coords, size, start, "N"))
        for start in left_col:
            max_energized = max(max_energized, self.energize(coords, size, start, "E"))
        for start in right_col:
            max_energized = max(max_energized, self.energize(coords, size, start, "W"))

        return max_energized
        
        
def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()