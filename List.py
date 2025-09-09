#   1)Using List() Construtor
a  = list((1,2,3,"Kausar"))
print(a)
b = list("KAUSAR")
print(b)


#    2)Creating List with Repeated Elements
c = [2]*6
print(c)



#    3)Accessing List Elements
d = [1,2,3,'kausar',True]
print(d[0])
print(d[4])



#   4)Adding Elements into List
#   append(),   extend(),    insert(), clear()
e = [0]
e.append(1)
print("after append:",e)
e.extend(['kausar',4,60])
print("after extend:",e)
e.insert(0,70)
print("after insert:",e)
e.clear()
print("after clear:",e)


#    5)Updating Elements into List
f  = [0,1]
f[1] = 50
print("after update:",f)



#   6)Removing Elements from List
#   remove(),   pop(),    del() 
val = [2,6,4,1,5]
val.remove(4)
print("after remove:",val)
popped_val = val.pop(1)
print("Popped Value:", popped_val)
print("after popped:",val)
del val[0]
print("after del:",val)



#   7)Iterating Over Lists
items = ["bread", "milk", "water"]
for a in items:
    print(a)


#    8)List Comprehension
cubes = [x**3 for x in range(0,6)]
print("after cube:",cubes)


def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            return -1
arr = [2,4,6,8,0,10]
target = 3
result =  linear_search(arr,target)
if result != -1:
    print(f"the value are found in list at index {result}")
else:
    print("by linear_search value not found")        



