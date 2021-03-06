# Homework Assignment #4: Lists

"""
Create a global variable called myUniqueList.
It should be an empty list to start.

Next, create a function that allows you to add things to that list.
Anything that's passed to this function should get added to myUniqueList,
unless its value already exists in myUniqueList.
If the value doesn't exist already,
it should be added and the function should return True.
If the value does exist, it should not be added,
and the function should return False;

Finally, add some code below your function that tests it out.
It should add a few different elements,
showcasing the different scenarios,
and then finally it should print the value of myUniqueList to show that it worked.
Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers.
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""
#Creating myUniqueList variable, which is an empty list at start.
myUniqueList = []
#Creating myLeftovers variable, which is an empty list at start and repetitive values get added into it.
myLeftovers = []

# function
def List_Element_Add(a):
    #existing element gets appended to myLeftovers
    if a in myUniqueList:
        bool = False
        myLeftovers.append(a)
        #function now returns false
        return bool
    #new element, not a part of myUniqueList gets added to myUniqueList
    elif a not in myUniqueList:
        myUniqueList.append(a)
        #function now returns true
        bool = True
        return bool

#function calls
# new element gets appended to
q = List_Element_Add("Hello")
# new element
r = List_Element_Add(0)
# new element
s = List_Element_Add(1)
# same element repetition
t = List_Element_Add(1)

# prints myUniqueList
print(myUniqueList, "Is my Unique List")
# prints myLeftovers
print(myLeftovers, "Is my Leftovers")
