with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

accmin = 9999999
minp = 0
prts = []
lin = 0

for line in input_data:
	stats = line.split()
	p = [int(n) for n in stats[0][3:-2].split(',')]
	v = [int(n) for n in stats[1][3:-2].split(',')]
	a = [int(n) for n in stats[2][3:-1].split(',')]
	prts.append([p,v,a])
	if accmin > abs(a[0])+abs(a[1])+abs(a[2]):
		accmin = abs(a[0])+abs(a[1])+abs(a[2])
		minp = lin
	lin+=1
print(accmin, minp)