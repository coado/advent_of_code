import timeit
from typing import List, Dict, Tuple

class Solution:

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        
        data = [i.split('\n') for i in data.split("\n\n")]
        return data
    
    def get_points_map(self, data):
        mirrors = []
        sizes = []

        for mirror in data:
            points = {}
            ROWS, COLS = len(mirror), len(mirror[0])
            for y in range(ROWS):
                for x in range(COLS):
                    points[(x, y)] = mirror[y][x]
            mirrors.append(points)
            sizes.append((ROWS, COLS))

        return mirrors, sizes
    
    
    
    def get_split_line_horizontal(self, points, size):
        ROWS, COLS = size

        def check_reflection(dy):
            smudges = 0
            for y1, y2 in dy:
                for x in range(COLS):
                    if points[(x, y1)] != points[(x, y2)]:
                        smudges += 1
                        if smudges > 1:
                            return False
            return smudges == 1

        for y in range(1, ROWS):
            dy = [(y - i - 1, y + i) for i in range(min(y, ROWS - y))]
            is_reflection = check_reflection(dy)
            if is_reflection:
                return y
            
        return 0
    
    def get_split_line_vertical(self, points, size):
        ROWS, COLS = size

        def check_reflection(dx):
            smudges = 0
            for x1, x2 in dx:
                for y in range(ROWS):
                    if points[(x1, y)] != points[(x2, y)]:
                        smudges += 1
                        if smudges > 1:
                            return False
            return smudges == 1

        for x in range(1, COLS):
            dx = [(x - i - 1, x + i) for i in range(min(x, COLS - x))]
            is_reflection = check_reflection(dx)
            if is_reflection:
                return x
            
        return 0


    def run(self):
        data = self.read_data()
        mirrors, sizes = self.get_points_map(data)
        
        res = 0
        for i in range(len(mirrors)):
            points = mirrors[i]
            horizontal_line = self.get_split_line_horizontal(points, sizes[i])
            vertical_line = self.get_split_line_vertical(points, sizes[i])
            
            res += vertical_line if vertical_line != 0 else horizontal_line * 100

        return res            

def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")


main()