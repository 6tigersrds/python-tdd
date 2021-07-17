

class ListManager:

    def include(self, x):
        return (x % 2 == 0)


    def filterList(self, somelist):
        newList = []
        newList[:] = [x for x in somelist if self.include(x)]
        return newList
