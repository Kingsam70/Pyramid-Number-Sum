# Calculating the sum of all the numbers in the nth position/row of the following pyramid:

"""
                        1
                    2       3
                4       5       6
            7       8       9       10
        11      12      13      14      15
    16      17      18      19      20      21
22      23      24      25      26      27      28
                        .
                        .
"""


# Finding the sum of all the numbers in the nth position of the above pyramid
# Observations:
    # 1 --> at position/row no 1, and line containing exactly one element i.e: 1
    # 2 --> at position/row no 2, and line containing exactly two elements that are: 2 and 3
    # Similarly at nth position number of elements will be 'n' who's sum we want to find.

# Procedure Theory:
    # If we were able to show relation between the very first element of the line(1, 2, 4, 7, etc) and the
    # position of that element, we would get a sequence/formulae to determine what exactly would be  the first
    # element/number, and we know at nth line no of elements/numbers would also be 'n', so we could find the sum

# Let's say that position (of the line we want to find the sum) is odd:
    # so i.e:
        # 1 --> 1
        # 3 --> 4   where 3 is the position and 4 is the value of the very starting element/number
        # 5 --> 11   similarly 5 is the odd position and 11 is the value
        # 7 --> 22
        # 9 --> 37  you can find what the value of starting no will be by looking at the original
            # sequence: (1, 2, 4, 7, 11, ...)

    # More elaborately:
        # 3, 5, 7 are the positions below:
            # 3 --> 4  ==> 3 * 1 + 1 = 4
            # 5 --> 11 ==> 5 * 2 + 1 = 11
            # 7 --> 22 ==> 7 * 3 + 1 == 22

        # we can easily see the pattern/relation between the starting value and the number i.e:
            # starting no = (n * ((n-1)/2)) + 1  <== this can be confirmed by putting values of positions.


# Let's say that position (of the line we want to find the sum) is even:
    # so i.e:
        # 2 --> 2
        # 4 --> 7  where 4 is the position and 7 is the value of the very stating element/number
        # 6 --> 16
        # 8 --> 29
        # 10 --> 46

    # More elaborately:
        # 2, 4, 6 are the positions below:
            # 4 --> 7 ==> 4 * 2 - 1
            # 6 --> 16 ==> 6 * 3 - 2
            # 8 --> 29 ==> 8 * 4 - 3

    # we can easily see the pattern/relation between the starting value and the number i.e:
        # starting no = ((n * (n/2)) - ((n/2) - 1)) <== this can be confirmed by putting values of positions.

# Actual coding:

# Prompt the user to enter the row number/position of the pyramid to calculate the sum
position = float(input("Enter the row number/position of the pyramid to calculate the sum: "))
# Convert the float value to an integer to ensure only valid positions are used
position = int(position)

# Making starting_no int as to avoid floating zero
if position % 2 == 0:  # meaning its even number
    starting_no = int(((position * (position/2)) - ((position/2) - 1)))
else:
    starting_no = int((position * ((position-1)/2)) + 1)

total_sum = 0
for num in range(position):
    total_sum += starting_no + num

print(f"\n{total_sum}")
print(f"At row {position} sum of the numbers will be: {total_sum}")
