
## This python file is based on the Sweigart's Automate the Boring Stuff with Python

list_1 = [['name',50,'John','NewYork'],['public',20,'Hero']]

list_2 = ["rat",'bat','hat']

# The rules for indexing and slicing the list is the same as in the string.

#list indexing

# print(list_1[0][2])  ## To choose the item from list within the list "Nested List"
    #output = John

# print(list_1[1])
    #output = ['name',50,'John','NewYork']

# print(list_2[1])
    # output = 'rat

## Slicing the list

# print(list_1[:])  #select all the items of the list list_1

# print(list_1[0][0:]) # [0] selects the first item of the list_1, which is also a list so [0:] selects all the items within it.

##length of the list

# print(len(list_1))
# print(len(list_2))

## Changing the item of the list

    # using indexing

# list_1[0][0] = "Name"  # changes the first item's first item from list_1
# print(list_1)

# list_2[2] = "hand"
# print(list_2)


# new_list = list_2 + ["sand","hand","land"]
# print(new_list)
    # output = ['rat', 'bat', 'hat', 'sand', 'hand', 'land']

# new_list = list_2 *2
# print(new_list)
    #output = ['rat', 'bat', 'hat', 'rat', 'bat', 'hat']

# new_list = [1,2,3,4,5,6,7] + list_1
# print(new_list)
    #output = [1, 2, 3, 4, 5, 6, 7, ['name', 50, 'John', 'NewYork'], ['public', 20, 'Hero']]

# new_list = list_1 + [1,2,3,4,5,6,7]
# print(new_list)
    #output = [['name', 50, 'John', 'NewYork'], ['public', 20, 'Hero'], 1, 2, 3, 4, 5, 6, 7]


## removing the items from list 

# del list_2[1]
# print(list_2)



# petNames = []
# while True:
#     print('Enter the name of cat ' + str(len(catNames) + 1) +
#       ' (Or enter nothing to stop.):')
#     name = input()
#     if name == '':
#         break
#     # catNames = petNames + [name]  # list concatenation
#     petNames.append(name)           #list append
# print('The cat names are:')
# for name in catNames:
#     print('  ' + name)

# customerNames = []

# while True:

#     name = input("Enter the pet name" + str(len(customerNames) +1) + ":")

#     if not name:
#         break
    
#     customerNames.append(name)

# print("The pet names are :")
# for item in customerNames:
#     # print(item)               # To print name in every new line
#     print(item,end = " | ")     # To print name in single line with a pipe in between


# copying the items of the list
# list_3 = [item for item in list_2]
# print(list_3)

# for i in range(len(list_2)):     # To return every items from list_2

#     print("Index " + str(i) +" of the list_2 is : " + list_2[i])

