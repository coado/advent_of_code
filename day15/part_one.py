import timeit

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        
        return data
    
    def run(self):
        data = self.read_data().strip().split(',')
        
        res = 0
        for text in data:
            cur_value = 0
            for char in text:
                cur_value += ord(char)
                cur_value *= 17
                cur_value %= 256
            res += cur_value
        return res




def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()