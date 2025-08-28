# empty list
my_list = []

#  Appending elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# insert 15 at index 1
my_list.insert(1, 15)

# extend the list with multiple elements
my_list.extend([50, 60, 70])

# 5. Remove the last element
my_list.pop()

# sorting the list    
my_list.sort()

#printing index of element 30
index_of_30 = my_list.index(30)
print("The index of 30 is:", index_of_30)

# Print final list to verify
print("Final my_list:", my_list)
