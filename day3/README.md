## Part One: Sliding Window Approach

In this quest, a sliding window of height 3 (or 2 at the edges) is employed to process numbers and their adjacent symbols. The algorithm consists of four key steps:

1. **No Symbol and Number:**

   - If there is neither a symbol nor a number in the current window, set `is_adjacent` to false.

2. **Symbol Presence:**

   - If a symbol is found in the window, set `is_adjacent` to true.

3. **Number Processing:**

   - When encountering a number:
     - Check if a symbol exists in the window.
     - If true, pass `is_adjacent` to the next iteration. The preceding window might contain the symbol (adjacent on the left side).

4. **Number Read Completion:**
   - When there is no number, and the read number is not 0 (indicating completion of number reading):
     - Check if there is a symbol in the current window (adjacent to the right side).
     - If adjacent, add to the total and clear the read number.

Additionally, account for reading a number at the edge of the line after the iteration.

## Part Two

- **Data Preparation:**

  - Create a copy of the input data, retaining only the numerical values.
  - Expand each digit to its full version. For example, [1, 2, 3] becomes [123, 123, 123].

- **Algorithm Implementation:**
  - Iterate over the input data.
  - Locate each "\*" occurrence.
  - Create a 3x3 window (or smaller near edges) centered at the "\*" coordinates using prepared data. Window contains all adjacent numbers.
  - Extract all unique numbers from each row of the window.
  - If the count of adjacent numbers is 2:
    - Multiply the two numbers.
    - Add to the result
