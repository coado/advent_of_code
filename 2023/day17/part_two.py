import heapq

class Block:
    def __init__(self, x, y, heat_loss, direction, steps, prev=None):
        self.x = x
        self.y = y
        self.heat_loss = heat_loss
        self.direction = direction
        self.steps = steps
        self.prev = prev

    def __lt__(self, other):
        return self.heat_loss < other.heat_loss


class Solution:

    def __init__(self):
        self.directions = {
            "N": (0, -1),
            "S": (0, 1),
            "E": (1, 0),
            "W": (-1, 0)
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
                coords[(x, y)] = int(data[y][x])

        return coords, (ROWS, COLS) 
    
    def is_opposite(self, direction, new_direction):
        if direction == "N" and new_direction == "S":
            return True
        elif direction == "E" and new_direction == "W":
            return True
        elif direction == "S" and new_direction == "N":
            return True
        elif direction == "W" and new_direction == "E":
            return True
        else:
            return False
    
    
    def run(self):
        data = self.read_data()
        coords, size = self.convert_to_coords(data)
        ROWS, COLS = size
        end_x, end_y = COLS - 1, ROWS - 1

        # heat_loss, x, y, heat_loss, h, direction, steps
        heap = [Block(0, 0, 0, None, 0)]
        visited = set()
        visited.add((0, 0, None, 0))

        max_steps = 10
        last = None


        while heap:
            block = heapq.heappop(heap)
 
            if block.x == end_x and block.y == end_y and block.steps >= 4:
                last = block
                print(f"Found path with heat loss: {block.heat_loss}")
                break

            for new_direction, d in self.directions.items():
                if (block.steps < 4 and new_direction != block.direction) and block.direction != None:
                    continue

                new_steps = 1
                if new_direction == block.direction:
                    new_steps += block.steps

                dx, dy = d
                new_x, new_y = block.x + dx, block.y + dy
                
                if (new_steps > max_steps or
                    self.is_opposite(block.direction, new_direction) or 
                    new_x not in range(COLS) or
                    new_y not in range(ROWS)
                ):
                    continue

                new_heat_loss = coords[(new_x, new_y)] + block.heat_loss
                if (new_x, new_y, new_direction, new_steps) in visited:
                    continue
                
                # h = new_heat_loss + abs(new_x - end_x) + abs(new_y - end_y)
                visited.add((new_x, new_y, new_direction, new_steps))
                heapq.heappush(heap, Block(new_x, new_y, new_heat_loss, new_direction, new_steps, block))



        # mark path
        while last.prev:
            x, y, dir = last.x, last.y, last.direction
            arrow = ""
            if dir == "N":
                arrow = "^"
            elif dir == "E":
                arrow = ">"
            elif dir == "S":
                arrow = "v"
            elif dir == "W":
                arrow = "<"
            coords[(x, y)] = arrow

            last = last.prev

        # print grid
        grid = ''

        for y in range(ROWS):
            for x in range(COLS):
                grid += str(coords[(x, y)])
            grid += "\n"

        print(grid)



def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()