# ṣets is also a container for storing multiple values in a variable
#  it is enclosed in { }

#  Sets are unordered: they can be printed in different order
# immutable: can't update existing values but can add or remove items, unindexed, duplicates are not allowed, any datatype, mix of different data types

names = {"chandler", "joey", "monica", "ross"}

print(len(names))
print(type(names))

# accessong items in sets
for i in names:
    print(i)

# add element in set
names.add("rachel")
names.add("ross")
print(names)

# add another sequence in a set
names_list = ["harvey", "louis"]
names.update(names_list)
print(names)

# removing element from a set
# names.remove("louis")
names.discard("louis") #this function will not throw an error if the value is not present in the set.
print(names)

#  Union function to add two sets
s1 = {'c', 'g', 'd'}
s2 = {'d', 'w', 'q'}
s3 = s1.union(s2)
print(s3)

# s1.update(s2)
# print(s1).

# keep only duplicated
s1.intersection_update(s2)
print(s1)

# keep all values except duplicated
s1.symmetric_difference_update(s2)
print(s1)