#Methods in Set

collection = set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add("hello")
collection.add((1,2,3)) # adds the whole tuple as a single element
#collection.add([1,2,3]) # error because list is mutable


collection.remove(1)
#collection.remove(3) #error
print(collection)