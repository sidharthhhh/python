def counter():
    count = [0]
    def increment():
        count[0] += 1
        return count[0]
    return increment

c = counter()
print(c())  # Output: 1
print(c())  # Output: 2

# counter() function:

# Defines a list count = [0]. Using a list allows us to modify its content even within the inner function.
# Defines an inner function increment().
# Returns the increment function.


# increment() function:

# Accesses the count list from its enclosing scope.
# Increments the value in count[0] by 1.
# Returns the new value of count[0].


# c = counter():

# Calls counter() and assigns the returned increment function to c.
# c now holds a reference to increment, which has access to the count list in its closure.


# print(c()):

# First call: Increments count[0] from 0 to 1 and returns 1.
# Second call: Increments count[0] from 1 to 2 and returns 2.