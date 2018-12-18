tup1 = ('Java', 'AI', "MachineLanguage", "Springs", 2018);
tup2 = (1, 2, 3, 4, 5);
tup3 = "a", "e", "i", "o", "u";

for it in tup1, tup2, tup3:
    print(it)

tup_all = tup1 + tup2 + tup3

print(tup_all)

print(5 in tup2)

# Convert list to tuple

mylist = [1, 2, 3, 4]
tupleFromList = tuple(mylist)

mylist.append("four")
print(mylist)
print(tupleFromList)
print(id(mylist))
print(id(tupleFromList))
