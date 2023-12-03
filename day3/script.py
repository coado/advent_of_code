import numpy as np

class Solution:
    def parse_data(self):
        data = []
        with open('data.txt', 'r') as f:
            for line in f:
                tokens = list(line.strip())
                data.append(tokens)
        return np.array(data)

    def is_symbol(self, el):
        return el != '.' and not el.isdigit()
    
    def contains_symbol(self, arr):
        for el in arr:
            if self.is_symbol(el):
                return True
        return False
    
    def prepare_data(self, data):
        parsed = np.zeros(data.shape, np.uint32)
        ROWS, COLS = data.shape

        for r in range(ROWS):
            cur = 0
            for c in range(COLS):
                if data[r, c].isdigit():
                    cur = (cur*10) + int(data[r, c])
                    continue
                
                if cur != 0:
                    n = len(str(cur))
                    for i in range(c - n, c):
                        parsed[r, i] = cur
                    cur = 0

            if cur != 0:

                n = len(str(cur))
                for i in range(COLS - n, COLS):
                    parsed[r, i] = cur
                cur = 0
        return parsed


    def part_one(self):
        data = self.parse_data()
        ROWS, COLS = data.shape
        total = 0
        for r in range(ROWS):
            cur = 0
            is_adjacent = False
            cur_index = 1
            if r == 0:
                cur_index = 0

            for c in range(COLS):
                window = data[max(0, r-1):min(r+2, ROWS), c]                
                
                if window[cur_index].isdigit():
                    cur = (cur*10) + int(window[cur_index])
                    is_adjacent = is_adjacent or self.contains_symbol(window)
                    continue

                if cur != 0:
                    is_adjacent = is_adjacent or self.contains_symbol(window)
                    if is_adjacent:
                        total += cur
                    cur = 0

                is_adjacent = self.contains_symbol(window)

            if is_adjacent:
                total += cur
                    
        return total
                

    def part_two(self):
        data = self.parse_data()
        parsed = self.prepare_data(data)
        ROWS, COLS = data.shape
        total = 0

        for r in range(ROWS):                
            for c in range(COLS):
                el = data[r, c]
                if el != '*':
                    continue
                
                window = parsed[max(0, r-1):min(r+2, ROWS), max(0, c-1):min(c+2, COLS)]
                print(window)
                adjacent_numbers = []
                for row in window:
                    unique_numbers_in_row = [i for i in np.unique(row) if i != 0]
                    adjacent_numbers += unique_numbers_in_row

                if len(adjacent_numbers) != 2:
                    continue
                
                total += (adjacent_numbers[0] * adjacent_numbers[1])

        return total

    


def main():
    solution = Solution()
    # print(solution.part_one())
    print(solution.part_two())


main()
                