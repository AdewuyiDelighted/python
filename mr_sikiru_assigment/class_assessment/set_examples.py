my_set = {1,3,5,3,"ope",4,"ope"}
print(my_set)
#to convert set to immutable use the method frozenset


#super_set
#subset

set1 = set(range(1,21))
set2 = {1,4,3,5}
print(set1.issuperset(set2))
print(set1.issubset(set2))

#union print number that exist in both set
print(set1 | set2)
#0r

print(set1.union(set2))
#intersection what you can see in both set
print(set1 & set2)
#or
print(set1.intersection(set2))
#difference print out the number that is not in the set you are subtracting from
print(set1 - set2)
#0r
print(set2.difference(set1))

#symetric difference bring out what is not in both set
print(set1.symmetric_difference(set2))
