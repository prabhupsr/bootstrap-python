def find007(sequence, targetSeq):
    pos = 0
    for val in sequence:
        if val == targetSeq[pos]:
            print(targetSeq[pos])
            pos = pos + 1
            if pos == len(targetSeq):
                return True

    return pos == len(targetSeq) - 1


print(find007([1, 2, 3, 0, 0, 4, 3, 2, 7, 5], [0, 0, 7]))
