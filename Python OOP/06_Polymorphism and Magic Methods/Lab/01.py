# def execute(function, *args):
#     return function(*args)

execute = lambda fn, *args: fn(*args)

def say_hello(name, my_name):
    print(f"Hello, {name}, I am {my_name}")

def say_bye(name):
    print(f"Bye, {name}")

execute(say_hello, "Peter", "George")
execute(say_bye, "Peter")
