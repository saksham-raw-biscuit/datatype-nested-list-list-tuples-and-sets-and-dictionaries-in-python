

## method to find a item index from the list.
# index refers to the position of the item

list_1 = ['Food','Color','Address','Galaxy','Technology']
list_2 = [1,-5,-99,99,45,0]

# print(list_1.index('Technology'))


#method to add items to teh list

## we have here two method to add to the list 
# 1. append(a)
# 2. insert(a,b)

# append is to when the new item needs to be stored at the last [-1] of the list

# list_1.append("AutoMobile")
# print(list_1)
    #Output : ['Food', 'Color', 'Address', 'Galaxy', 'Technology', 'AutoMobile']

# insert can add new item to any index in the list

# list_1.insert(2,"Landscape")  # the lasdscape will br placed in the index 2
# print(list_1)
    #Output : ['Food', 'Color', 'Landscape', 'Address', 'Galaxy', 'Technology', 'AutoMobile']


##previously we used del to delete any item from the list
# but the method used is .remove(a)

##The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is useful when you know the value you want to remove from the list.

# list_1.remove("Technology")
# print(list_1)
    # Output : ['Food', 'Color', 'Landscape', 'Address', 'Galaxy', 'AutoMobile']



# .sort() to sort the list in ascending order or in alphabetical order

list_1.sort()
print(list_1)

list_1.sort(reverse=True)
print(list_1)

list_2.sort()
print(list_2)

spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()

    #output:['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
    #Because python follows the ASCII order Capital Z comes before lower a

spam.sort(key=str.lower)
print(spam)
    #Output : ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']


## reverse the whole loop:

spam.reverse()
print(spam)