def ten_multiple_numbers_provider_lazy():
    list_number = [x for x in range(1, 100) if x % 2 == 0]
    print(list_number)
    for pos, number in enumerate(list_number):
        if number % 10 == 0:
            yield pos, number
            print("before value yielded")
        print("processing number in pos ", pos + 1)


numbers_provider_lazy = ten_multiple_numbers_provider_lazy()
print(numbers_provider_lazy)  # not computed yet

print(next(numbers_provider_lazy))

print(next(numbers_provider_lazy))

# first 4 elements taken by this loop
# for i, (y, n) in enumerate(numbers_provider_lazy):
#     print(i, y, n)
#     if i == 1:
#         break
# print("next element 50 is taken using next of generator ")
# print("************** ")
# print(next(numbers_provider_lazy))
# print("************** ")
#
# # remaining are taken by this
# lazy_number_list_fetched_all = [v for v in numbers_provider_lazy]
# print(lazy_number_list_fetched_all)
