# You are given a number, stored in a variable with the name number . Perform the following operations on the value stored in the number
# 1. Multiply the value by 3
# 2. Add 7 after it
# 3. Subtract 10 from it
# After performing all the above operations, print the updated value


def operationNumber(Number):

   mul = Number*3
   add = mul+7
   sub = add-10
   print(sub)

Number = int(input())
operationNumber(Number)