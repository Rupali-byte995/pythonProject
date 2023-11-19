"""
Program 1:

Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25, 36, 42, 10)





Program 2:

Find the intersection and union of two sets.



set1 = {1, 2, 3, 4, 5}

set2 = {3, 4, 5, 6, 7}





Program 3:

Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]





Program 4:

Remove a key-value pair from the dictionary.





Program 5:

Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

{

"bookingid": 2384,

"booking": {

"firstname": "PRAMOD",

"lastname": "Dutta",

"totalprice": 432,

"depositpaid": False,

"bookingdates": {

"checkin": "2022-01-01",

"checkout": "2022-01-01"

},

"additionalneeds": "Lunch"

}

}


"""
# Program 1:
#
# Find the maximum and minimum elements in a tuple.
#
my_tuple = (15, 8, 25, 36, 42, 10)
print(max(my_tuple))
# Program 2:
# Find the intersection and union of two sets.
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("Union: ",set1.union(set2))
print("Intersection: ",set1.intersection(set2))
# Program 3:
# Remove duplicate elements from a list.
my_list = [1, 2, 2, 3, 4, 4, 5]
my_set=set(my_list)
print(my_set)
# Program 4:
# Remove a key-value pair from the dictionary.
my_dict={'a':1,'b':2,'c':3}
del my_dict['a']
print(my_dict)
#Program 5:

# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data
# {
# "bookingid": 2384,
#
# "booking": {
#
# "firstname": "PRAMOD",
#
# "lastname": "Dutta",
#
# "totalprice": 432,
#
# "depositpaid": False,
#
# "bookingdates": {
#
# "checkin": "2022-01-01",
#
# "checkout": "2022-01-01"
#
# },
# "additionalneeds": "Lunch"
# }
# }
mybooking={
"bookingid": 2384,
"booking": {"firstname": "PRAMOD","lastname": "Dutta","totalprice": 432,"depositpaid": False,
"bookingdates": {"checkin": "2022-01-01","checkout": "2022-01-01"
}},"additionalneeds": "Lunch"
}
print("Booking id : ",mybooking.get('bookingid'))
print("Checkin",mybooking.get("booking").get('bookingdates').get('checkin'))
print("Checkout",mybooking.get("booking").get('bookingdates').get('checkout'))