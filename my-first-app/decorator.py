def first_func():
    print("This is my first function")


def second_func(func):
    print("This is my second function")
    return func


my_func = second_func(first_func)
