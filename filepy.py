filelines = open("abc.txt").read()

linesList = filelines.split('\n')

print(len(linesList))
print(linesList.count("ada"))
print(linesList)

with open("abc.txt", mode="r") as fileee:
    lns = fileee.readlines()
    for pos, val in enumerate(lns):
        print(pos)
        print(val)



