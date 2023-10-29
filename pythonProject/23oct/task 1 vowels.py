#  Count vowels and consonants in a String
# aeiou
# input = pramod
# vol = 2

input_string=input("Enter string whose vowel and consonant should be counted")
count_vowels=0
count_cons=0
for c in input_string:
    if(c=='a'or c=='e' or c=='i' or c=='o' or c=='u'):
        count_vowels=count_vowels +1
    else:
        count_cons=count_cons+1
print("Vowels=",count_vowels)
print("Consonants=",count_cons)

