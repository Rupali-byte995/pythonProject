input_string=input("enter the palindrome check")
#ABCD
# def pali_checker(input_string):
#     rev_string=""
#     for c in input_string:
#         rev_string=c+rev_string
#     return rev_string
# reverse=pali_checker(input_string)
# if(reverse==input_string):
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# Using built in method
if(input_string==input_string[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")
