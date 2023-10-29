# Right Triangle Star Pattern
"""
      col 1   col2
row 0 *
row 1 *      *
***
****
*****
"""
n = int(input("enter the number to form pyramid:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
