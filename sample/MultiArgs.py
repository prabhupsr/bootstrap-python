def accept_multi_arg(*args, **key_value_args):
    print(args)
    print(type(args) == tuple)  # *args is a tuple
    print(key_value_args)
    print(type(key_value_args) == dict)


accept_multi_arg(1, 2, 3, a=5, b=2)

