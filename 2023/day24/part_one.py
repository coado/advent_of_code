import timeit


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

        area = (200000000000000, 400000000000000)

        for line  in data:
            px, py, pz = line[0]
            vx, vy, vz = line[1]

            x1, y1 = px, py
            x2, y2 = px + vx, py + vy
            
            a = (y2 - y1) / (x2 - x1 or 0.0000001)
            b = y1 - a*x1

            hails.append([px, py, pz, vx, vy, vz, a, b])

        total = 0
        for i in range(len(hails)):
            for j in range(i, len(hails)):
                hail1, hail2 = hails[i], hails[j]

                px1, py1, _, vx1, vy1, _, a1, b1 = hail1
                px2, py2, _, vx2, vy2, _, a2, b2 = hail2

                if a1 == a2:
                    continue

                x = (b2 - b1) / (a1 - a2)
                y = a1*x + b1

                if (vx1 < 0 and x > px1) or (vx1 > 0 and x < px1):
                    continue
                if (vy1 < 0 and y > py1) or (vy1 > 0 and y < py1):
                    continue
                if (vx2 < 0 and x > px2) or (vx2 > 0 and x < px2):
                    continue
                if (vy2 < 0 and y > py2) or (vy2 > 0 and y < py2):
                    continue

                if x >= area[0] and x <= area[1] and y >= area[0] and y <= area[1]:
                    total += 1
        
        return total



        
            


def main():
    sol = Solution()
    print(f"Part One: {sol.run()}")
    elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    print(f"Elapsed Time: {elapsed:.3f} ms")

main()