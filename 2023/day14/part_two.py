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
    

    def move_north(self, points, size):
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
                    if len(minY) == 0:
                        continue                    
                    move_y = heapq.heappop(minY)
                    heapq.heappush(minY, y)
                    points[(x, y)] = "."
                    points[(x, move_y)] = "O"

    def move_west(self, points, size):
        ROWS, COLS = size
        for y in range(ROWS):
            minX = []
            for x in range(COLS):
                cur = points[(x, y)]
                if cur == ".":
                    heapq.heappush(minX, x)
                elif cur == "#":
                    minX = []
                else:
                    if len(minX) == 0:
                        continue                    
                    move_x = heapq.heappop(minX)
                    heapq.heappush(minX, x)
                    points[(x, y)] = "."
                    points[(move_x, y)] = "O"

    def move_south(self, points, size):
        ROWS, COLS = size
        for x in range(COLS):
            maxY = []
            for y in range(ROWS - 1, -1, -1):
                cur = points[(x, y)]
                if cur == ".":
                    heapq.heappush(maxY, -y)
                elif cur == "#":
                    maxY = []
                else:
                    if len(maxY) == 0:
                        continue                    
                    move_y = -heapq.heappop(maxY)
                    heapq.heappush(maxY, -y)
                    points[(x, y)] = "."
                    points[(x, move_y)] = "O"

    def move_east(self, points, size):
        ROWS, COLS = size
        for y in range(ROWS):
            maxX = []
            for x in range(COLS - 1, -1, -1):
                cur = points[(x, y)]
                if cur == ".":
                    heapq.heappush(maxX, -x)
                elif cur == "#":
                    maxX = []
                else:
                    if len(maxX) == 0:
                        continue                    
                    move_x = -heapq.heappop(maxX)
                    heapq.heappush(maxX, -x)
                    points[(x, y)] = "."
                    points[(move_x, y)] = "O"

      
    def calculate_load(self, points, size):
        ROWS, COLS = size
        load = 0
        for y in range(ROWS):
            for x in range(COLS):
                if points[(x, y)] == "O":
                    load += ROWS - y
        return load 

    def cycle(self, points, size):
        self.move_north(points, size)
        self.move_west(points, size)
        self.move_south(points, size)
        self.move_east(points, size)  


    def print_grid(self, points, size):
        grid = ''
        ROWS, COLS = size
        for y in range(ROWS):
            for x in range(COLS):
                grid += points[(x, y)]
            grid += '\n'
        print(grid)

    def floyd(self, points, size):
        slow = points.copy()
        fast = slow.copy()
        met = False
        before_met = 0
        while True:
            before_met += 1
            self.cycle(slow, size)
            self.cycle(fast, size)
            self.cycle(fast, size)
            if slow == fast:
                met = True
                break

        if not met:
            return -1

        slow = points.copy()

        loop_length = 0
        while slow != fast:
            self.cycle(slow, size)
            loop_length += 1

        offset = 0
        slow = points.copy()
        while slow != fast:
            self.cycle(slow, size)
            self.cycle(fast, size)
            offset += 1

  
        return loop_length, offset

    def run(self):
        data = self.read_data()
        points, size = self.get_points_map(data)

        loop_length, offset = self.floyd(points, size) 
        print(f"Loop Length: {loop_length}")
        print(f"Offset: {offset}")
        
        number_of_cycles = (1000000000 - offset) % loop_length + offset

        for _ in range(number_of_cycles):
            self.cycle(points, size)

        load = self.calculate_load(points, size)
        return load


def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()