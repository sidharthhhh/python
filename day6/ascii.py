# print(ord("a")) #97
# print(chr(97))

# 97-112 -> lower case
# 65-90 -> upper case

# def check(character):
#     if(ord(character) in range(97,113)):
#         print("lower case")
#     elif(ord(character) in range(65,91)):
#         print("upper case")
#     else:
#         print('something wrong')

# check("N")    # ord() use karne input character hi dena haii




# isapha() is a buildin string method which check character is an alphabat or not

# Shifting a character by 3 places (Caesar Cipher)
def shift_character(char, shift):
    if char.isalpha():
        base = 65 if char.isupper() else 97
        return chr((ord(char) - base + shift) % 26 + base)
    else:
        return char

print(shift_character('A', 3))  # Output: 'D'
print(shift_character('m', 3))  # Output: 'p'
print(shift_character('2', 3))  # Output: '2'

# ord(char) gets the ASCII value of the character.
# ord(char) - base shifts the ASCII value to the range starting from 0 (either 0-25 for uppercase or 0-25 for lowercase).
# + shift applies the requested shift to the character.
# % 26 ensures the shifted value wraps around to the beginning of the alphabet if it goes beyond 'Z' or 'z'.
# + base shifts the value back to the correct ASCII range for uppercase or lowercase letters.
# chr() converts the resulting ASCII value back to a character and returns it.