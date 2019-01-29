def isListOfInts(ele):
    if(type(ele) is not list):
        raise ValueError(str(ele) + " - arg not of <list> type")
    else:
        if len(ele) is 0:
            return True
        else:
            flag = 1
            for i in ele:
                if(type(i) is not int):
                    flag = 0
            if (flag == 1):
                return True
            else:
                return False


def testList(a):
    print(isListOfInts(a))

testList([])
testList([1])
testList([1, 2])
testList([0])
testList(['1'])
testList([1, 'a'])
testList(['a', 1])
testList([1, 1.])
testList([1., 1.])
testList((1, 2))