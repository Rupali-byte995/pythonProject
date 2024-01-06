# Read a file
# with open('pramod.txt', 'r') as file:
#     content = file.read()
#     print(content)
# write to a file
# with open('example.txt','w') as file:
#     file.write('hello i am fresh')
# append to a file
# with open('example.txt','a') as file:
#     file.write('\nI am appended data')

# with open('pramod.txt','r') as file:
# #print(file.readline())
#    contents=file.readlines()
# for line in contents:
#         print(line,end='')
import csv

with open('data.csv') as csvfile:
    reader = csv.reader(csvfile)
    for x in reader:
        pr

        int(x)
