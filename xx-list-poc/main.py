
def remove(x):
    # include only if even number....
    return (x % 5 == 0)


def filterList(somelist):
    newList = [x for x in somelist if not remove(x)]
    return newList

list = [5,10,2,30,18,274,232,15]
print(list)
print(filterList(list))

