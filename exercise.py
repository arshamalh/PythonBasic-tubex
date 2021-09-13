import random

SampleList = [random.randint(1, 9) for _ in range(1, 20)] # It will have at least twice of any number
def DuplicateRemover(GivenList):
    for x in GivenList:
        detect = GivenList.count(x)
        if detect > 1:
            i = 0
            while i < detect - 1:
                GivenList.remove(x)
                i += 1
    return GivenList
print(f'Result is :{DuplicateRemover(SampleList)}')
