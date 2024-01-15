thislist = ["apple", "banana", "cherry", "mango"]
print(thislist)

thislist.insert(1, "orange")
print(thislist)

rlist = reversed(thislist)
print(rlist)

for x in rlist:
  print(x)
