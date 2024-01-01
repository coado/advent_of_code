import timeit
import math
import numpy as np

class Solution:

    def __init__(self):
        self.pipes = {
            "|": [[1, 0], [-1, 0]],
            "-": [[0 , 1], [0, -1]],
            "L": [[-1, 0], [0, 1]],
            "J": [[0, -1], [-1, 0]],
            "7": [[1, 0], [0, -1]],
            "F": [[0, 1], [1, 0]],
            ".": [[0, 0]],
            "S": [[0, 0]]
        }

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def find_start_coords(self, data):
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "S":
                    return (i, j)
        return -1, -1
    

    def part_one(self):
        data = np.array([list(i) for i in self.read_data().split("\n")])
        start_row, start_col = self.find_start_coords(data)

        def traverse(row, col, prev_row, prev_col):

            cur_pipe = data[row][col]
            dist = 1

            while cur_pipe != "S":
                if data[row][col] == ".":
                    return -1
                
                # copy the destinations
                destinations = self.pipes[cur_pipe][:]
                # one destination should point to the previous pipe
                if [prev_row - row, prev_col - col] in destinations:
                    destinations.remove([prev_row - row, prev_col - col])
                else:
                    # if the previous pipe is not in the destinations, then there is no connection between the pipes
                    return -1
                
                dest = destinations[0]
                prev_row = row
                prev_col = col
                row = row + dest[0]
                col = col + dest[1]
                cur_pipe = data[row][col]
                dist += 1

            
            return dist
        
        trav_1 = traverse(start_row, start_col + 1, start_row, start_col)
        trav_2 = traverse(start_row, start_col - 1, start_row, start_col)
        trav_3 = traverse(start_row + 1, start_col, start_row, start_col)
        trav_4 = traverse(start_row - 1, start_col, start_row, start_col)

        return math.ceil(max(trav_1, trav_2, trav_3, trav_4) / 2)
                


    def part_two(self):
        data = np.array([list(i) for i in self.read_data().split("\n")])
        start_row, start_col = self.find_start_coords(data)

        def traverse(row, col, prev_row, prev_col):
            pipe_coords = []
            cur_pipe = data[row][col]

            while cur_pipe != "S":
                if data[row][col] == ".":
                    return None
                
                # copy the destinations
                destinations = self.pipes[cur_pipe][:]
                # one destination should point to the previous pipe
                if [prev_row - row, prev_col - col] in destinations:
                    destinations.remove([prev_row - row, prev_col - col])
                else:
                    # if the previous pipe is not in the destinations, then there is no connection between the pipes
                    return None

                pipe_coords.append((row, col))
                dest = destinations[0]
                prev_row = row
                prev_col = col
                row = row + dest[0]
                col = col + dest[1]
                cur_pipe = data[row][col]

            
            return pipe_coords
        
        pipe_coords_1 = traverse(start_row, start_col + 1, start_row, start_col)
        pipe_coords_2 = traverse(start_row, start_col - 1, start_row, start_col)
        pipe_coords_3 = traverse(start_row + 1, start_col, start_row, start_col)
        pipe_coords_4 = traverse(start_row - 1, start_col, start_row, start_col)

        pipe_coords = pipe_coords_1 or pipe_coords_2 or pipe_coords_3 or pipe_coords_4
        pipe_coords.append((start_row, start_col))
        pipe_coords = set(pipe_coords)

        closed_area = 0
        ROWS, COLS = len(data), len(data[0]) 

        closed_area_coords = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pipe_coords:
                    continue

                horizontal_crosses = 0
                for col in range(c + 1, COLS):
                    if (r, col) in pipe_coords and data[r][col] in ["|", "L", "J"]:
                        horizontal_crosses += 1

                if horizontal_crosses % 2 == 1:
                    closed_area_coords.append((r, c))
                    closed_area += 1


        # # Draw pipes as #
        # content = ""
        # for r in range(ROWS):
        #     row = ''
        #     for c in range(COLS):
        #         if (r, c) in closed_area_coords:
        #             row += "I"
        #         elif data[r][c] == ".":
        #             row += "O"
        #         else:
        #             row += "#"
        #     content += row + "\n"

        # print(content)

        return closed_area

def main():
    sol = Solution()
    print(f"Part one: {sol.part_one()}") 
    time_part_one = (timeit.timeit(sol.part_one, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_one:.3f} ms")
    print(f"Part two: {sol.part_two()}")
    time_part_two = (timeit.timeit(sol.part_two, number=10) / 10) * 1000
    print(f"Elapsed Time: {time_part_two:.3f} ms")

main()