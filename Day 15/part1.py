A = 679
B = 771
Alist = []
Blist = []

def gen_A():
	global A
	A = (A*16807)%2147483647
	while A%4 != 0:
		A = (A*16807)%2147483647
	return A

def gen_B():
	global B
	B = (B*48271)%2147483647
	while B%8 != 0:
		B = (B*48271)%2147483647
	return B

count = 0
for i in range(5000000):
	gen_A()
	strA = str(bin(A)[2:].zfill(32))
	Alist.append(strA[-16:])

for i in range(5000000):
	gen_B()
	strB = str(bin(B)[2:].zfill(32))
	Blist.append(strB[-16:])

for i in range(5000000):
	if Alist[i] == Blist[i]:
		count+=1
print(count)