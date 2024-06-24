# You are given five numbers stored in variables with the following names
# one, two, three, four, five
# Find the sum of the five values, and print it



def findSum(one,two,three,four,five):
   print(one+two+three+four+five)


one,two,three,four,five= map (int,input().split())
findSum(one,two,three,four,five)