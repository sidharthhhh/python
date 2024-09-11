# str = "hello"
# reverseStr = ""
# for i in str:
#     reverseStr=i+reverseStr
# print(reverseStr)


# question 2: - find first non repetable character

# input_str = "hhhhhellloworld"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print(char)
#         break

input_str = "hhhhhellloworld"

for char in input_str:
    count = input_str.count(char)
    print(f"Checking '{char}': appears {count} time(s)")
    if count == 1:
        print(f"First non-repeatable character: {char}")
        break
