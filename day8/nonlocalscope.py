def outer():
    x = 'outer'
    def inner():
        nonlocal x
        x = 'inner'
    inner()
    print(x)
outer()


# In this context, `nonlocal x` declares that the `x` variable inside the `inner()` function refers to the `x` variable
# in the nearest enclosing scope (the `outer()` function), allowing `inner()` to modify the `x` from `outer()` rather
# than creating a new local variable.