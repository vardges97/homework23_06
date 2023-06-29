def sorted_list(list1):
    for i in range(1, len(list1)):
        if list1[i]<list1[i-1]:
            return False
        return True


list1=[1,2,3,4,5]
list2=[2,1,5,6,8]
print(sorted_list(list1))
print(sorted_list(list2))