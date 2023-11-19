product=[{'name':'laptop','price':1000},{'name':'Smartphone','price':500},{'name':'tablet','price':300},
         {'name':'headphone','price':400}]

#print(product[0]['name'])
def is_afford(w):
    return w['price']<500

affordable_product=list(filter(is_afford,product))
# print(affordable_product[0]['name'],affordable_product[0]['price'])
# print(type(affordable_product[1]))
for i in affordable_product:
    print(i['name']+str(i['price']))