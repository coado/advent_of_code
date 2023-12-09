## Part One ⭐

The brute-force approach involves checking every possible time and comparing the distance reached with the current record. However, a more efficient solution exists. By using a quadratic equation of the form:

`y = x * (time - x) - distance`

Here, 'x' represents the time taken, and 'y' calculates the distance reached. Subtracting the actual distance from this equation helps shift it down, positioning the zero points at the times when the race record was achieved. The region between these zero points represents all possible times that can beat the record. The solution involves calculating the number of times within this range plus 1 (including the last time), offering a more optimized approach than a brute-force method.

## Part Two ⭐⭐

Part two builds upon the approach from part one, utilizing the same quadratic equation:

`y = x * (time - x) - distance`

This equation helps identify the time instances when the race record is either reached or surpassed. By leveraging the properties of this quadratic graph, the algorithm efficiently calculates the number of ways to beat the record. The simplicity and effectiveness of the equation streamline the solution to the given problem.


![image](https://github.com/coado/advent_of_code_2023/assets/64146291/13ac9605-1a89-41a8-b57a-fefab62f0708)
