import timeit
import sympy

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().splitlines()
        data = [line.split('@') for line in data]
        data = [[list(map(int, line[0].split(','))), list(map(int, line[1].split(',')))] for line in data]
        return data

    def run(self):
        data = self.read_data()
        hails = []

        xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")

        for line  in data:
            px, py, pz = line[0]
            vx, vy, vz = line[1]

            hails.append([px, py, pz, vx, vy, vz])


        equations = []

        for sx, sy, sz, vx, vy, vz in hails:
            equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
            equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))


        answers = sympy.solve(equations)
        ans = answers[0]
        print(answers)
        return ans[xr] + ans[yr] + ans[zr]

    
        
            


def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()