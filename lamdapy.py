numbers = [1, 2, 3, 4, 5, 6]
transformed_numbers = map(lambda x: x * x, numbers)
filtered_number = filter(lambda num: num % 3 == 0, transformed_numbers)
for v in filtered_number:
    print(v)






