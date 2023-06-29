def is_sorted(list1):
    for i in range(1,len(list1)):
        if list1[i] < list1[i+1]:
            return False

    return True