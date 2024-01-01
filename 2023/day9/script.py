import timeit

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data
    
    def predict_dfs(self, sequence):
        lower_level = []

        all_zeros = True
        for i in range(1, len(sequence)):
            val = sequence[i] - sequence[i-1]
            lower_level.append(val)
            if val != 0:
                all_zeros = False

        if all_zeros:
            return sequence[-1]

        lower_level_prediction = self.predict_dfs(lower_level)
        return lower_level_prediction + sequence[-1]
    
    def predict_dfs_inv(self, sequence):
        lower_level = []

        all_zeros = True
        for i in range(1, len(sequence)):
            val = sequence[i] - sequence[i-1]
            lower_level.append(val)
            if val != 0:
                all_zeros = False
        if all_zeros:
            return sequence[0]

        lower_level_prediction = self.predict_dfs_inv(lower_level)
        return sequence[0] - lower_level_prediction

    def part_one(self):
        data = [list(map(int, i.split(" "))) for i in self.read_data().split("\n")]

        res = 0
        for sequence in data:
            res += self.predict_dfs(sequence)

        return res

    def part_two(self):
        data = [list(map(int, i.split(" "))) for i in self.read_data().split("\n")]

        res = 0
        for sequence in data:
            res += self.predict_dfs_inv(sequence)

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