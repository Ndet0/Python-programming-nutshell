list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print(list1 is list2)  # False because they are different objects in memory
print(list1 is list3)  # True because both refer to the same object in memory
print(list1 is not list2)  # True because they are different objects in memory