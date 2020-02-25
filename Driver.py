import time
from Classes import Node, LinkedList

myList = LinkedList()
print("Here's the empty list")
print(myList)
time.sleep(2)
print("Now, let's add to it.")
myList.prepend(30)
print(myList)
time.sleep(0.7)
myList.prepend("255")
print(myList)
time.sleep(0.7)
myList.append('Hello World')
print(myList)
time.sleep(0.7)
myList.prepend(6)
print(myList)
time.sleep(0.7)
print("I'm going to remove from the head")
myList.remove_head()
print(myList)
time.sleep(0.7)
print('now, to take from the end')
myList.remove_end()
print(myList)
time.sleep(0.7)
print("Is 6 in the list?")
myList.search(6)
print(myList)
time.sleep(0.7)
print("Is 23 in the list?")
myList.search(23)
print(myList)
time.sleep(0.7)
print("Now, let's remove from the list.")
time.sleep(2)
myList.remove_distinct(6)
print(myList)
