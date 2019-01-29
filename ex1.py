def ruler(num):
    i = 1
    list1 = ""
    list2 = " "
    while(i<=num):
        list1 += str(i % 10)
        i += 1
        if (i % 10 == 0):
            list2 += str(int(i / 10))
        else:
            list2 += " "

    print(list2)
    print(list1)

num = int(raw_input())
ruler(num)
