from collections import deque


class Solution:

    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        return data

    def part_one(self):
        data = self.read_data().split("\n\n")
        
        seeds = [int(i) for i in data[0].split(" ")[1:]]
        mappings = [[list(map(int, row.split())) for row in mapping.split("\n")[1:]] for mapping in data[1:]]
        
        for mapping in mappings:
            for i, seed in enumerate(seeds):
                for row in mapping:
                    dst, src, n = row
                    if seed >= src and seed < src + n:
                        seeds[i] = seed - src + dst
                        break
        return min(seeds)

    def part_two(self):
        data = self.read_data().split("\n\n")
        
        seeds = [int(i) for i in data[0].split()[1:]]
        seeds_ranges = deque([(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)])
        mappings = []

        for mapping in data[1:]:
            rows = []
            for row in mapping.split("\n")[1:]:
                # Split on whitespace and convert to ints
                rows.append(list(map(int, row.split())))
            # Sort by src, ascending
            mappings.append(sorted(rows, key=lambda x: x[1]))
                

        for mapping in mappings:
            cur_seeds_len = len(seeds_ranges)
            for _ in range(cur_seeds_len):
                start, seed_range = seeds_ranges.popleft()
                
                for row in mapping:
                    dst, src, n = row

                    if start + seed_range <= src:
                        seeds_ranges.append((start, seed_range))
                        seed_range = 0
                        break

                    if start >= src + n:
                        continue

                    
                    if start < src:
                        crop_start = start
                        crop_length = src - start
                        seeds_ranges.append((crop_start, crop_length))
                        start = src
                        seed_range -= crop_length

                    
                    dst_start = start - src + dst
                    range_end = min(src + n - 1, start + seed_range - 1)
                    range_length = range_end - start + 1
                    seeds_ranges.append((dst_start, range_length))

                    start = range_end + 1
                    seed_range -= range_length

                    if seed_range == 0:
                        break
                
                if seed_range > 0:
                    seeds_ranges.append((start, seed_range))
                        

        lowest_location = float("inf")
        for seed in seeds_ranges:
            lowest_location = min(lowest_location, seed[0])           
        return lowest_location
                        

def main():
    s = Solution()
    # print(s.part_one())
    print(s.part_two())

main()