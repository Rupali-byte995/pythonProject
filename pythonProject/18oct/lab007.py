# """
# for i in range(1, 10):
#     if (i % 2 == 0):
#         print("Found an even number")
#         continue
#     print(f'Odd number  {i}')
#
# """
# count = 1
# while count <= 100:
#     print(count)
#     if count ==51:
#         break
#     count = count + 1
# factorial
num = int(input("Enter whose factorial needs to be calculated"))
if num < 0:
    print("For factorial number cannot be negative")
else:
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
print("Factorial is ", fact)
