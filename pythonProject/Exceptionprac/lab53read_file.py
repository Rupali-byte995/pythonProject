# File I/O in python
# Read a file
# f = open('rupali.txt', 'r')
# print(f.read())
# f.close()
# # Append a file
# f1 = open('rupali.txt', 'a')
# f1.write("Yes i have append data")
# f1.close()
# f = open('rupali.txt', 'r')
# print(f.read())
# f.close()
# # file is present in diffrent folder
# # f2=open('../30oct/rr.txt','r')
# # print(f2.read())
# f3 = open('r2.txt', 'a')
# f3.write("You are appending in non existing file")
# f3.close()
# f3 = open('r2.txt', 'w')
# f3.write("UUUU")
# f3.close()
# try:
#     f = open('r4.txt', 'r')
#     print(f.read())
# except Exception as e:
#     print("Error", e)
try:
    file = open('rupali3.txt', 'r')
    print(file.read())
except Exception as e:
    print(e)
finally:
    if file:
        file.close()
        print("File closed successfully")
