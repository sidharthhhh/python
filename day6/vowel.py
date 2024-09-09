# user se input lena hai and check karna hai kitne vowel and oor kitne consonent

# def check(string):
#     vowels = 'aeiouAEIOU'
#     vowelCount=0
#     consonentCount=0

#     for char in string:
#       if char.isalpha():
#           if char in vowels:
#             vowelCount+=1
#           else:
#             consonentCount+=1
#     return vowelCount, consonentCount

# userInput = input("enter string only: ")


# vowels, consonants = check(userInput)

# # Print the results
# print(f"Number of vowels: {vowels}")
# print(f"Number of consonants: {consonants}")






# check it contain alphabat or not
character = input("write strint: ")
if 97 <= ord(character) <= 122 or 65 <= ord(character) <=90:
    print(character + " is correct")
else:
    print(character + " is not correct")

