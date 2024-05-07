# enumerate function is a built-in function used insted of using the for loop to obtain the index of the item in the list

list_1 = ["Pen","Book","Copy","Bag","College"]

for a,b in enumerate(list_1):

    print(str(a) + ":" + b)

# a is the index of each item of the list 0,1,2,3,4
# b is the item of the list.

    # Output :
        # 0:Pen
        # 1:Book
        # 2:Copy
        # 3:Bag
        # 4:College