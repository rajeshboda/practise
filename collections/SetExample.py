mySet = {"Java", "C", "C++", "Python......".rstrip('.'), "Python"} ## no duplicates
print(mySet)

#for it in mySet:
#    print(it)

print("Size -->", len(mySet))
mySet.add("Crazy Programming Languages")
mySet.add("But rocks!!!")

#for it in mySet:
#    print(it)

copyMySet = mySet
print(id(mySet))
print(id(copyMySet))

mySet.add("But rocks!!! again")

for it in mySet:
    print(it)


for it in copyMySet:
    print(it)

unionOfAll = mySet.union(copyMySet)
for it in unionOfAll:
    print(it)
