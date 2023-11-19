# filter
# write positive numbers
num = [-1, 2, -8, 6, 3, -10, 0]


def is_positive(num):
    return num >= 0


pos_num = list(filter(is_positive, num))
print(pos_num)
