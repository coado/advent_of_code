## Part one

Iterate over characters in each line. Whenever we find a digit, we always want to update the last_digit. The first_digit is set only once. After the line is processed, we update the result.

## Part two

The main difference from part one is that we also want to look for substrings. On each character, we check if it is a digit. If yes, we do the same thing as in part one. Otherwise, we iterate over an array of words, which contains names of digits, and check if we read any digit as a string ("one", "two", ...). If true, we change the string to the integer and update our variables.
