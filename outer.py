def outer_func(x):
    def inner_func():
        return x*5
    return inner_func()


print(outer_func(10))