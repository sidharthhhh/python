# lenn = input("write the string: ")
# count = 0
# for char in lenn:
#     count+=1
# print(count)


# toggle each character in the string:- upper case to lower case ma and lower case ko upper case ma

# def toogle(char):
#     char2 = char.swapcase()
#     print(char2) 

# toogle("hello")

# count the no. of vowel in the string
vowelCount = input("enter the string: ")

count = 0

vowelCount = vowelCount.lower()
for i in vowelCount:
    if i == 'a' or i == 'e' or i=='i' or i=='o' or i=='u':
      count+=1
if count==0:
    print("koii viwel nai hai")
else:
    print(str(count) + "vowel count")
    # print(count + "vowel count")    # int and string ka concatination karra tha ye


