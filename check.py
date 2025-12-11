# assert True # whatever that is true, returns nothing
# assert 3 + 3 == 6 # since it's true, it returns nothing back
# assert False # returns error
# assert False, "that's false"


def my_add(x, y): 
    return x - y


my_add(1, 2) == 3

assert my_add(1, 2) == 3   # this is the idea of unittesting

calculated = my_add(1, 2)
excepted = 3
assert calculated == excepted   # if it's too long, can split into variables




