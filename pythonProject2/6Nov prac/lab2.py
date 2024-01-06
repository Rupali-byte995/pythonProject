# # # # print f
# # # n = int(input("Enter value of n"))
# # # print(f'2 x 1={n * 2}')
# str="this is pramod"
# # print(len(str))
# # print(str[0:4:2])
# # print(str[::-1])
# print(str.capitalize())
# print(str.capitalize())
# print(str.replace("pramod",'rupali'))
# print(str.find('pramod'))
# print(str.count('pramod'))
# l1=[1,2,'tt']
# l1[1]=88
# print(l1)
# s1={1,2,3,6,3}
# print(s1)
# l1=[1,2,3]
# l2=[1,2,3]
# print(l1 is l2)
# l3=[5,6,7,8]
# print(5 not in l3)
# x=5
# y=10
# print(y if x<y else x)
# str='Hello'
# str+='world'
# print(str)
# Use the ternary operator to find the maximum of three numbers entered by the user
# a=int(input("Enter a\n"))
# b=int(input("Enter b\n"))
# c=int(input("Enter c\n"))
# if a>b and a>c:
#     max=a
# elif b>a and b>c:
#     max=b
# else:
#     max=c
# print("Max is ",max)
# for i in range(10):
#     print(i)
# u=list(range(1,10,2))
# print(u)
"""
A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.
Use an if-else statement to make this determination.
"""
# year=int(input("Enter year to check if it leap year or not"))
# if year%4==0 or year%400==0 and year%100!=0:
#     print("Leap year")
# else:
#     print("Not a leap year")
# a=int(input("Eneter side a"))
# b=int(input("Eneter side b"))
# c=int(input("Eneter side c"))
# if a==b and a==c:
#     print("Equilateral")
# elif a==b or a==c or b==c:
#     print("Isosceles triangle")
# else:
#     print("Scelane triangle")

# for i in range(1,10):
#     if i==3:
#         continue
#     print(i)
# 5!=5*4*3*2*1
# n=int(input("Factorial  whose is to be calculated"))
# if n<0:
#     print("Negavtive number no")
# else:
#     fact=1
#     while n>0:
#         fact=fact*n
#         n-=1
#     print("factorial is :",fact)
# num=int(input("Enter till u want fibo series"))
# a,b=0,1
# i=0
# while i<=num:
#     a,b=b,a+b
#     print(a,end='\t')
#     i=i+1
# a=int(input("Eneter a"))
# b=int(input("Eneter b"))
# match a>b:
#     case True:
#         print("a is greater")
#     case False:
#         print("b is greater")
#
# def sum(a,b):
#   return a+b
# palindrome string
# pali=input("Eneter string ")
# rev_string=""
# for i in pali:
#     rev_string=i+rev_string
# print(rev_string)
# if(rev_string==pali):
#     print("Palindrome")
# else:
#     print("Not a palindrome")
# if(pali==pali[::-1]):
#     print("palindrome")
# else:
#     print("Not a plaindrome")
# sum of digit
# num=12345
# sum=0
# while num!=0:
#     digit=num%10
#     sum=sum+digit
#     num=int(num/10)
# print(sum)
# num=int(input("Enter num"))
# dig = 0
# rev = 0
# sum=0
# while num > 0:
#     dig = num % 10
#     sum= sum + dig
#     num = int(num / 10)
# print(sum)
# a=lambda a:a**3
# print(a(4))
#       col 1   col2
# *
# * *
# ***
# ****
# *****
# n=4
#
# for i in range (1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()
# vowels and consonents in a string
# count_str = input("Enter the string ")
# count_vow = 0
# count_conso = 0
# for c in count_str:
#     if (c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u'):
#         count_vow += 1
#     else:
#         count_conso += 1
# print("Vowels", count_vow)
# print("consonants", count_conso)
"""
input_string=input("Enter string whose vowel and consonant should be counted")
count_vowels=0
count_cons=0
for c in input_string:
    if(c=='a'or c=='e' or c=='i' or c=='o' or c=='u'):
        count_vowels=count_vowels +1
    else:
        count_cons=count_cons+1
print("Vowels=",count_vowels)
print("Consonants=",count_cons)"""


# l1=[1,2,3,4]
# # l1.append(5)
# # print(l1)
# # l1.extend([8,9])
# # print(l1)
# l1.insert(1,5)
# print(l1)
# # l2=l1.copy()
#
# # l1.append(8)
# # print(l2)
# l1.pop()
# print(l1)
# l1 = [1, 2, 3, 4]
# l2=[8,9]
# print(l1+l2)
# def sq(x):
#     return x*x
# print(list(map(sq,l1)))
# #list-[]
# # set={}
# #tuple-()
# s1={1,2,3}
# s2={2,3,4}
# print(s1.union(s2))
# print(s2.issubset(s1))
# my_dict={'bat':1,'cat':2}
# print(my_dict['bat'])
# print(my_dict.get('bat'))
# for k,v in my_dict.items():
#     print(k,v)
# from collections import OrderedDict
# od=OrderedDict()
# od['bat']=1
# od['cat']=5
# for k,v in od.items():
#     print(k,v)
class Person:
    name = 'Amit'
    age = 56
    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

    #     def p_print(self):
    #         print("name=",self.name)
    #         print("Age=",self.age)
    #
    # amit=Person()
    # amit.p_print()
    # class Person:
    #     def __init__(self, name, age):
    #         self.__name = name
    #         self.__age = age
    #
    #     def print_details(self):
    #         print("Name:", self.__name, 'Age', self.__age)
    #
    #     def get_details(self):
    #         return self.__name, self.__age
    #
    #     def set_name(self, name, age):
    #         self.__name = name
    #         self.__age = age
    #         print("Name::", self.__name, self.__age)
    #
    #
    # per = Person('rupali', 26)
    # per.print_details()
    # per.set_name('pramod',28)
    # class A:
    #     def greet(self):
    #         print("class A")
    # class B:
    #     def greet(self):
    #         print("class B")
    # class C(A,B):
    pass


# class D(B,A):
#     pass
# obj1=C()
# obj2=D()
# class Animal :
#     def sound(self):
#         print("Animal sound")
# class cat(Animal):
#     def sound(self):
#         print(" I am in cat class")
#         super().sound()
# obj1=cat()
# obj1.sound()
from abc import ABC, abstractmethod


# class Animal(ABC):
#     @abstractmethod
#
#     def sound(self):
#         pass
#
#
# class Dog(Animal):
#     def sound(self):
#         print("I am in")
# d=Dog()
# d.sound()
#Reading a file
# f=open('rt.txt','r')
# print(f.read())
# f.close()
f=open('rt1.txt','a')
f.write("I am rt1 write 2 mode")
