# # Exception
# try:
#     a = 10 / 0
# except Exception as e:
#     print("You have an error",e)
#try else except finally
try:
    num1=int(input("Enter num1"))
    num2=int(input("Enter num2"))
    print(num1/num2)
except Exception as e:
           print("Exception :",e)
else:
    print("I am in else block")
finally:
    print("I am in finally block")
