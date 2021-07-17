from ListManager import ListManager

def test1():
    mgr = ListManager()
    list = [1,2,3,4]
    assert mgr.filterList(list) == [2,4]

