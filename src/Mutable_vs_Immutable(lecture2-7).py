#!/usr/bin/env python3

# test immutable vs immutable
# the behavior of list1 and list2 is a mindwarp

def append(myseq):
    myseq += (9,9,9)
    return myseq

tuple1 = (1,2,3)
list1 = [1,2,3]

print('tuple1', tuple1, id(tuple1))
print('list1', list1, id(list1))
print()

tuple2 = append(tuple1)
list2 = append(list1)

print('tuple1', tuple1, id(tuple1))
print('tuple2', tuple2, id(tuple2))
print()

print('list1', list1, id(list1))
print('list2', list2, id(list2))
print()
