import timeit

class Solution:
    def read_data(self):
        with open("data.txt", "r") as f:
            data = f.read()
        
        return data
    

    def label_hash(self, label):
        res = 0
        for char in label:
            res += ord(char)
            res *= 17
            res %= 256
        return res
    
    def find_lens_index(self, label, box):
        res = -1
        for i, lens in enumerate(box):
            if lens[0] == label:
                res = i
                break 
        return res
    
    def run(self):
        data = self.read_data().strip().split(',')

        boxes = {}
        
        for sequence in data:
            label, focal_length = '', None

            if sequence[-1] == '-':
                label = sequence[:-1]
            else:
                focal_length = int(sequence[-1])
                label = sequence[:-2]

            box = self.label_hash(label)

            if box not in boxes:
                if focal_length is None:
                    continue
                boxes[box] = []
            
            # (label, focal_length)
            if focal_length is None:
                # find the lens with the same label and remove it
                boxes[box] = [lens for lens in boxes[box] if lens[0] != label]

                # remove the box if it is empty
                if not boxes[box]:
                    del boxes[box]
            else:
                # check if it is already in the list
                lens_index = self.find_lens_index(label, boxes[box])
                if lens_index == -1:
                    # add the lens
                    boxes[box].append((label, focal_length))
                else:
                    # update the focal length
                    boxes[box][lens_index] = (label, focal_length)
                
        res = 0
        # iterate over boxes
        for i, box in boxes.items():
            for slot_index, lens in enumerate(box):
                label = lens[0]
                focal_length = lens[1]
                focusing_power = (1 + i) * (slot_index + 1) * focal_length
                res += focusing_power

        return res




def main():
    sol = Solution()
    print(f"Part Two: {sol.run()}")
    # elapsed = (timeit.timeit(sol.run, number=10) / 10) * 1000
    # print(f"Elapsed Time: {elapsed:.3f} ms")

main()