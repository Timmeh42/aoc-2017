import time
st = time.time()

ps = 0
s=0

for i in range(1, 50000000):
	ps = (ps+344)%i+1
	if ps == 1:
		s=i
print(s)

et = time.time()
print(et-st)