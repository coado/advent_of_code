import timeit
from collections import deque

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read().strip().splitlines()
        data = [list(map(int, line.replace('~', ',').split(','))) for line in data]
        return data

    def run(self):
        bricks = self.read_data()
        # sort by z
        bricks.sort(key=lambda brick: brick[2])

        for i, brick in enumerate(bricks):
            max_z = 1
            xs, ys, _, xe, ye, _ = brick

            for rest in bricks[:i]:
                rxs, rys, _, rxe, rye, rze = rest
                if max(xs, rxs) <= min(xe, rxe) and max(ys, rys) <= min(ye, rye):
                    max_z = max(max_z, rze + 1) 

                # if (xe < rxs or xs > rxe) or (ye < rys or ys > rye):
                #     continue
                    
                # max_z = max(max_z, rze + 1) 

            brick[5] -= brick[2] - max_z
            brick[2] = max_z

        bricks.sort(key=lambda brick: brick[2])    

        k_to_v = {i: set() for i in range(len(bricks))} 
        v_to_k = {i: set() for i in range(len(bricks))}  


        for j, upper in enumerate(bricks):
            for i, lower in enumerate(bricks[:j]):
                uxs, uys, uzs, uxe, uye, _ = upper
                lxs, lys, _, lxe, lye, lze = lower

                if max(uxs, lxs) <= min(uxe, lxe) and max(uys, lys) <= min(uye, lye) and uzs == lze + 1:
                    k_to_v[i].add(j)
                    v_to_k[j].add(i)
    
        total = 0

        for i in range(len(bricks)):
            q = deque(j for j in k_to_v[i] if len(v_to_k[j]) == 1)
            falling = set(q)
            falling.add(i)

            while q:
                f = q.popleft()
                for k in k_to_v[f]:
                    if v_to_k[k] <= falling:
                        q.append(k)
                        falling.add(k)

            
            total += len(falling) - 1 

        return total




def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()