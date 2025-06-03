d = {
    "a" : 23,
    "b" : 34,
    "c" : 56,
    0 : "Ram"
}
print(d)
print(d["a"])
print(d.items())
print(d.keys())
print(d.values())
d.update({"a":"Shera", "Rama" : 99})
print(d)
print(d.get("Shivika"))   #gives none if not exist
# print(d["shivika"])         #gives error

print(d.get("Rama"))

d.pop('a')   #removes givenkey  and value

print(d)
d.popitem()   #removes last inserted item 

print(d)