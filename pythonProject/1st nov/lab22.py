# filter
#write even numbers
numbers = [1, 2, 3, 4, 5, 6]


def is_even(number):
    return number % 2 == 0


even = list(filter(is_even, numbers))
print(even)
