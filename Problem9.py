
#You are given 7 numbers A, B, C, D, E, F, G. Find out the product of (A + B + C) and (D + E + F + G)

def calculate_Products(a,b,c,d,e,f,g):
   Add = a + b + c
   Add2 = d + e + f + g
   Product = Add * Add2
   print(Product) 



a,b,c,d,e,f,g = map(int,input().split())
calculate_Products(a,b,c,d,e,f,g)