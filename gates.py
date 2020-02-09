gates  = int(input())

planeNum = int(input())

planes = []

gateFree = []

count = 0

for i in range(planeNum):
	tmp = int(input())
	planes.append(tmp)
for x in range(gates):
	gateFree.append(1)

for y in planes:
	if y-1 <=len(planes):
		if gateFree[y-1] == 1:
			count += 1
			gateFree[y-1] = -1
		else:
			pass

print(count)
	

