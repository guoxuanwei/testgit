import operator


def assertEqual(list1, list2):
    list1.sort()
    list2.sort()
    return operator.eq(list1, list2)
    # return list1 == list2


if __name__ == '__main__':
    a = ['海南麒麟瓜5斤装']
    b = ['海南麒麟瓜5斤装']
    print(assertEqual(a, b))
