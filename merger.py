def merger(ls1,ls2):
    result= ls1 + ls2
    for i in range(len(result)):
        for j in range(len(result)-1):
            if result[j]>result[j+1]:
                result[j],result[j+1]= result[j+1],result[j]
    return result

list1=[1,2,4,3,5]
list2=[4,5,8,6,7]
new_list = merger(list1,list2)
print(new_list)