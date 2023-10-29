#set
set1=set("pramod")
print(set1)
set1={1,2,3,4,5,5}
print(set1)
#union and intersection
set1={1,2,3,4,5}
set2={5,6,7,8,9}
my_union_set=set1.union(set2)
print(my_union_set)
myset_int=set1.intersection(set2)
print(myset_int)
#diffrence
my_set_diff=set1.difference(set2)
print(my_set_diff)
#subset
print(set2.issubset(set1))#false
#all elemnts of set 1 should be present in set 2 then it will come as true