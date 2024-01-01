import timeit
import heapq

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        
        data = data.split('\n')
        return data
    
    def get_points_map(self, data):
        points = {}
        ROWS, COLS = len(data), len(data[0])
        
        for y in range(ROWS):
            for x in range(COLS):
                points[(x, y)] = data[y][x]

        size = (ROWS, COLS)
        return points, size
    

    def move_rocks(self, points, size):
        ROWS, COLS = size

        for x in range(COLS):
            minY = []
            for y in range(ROWS):
                cur = points[(x, y)]
                if cur == ".":
                    heapq.heappush(minY, y)
                elif cur == "#":
                    minY = []
                else:
                    # Rock
                    if len(minY) == 0:
                        # We can't move rock any more
                        continue
                    
                    # Get new rock position
                    move_y = heapq.heappop(minY)
                    # Put current rock position to the stack
                    heapq.heappush(minY, y)
                    points[(x, y)] = "."
                    # Move rock to the farthest empty space
                    points[(x, move_y)] = "O"
                     
    def calculate_load(self, points, size):
        ROWS, COLS = size
        load = 0
        for y in range(ROWS):
            for x in range(COLS):
                if points[(x, y)] == "O":
                    load += ROWS - y
        return load   

    def run(self):
        data = self.read_data()
        points, size = self.get_points_map(data)
        self.move_rocks(points, size)
        load = self.calculate_load(points, size)

        return load


def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")


main()