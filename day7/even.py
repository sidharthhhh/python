# num = [1,2,3,4,5,6,7,8,9]
# count = 0

# for i in num:
#     if i % 2 == 0:
#         count=count + i
# print(count)

# example 2 :- calculate the sum of even no. up to number n
n = int(input("write your number: "))

def sumOfEvenNo(n):
    sum_even = 0
    for i in range(0,n+1):
        if i%2==0:
          sum_even=sum_even+i
    print(sum_even)
sumOfEvenNo(n)

