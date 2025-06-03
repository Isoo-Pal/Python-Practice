s = {2,4,3,5,4,1,1,6}
s2 = set()   #empty set

print(type(s))
print(type(s2))
print(s)

s.add(9)
print(s)

s.update([0,7])   #Adds multiple elements from any iterable (list, tuple, etc.)
print(s)

s.remove(1)   #removes all 1's
print(s)

s.discard(10)    # No error even if 10 is not in the set
s.pop()      #removes any random element

print(s)
print(len(s))

