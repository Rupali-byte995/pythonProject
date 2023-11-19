#counter in collections
word=['red','blue','red','blue','violet']
from collections import Counter
cnt=Counter()
for x in word:
    cnt[x]=cnt[x]+1
print(cnt)

#Ordered Dictionary
from collections import OrderedDict
d=OrderedDict()
d['a']='A'
d['b']='B'
d['c']='C'
for k,v in d.items():
    print(k,v)