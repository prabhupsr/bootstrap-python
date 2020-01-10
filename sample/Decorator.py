def method_decorator(function):
    def wrp_fn(numbers):
        print(function)
        function(numbers)
        print("execution completed")

    return wrp_fn


@method_decorator
def sum_numbers(numbers):
    print(sum(numbers))


def method_decorator_with_return(function):
    def wrp_fn(*list_args, **key_value_args):
        print(function.__name__)
        return function(*list_args, **key_value_args)

    return wrp_fn


@method_decorator_with_return
def sum_numbers_with_rtn(numbers):
    return sum(numbers)


sum_numbers([1, 9, 12, 67])
print(sum_numbers_with_rtn([1, 9, 12, 697]))


class WrpCls:
    # name is optional init__(self) is fine if we don't have any constructor args
    def __init__(self, name):
        self.name = name

    # call method must be ovr written to decorate a method
    # *args, **kwargs means any argument
    def __call__(self, fn, *args, **kwargs):
        def wrp_fn(*argz, **kwargz):
            print("wrp called")
            return fn(*argz, **kwargz)
        return wrp_fn


@WrpCls("abc")
def sum_number_with_cls_decorator(numbers):
    total = sum(numbers)
    print("total iss  ", total)
    return total


sum_number_with_cls_decorator([1, 4, 3, 2, 4])
