def even_odd(*args):
    command = args[-1]
    nums = args[:-1]

    if command == "even":
        return list(filter((lambda x: x % 2 == 0), nums))
    elif command == "odd":
        return list(filter((lambda x: x % 2 != 0), nums))

print(even_odd(1, 2, 3, 4, 5, 6, "even"))