# demonstrate hashtable usage

# TODO: create a hashtable all at once
items1 = dict({"Key1":1, "Key2":2, "Key3":"three"})
print(items1)

# TODO: create a hashtable progressively
items2 = {}
items2["Key10"] = 10
items2["Key20"] = 20
items2["Key30"] = 30
print(items2)

# TODO: try to access a nonexistent key
#print(items2["Key2"])

# TODO: replace an item
items2["Key20"] = "Two"
print(items2)

# TODO: iterate the keys and values in the dictionary
for key, value in items2.items():
    print("Key is : ", key, " It's value is : ", value)