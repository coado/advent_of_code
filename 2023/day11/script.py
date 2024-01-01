import timeit
import numpy as np
import math

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def expand_universe(self, universe):
        ROWS, COLS = len(universe), len(universe[0])

        row_galaxies = [0] * ROWS
        col_galaxies = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if universe[r][c] == "#":
                    row_galaxies[r] += 1
                    col_galaxies[c] += 1

        expanded = 0
        for row, galaxies in enumerate(row_galaxies):
            if galaxies == 0:
                new_row = ["."] * COLS
                universe = np.insert(universe, row + expanded, new_row, axis=0)
                expanded += 1

        expanded = 0
        for col, galaxies in enumerate(col_galaxies):
            if galaxies == 0:
                new_col = ["."] * len(universe)
                universe = np.insert(universe, col + expanded, new_col, axis=1)
                expanded += 1

        return universe


    def expand_large_universe(self, universe):
        ROWS, COLS = len(universe), len(universe[0])

        row_galaxies = [0] * ROWS
        col_galaxies = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if universe[r][c] == "#":
                    row_galaxies[r] += 1
                    col_galaxies[c] += 1

        large_universe = np.ones((ROWS, COLS), dtype=int)
        # if there is no galaxy in a row, then write 1000000 in that row
        for row, galaxies in enumerate(row_galaxies):
            if galaxies == 0:
                large_universe[row] = 1000000

        # if there is no galaxy in a column, then write 1000000 in that column
        for col, galaxies in enumerate(col_galaxies):
            if galaxies == 0:
                large_universe[:, col] = 1000000

        return large_universe
    
    def part_one(self):
        universe = np.array([list(i) for i in self.read_data().split("\n")])
        universe = self.expand_universe(universe)
        coords = []

        ROWS, COLS = len(universe), len(universe[0])

        for r in range(ROWS):
            for c in range(COLS):
                if universe[r][c] == "#":
                    coords.append((r, c))

        res = 0

        # calculate distances between all pairs of coordinates
        for i in range(len(coords)):
            cur_row, cur_col = coords[i]
            for j in range(i + 1, len(coords)):
                next_row, next_col = coords[j]
                dist = abs(cur_row - next_row) + abs(cur_col - next_col)
                res += dist
        
        return res

    def part_two(self):
        universe = np.array([list(i) for i in self.read_data().split("\n")])
        large_universe = self.expand_large_universe(universe)

        coords = []

        ROWS, COLS = len(universe), len(universe[0])

        for r in range(ROWS):
            for c in range(COLS):
                if universe[r][c] == "#":
                    coords.append((r, c))

        res = 0

        # calculate distances between all pairs of coordinates
        for i in range(len(coords)):
            cur_row, cur_col = coords[i]
            for j in range(i + 1, len(coords)):
                next_row, next_col = coords[j]

                start_row = min(cur_row, next_row)
                end_row = max(cur_row, next_row)

                start_col = min(cur_col, next_col)
                end_col = max(cur_col, next_col)

                window_horizontal = large_universe[start_row, start_col+1:end_col + 1]
                window_vertical = large_universe[start_row+1:end_row + 1, start_col]

                dist = sum(window_horizontal) + sum(window_vertical)
                # print(f"{i + 1} {j + 1} {window_horizontal}")
                res += dist
        
        return res
                        
                
def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}")
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(f"Part two: {sol.part_two()}")
    time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_two:.3f} ms")

main()