# You are given a number X. Find the value of X, if
# 1. X is multiplied by 3
# 2. 10 is added to the new value of X.




def calculate_value(X):

   mul = X*3
   add = mul + 10
   print(add) 


X = int(input())
calculate_value(X)