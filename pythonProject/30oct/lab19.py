#Dictionary
my_dict={}
mydic2=dict()
my_phonebook={
    "Batman":9855,
    "Superwoman":8799,
    "Wonder":563666,
    "90":56
}
print(len(my_phonebook))
#accessing element of the dictionary
print(my_phonebook["Batman"])
# 2nd way of creating dictionary
my_phone=dict(bat=123,wonder=456)
print(my_phone.get('bat'))
pramod_details=dict(name="Pramod",age=34,address="KA")
print(pramod_details.get('name'))
print(pramod_details['name'])
# print(my_phonebook[90])
print(my_phonebook.get("90"))
print(list(my_phonebook.values()))