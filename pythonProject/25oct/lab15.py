numbers=[1,2,3,4,5]
sq=lambda x: x*x
# new_square=[]
# for i in numbers:
#     new_square.append(sq(i))
# print(new_square)

new_sq=list(map(lambda x:x*x,numbers))
print(new_sq)