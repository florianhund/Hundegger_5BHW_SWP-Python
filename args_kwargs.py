def outer_function(*args, **kwargs):
    def inner_sum():
        return sum(args)

    def inner_print_kwargs():
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    sum_result = inner_sum()
    print("Summe der args:", sum_result)
    print("Inhalt von kwargs:")
    inner_print_kwargs()

    return sum_result


result = outer_function(1, 2, 3, 4, 5, name="Alice", age=30, city="Berlin")
