from collections import OrderedDict, namedtuple

num_dict = {1: "a", 2: "b", 3: "c"}

# dict.items - keys
# dict.values - values
# dict.items - k,v
# dict not ordered
# Ordered dict is ordered
# Default Dict with default value

print(dict({"a": 1}))

for k, v in num_dict.items():
    print(k, v)


def dict_m():
    print("----------dict_m--------------------")
    dict_samp: OrderedDict = dict({1: "a", 2: "b", 3: "c"})
    print(dict_samp)
    # pop item uses LIFO
    print(dict_samp.popitem())
    print(dict_samp.pop(1))
    print(dict_samp.get(9, ""))
    print(dict_samp.get(10) is None)
    try:
        print("pop called for unavailable key", dict_samp.pop(10))
    except KeyError as err:
        print("Key Error - ", err)

    dict_samp.update(abc=10)

    print(dict_samp)
    print("----------dict_m--------------------")

    generated_dict = {abs(num): num ** 2 for num in range(10, -30, -5)}
    print("generated_dict -- ", generated_dict)


dict_m()
print(num_dict)


def named_tuple():
    Student = namedtuple("student", ['name', 'age'])
    print("tuple - ", Student)
    print(Student("mani", "30"))
    tuple_with_values = Student(name='prabhu', age=20)
    print(tuple_with_values)
    print(tuple_with_values.name)
    print(tuple_with_values[1])
    print(tuple_with_values._fields)
    name, age = tuple_with_values
    print(name, age)


named_tuple()
