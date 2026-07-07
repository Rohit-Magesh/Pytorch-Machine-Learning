l1 = [1,2,3]
l2 = [4,5,6]
a = 3
op = []
for i in range(len(l1)):
    op.append((l1[i]*l2[i])+a)
print(op)