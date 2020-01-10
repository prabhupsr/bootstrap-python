listFromRange: list = list(range(2, 20, 2))
for pos, v in enumerate(listFromRange):
    print(pos, v)

tu: tuple = (1, 2, 3)
print("tuple is immutable {}", tu)

compVal = [(pos, x, y) for pos, x in enumerate(range(1, 10)) if x % 2 == 0 for y in [1, 15, 3]]
print(compVal)


def changecase(word):
    if word.islower():
        return word.upper()
    else:
        return word.lower()


s = ''
caseChangeVal = [changecase(val) for val in 'aBcDeFgH']

for char in 'aBcDeFgH':
    s = s.__add__(changecase(char))

print(s)
