#zip lists
#merge elements if number of elements in both the list are equal and if not,  zip will stop based on shortest one.
#if you want merge based on longest one, you can use below cycle or itertools.zip_longest 
list1=["a", "b","c"]
list2=["A","B","C"]

list1.append("f")

#what does lst[:] means, https://stackoverflow.com/questions/32448414/what-does-colon-at-assignment-for-list-do-in-python/32448477 
print(list1[:])

# what does the list.revers() do? https://www.programiz.com/python-programming/methods/list/reverse 

#List - append, extend and merge another or Add another list or tuple at specified index - https://note.nkmk.me/en/python-list-append-extend-insert/

print(list(zip(list1, list2)))

#It is possible to use the cycle() function from itertools to repeat values from the shorter list. This will allow zip() to iterate over all the elements from the longer list. 
# In this example, cycle() is used to repeat values from list_one and the resulting merged list will now contain all values from list_two.

from itertools import cycle
list_one = ['Joe', 'Mark', 'Jane']
list_two = [ 100, 34, 87, 23, 65 ]
merged2 = zip(cycle(list_one), list_two) #https://www.codespeedy.com/itertools-cycle-in-python/.. cycle is non-stop loop and it should break with some kind of exit statement. Here zip automatically stops the loop when it ends the list
print(list(merged2))
#[('Joe', 100), ('Mark', 34), ('Jane', 87), ('Joe', 23), ('Mark', 65)]


lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']] 
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]

def merge(list1, list2):
    return [(fromlist1 + [lst2[i][-1]]) for i, fromlist1 in enumerate(lst1)]
 
print(merge(lst1,lst2))

dict1={"b","c"}
dict1.add("a")
print(dict1)


