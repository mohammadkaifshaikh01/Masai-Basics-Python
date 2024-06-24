# You are given three numbers, stored in variables with the following names
# one, two, three
# You have to find the square of the three numbers, and find the sum of their square values
# Note : Square of a number, is a number multiplied by itself. For example, the square of 3, is 3 * 3 = 9


def calculate_sum_of_square(one,two,three):
  square = one*one
  square2 = two*two
  square3 = three*three
  print(square + square2 + square3)

one,two,three= map(int,input().split())
calculate_sum_of_square(one,two,three)