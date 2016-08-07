list1 = [1,2,5,4,5]
list2 = list1
list1[2] = 3
print(list2 )#mutable

list3 = [1,2,5,4,5]
list4 = list3[:] #created a copy as substring of whole string

list3[2] = 3

print(list4)