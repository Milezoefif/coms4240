# append()
L = [1, 2, 3, 4]
print("append()")
print(L)
L.append(5)
print(L)
print("\n")

# clear()
L = [1, 2, 3, 4, 5]
print("clear()")
print(L)
L.clear()
print(L)
print("\n")

# copy()
L = [1, 2, 3, 4, 5]
print("copy()")
print(L)
L2 = L.copy()
print(L2)
print("\n")

# count()
L = [1, 2, 2, 3, 2, 4, 5]
print("count()")
print(L)
print(f"There are {L.count(2)} 2's in L")
print("\n")

# extend()
L = [1, 2, 3, 4, 5]
print("extend()")
print(L)
L.extend([6, 7])
print(L)
print("\n")

# index()
L = [11, 7, 4, 41, 9]
print("index()")
print(L)
print(f"The number 41 is at index {L.index(41)}")
print("\n")

# insert()
L = [1, 3, 4, 5]
print("insert()")
print(L)
L.insert(1, 2)
print(L)
print("\n")

# pop()
L = [1, 2, 3, 4, 5]
print("pop()")
print(L)
L.pop()
print(L)
print("\n")

# remove()
L = [11, 7, 4, 41, 9]
print("remove()")
print(L)
L.remove(41)
print(L)
print("\n")

# reverse()
L = [1, 2, 3, 4, 5]
print("reverse()")
print(L)
L.reverse()
print(L)
print("\n")

# sort()
L = [4, 2, 5, 1, 3]
print("sort()")
print(L)
L.sort()
print(L)