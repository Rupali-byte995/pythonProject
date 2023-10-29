#list
my_list=[1,0,2,3,89,56]
print("my list at 0 index",my_list[0])
#append
my_list.append(6)
print("After append",my_list)
my_list.extend([8,9])
print("After extending",my_list)
my_list.insert(1,'a')
print("After insert function use ", my_list)
my_list.remove('a')
print("After removal",my_list)
my_copiedlist=my_list.copy()
print(my_copiedlist)
#clear
my_copiedlist.clear()
print(my_copiedlist )
#index
print(my_list.index(1))
#sort
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list )
#copy one list to another
l1=[1,2,3,4]
l2=l1

print(l2)
l3=l1.copy()
print("l3=",l3)
l1[0]=89
print("l2",l2)
print("l3",l3)
print("length of l1",len(l1))
print("count of 3 in l1",l1.count(3))
