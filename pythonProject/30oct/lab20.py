my_dict={'a':1,'b':2,'c':3,'a':9}
keys=list(my_dict.keys())
values=list(my_dict.values())
print(values[0])
#my_dict.clear()

#print(my_dictf)
my_copy_dict=my_dict.copy()
print(my_copy_dict)
print(set(my_copy_dict.items()))
my_dict={'a':1,'b':2,'c':3,'d':1 }
#print(my_dict.pop('a'))
# how to iterate  items in dictionary
# for k,v in my_dict.items():
#     print(k)
#     print(v)
print(my_dict.popitem())
my_dict['r']=88
my_dict['f']=89
#my_dict={'a':1,'b':2,'c':3,'d':1 }
my_dict={'ff':78,'hh':56,'ll':89,True:123}
print(my_dict.items())
my_dict['r']=88
my_dict['f']=89
print(my_dict.items())
print(my_dict[True])