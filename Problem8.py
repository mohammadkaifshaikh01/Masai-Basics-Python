# You are given five numbers, stored in the variables with the following names
# one, two, three, four, five
# All the values are doubled, that is, they are multiplied by 2
# Find the sum of the values stored in one, two, three, four , after the above operation are performed

def doubleAll(one,two,three,four,five):
   A = one * 2
   B = two * 2
   C = three * 2
   D = four * 2
   E = five * 2

   print(A+B+C+D+E)

one,two,three,four,five = map(int,input().split())
doubleAll(one,two,three,four,five)