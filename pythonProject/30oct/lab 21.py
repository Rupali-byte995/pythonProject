#ordered Dict
from collections import OrderedDict
od=OrderedDict()
# od['a']=21
# od['b']=22
# od['c']=24
# print(od.items())
# od['d']=25
# print(od.items())
od['a']=1
od['d']=2
od['b']=3
print(od)
#now sorting the keys
keys=list(od.keys())
key_sort=sorted(keys,reverse=True)


# print(key_sort)
# od2=OrderedDict()
# od2[key_sort[0]]=56
# od2[key_sort[1]]=78
# print(od2)
