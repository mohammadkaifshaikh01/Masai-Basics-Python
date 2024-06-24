# You are given six numbers, stored in variables with the following names
#  one, two, three, four, five, six
# Print the product of all the six numbers



def calculate_products(one,two,three,four,five,six):
   print(one*two*three*four*five*six)


one,two,three,four,five,six = map(int,input().split())
calculate_products(one,two,three,four,five,six)