def multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
# print(double)
print(double(5)) 


# n is 2, as it's passed to multiplier(2) when creating the double function.
# x is 5, as it's passed to double(5) when calling the returned multiply function.

# The closure multiply remembers n=2 from its creation, then multiplies it by the input x=5, resulting in 10.