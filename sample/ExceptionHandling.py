from functools import reduce

print((lambda a, b: a + b)(1, 3))


class CustomException(Exception):
    def __str__(self) -> str:
        return f"EXCEPTION -- value = {self.total} , {self.message}"

    # *args will be used to accumulate exceptions i guess TODO
    def __init__(self, total, message, *args) -> None:
        super().__init__(*args)
        self.total = total
        self.message = message


def sum_numbers_with_multi_args(*args):
    return reduce(lambda x, y: x + y, args)


def sum_numbers(numbers):
    total = 0
    try:
        total = reduce(lambda x, y: x + y, numbers)
        if total > 100:
            raise CustomException("sum is greater than 100")
    except TypeError as a:
        print("error occurred", a)
        print("exception type", type(a))
        raise TypeError("cant perform sum")
    else:
        # if there is a return in try then else is unreachable
        print("from else")
    finally:
        print("reached finally ")
        return total


# if there is a return in finally then exception is not propagated
def sum_numbers_without_finally(numbers):
    try:
        total = reduce(lambda x, y: x + y, numbers)
        if total > 100:
            raise CustomException(total, "total cannot be greater than 100")
        return total
    except TypeError as a:
        print("TypeError --- >>", a)
        # raise here will rethrow
        raise a
    except CustomException as custom_exception:
        print(custom_exception)
        return str(custom_exception)


print(sum_numbers_with_multi_args(1, 3, 4, 6))
# list tuple are considered as single element if we pass to *args
print(sum_numbers_with_multi_args(tuple(range(1, 10))))
print(sum_numbers_with_multi_args(list(range(1, 10))))
# print("sum_numbers -- ", sum_numbers(range(1, 10)))
mixed_list = list(("abc", 1, "a", 2))
# as there is a return in finally the exception didn't came here
print("sum_mixed_numbers -- ", sum_numbers(mixed_list))
print("sum_mixed_numbers_without_finally_success -- ", sum_numbers_without_finally((1, 2, 3, 99)))
print("sum_mixed_numbers_without_finally -- ", sum_numbers_without_finally(mixed_list))
