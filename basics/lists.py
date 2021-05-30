l1 = [1, 2, 3]
l2 = [10, 20, 30]

l2.extend(l1)
print(l2)  # [10,20,30,1,2,3]

l2.sort()
print(l2)  # [1,2,3,10,20,30]

l2.sort(reverse=True)
print(l2)  # [30,20,10,3,2,1]
