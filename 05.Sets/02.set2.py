# we have to find common elements in three sorted lists using sets
ar1 = [1,5,10,20,40,80]
ar2 = [6,7,20,80, 100]
ar3 = [3,4,15,20,30,70,80, 120]

t1 = set(ar1)
t2 = set(ar2)
t3 = set(ar3)


s1 = t1.intersection(t2)
s1 = s1.intersection(t3)
print(s1)
final_list = list(s1)
print(final_list)