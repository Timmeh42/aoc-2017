import time
h = 0

st = time.time()

for b in range(108100, 125100+1, 17):
	f = 1
	for d in range(2, b//2+1):
		for e in range(2, b//d+1):
			if d * e  == b:
				f = 0
				h+=1
				break
		if f == 0:
			break
et = time.time()
print(h, et-st)