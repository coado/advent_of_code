## Part One - BFS

In this part, we iterate over each mapping, checking if any seed lies within its range. If a seed is found, we update it to its corresponding destination value; otherwise, we move on to the next seed.

## Part Two - BFS, Queue and Intervals

In this part, instead of single seed points, we are provided with seed ranges. The challenge lies in dealing with potential overlaps between a given seed range and multiple mapping ranges, resulting in different destinations for various segments of the seed range.

1. We begin by parsing all given seed ranges and storing them in a `deque` data structure. This choice is made due to the `deque` providing O(1) time complexity for both append and pop operations on both ends of the list.

2. To ensure accurate comparisons, we sort mapping ranges by their source values in ascending order.

3. For each mapping, we extract new mapped ranges based on the source ranges currently present in the queue. The process involves dequeuing from the left side and enqueuing the newly mapped range at the end. Before the loop, we save the initial length of the queue to track the number of source mappings.

   - If the end of the seed range is before the beginning of the mapping range, there is no overlap, and we append the same seed range to the queue.

   - If the beginning of the seed range is after the end of the mapping range, we proceed to the next iteration.

   - Otherwise, the ranges overlap. We check if the start of the seed range is lower than the start of the mapping range. If true, we crop the non-overlapping part and enqueue it. Now, we ensure the start of the seed range is at least equal to the mapping range. The end of the seed range may exceed the end of the mapping range, so we only consider overlapping values, pushing the mapped range to the queue.

After processing all mappings, there might be a range left without a corresponding mapping, which is also added to the queue.

Finally, the result is the lowest location from the ranges in the queue.
