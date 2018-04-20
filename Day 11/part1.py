with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

instr = input_data[0].split(",")

n = 0
s = 0
ne = 0
nw = 0
se = 0
sw = 0

x=0
y=0
z=0

for step in instr:
	if step == "n":
		n += 1
		y+=1
		z-=1
	if step == "s":
		s += 1
		y-=1
		z+-1
	if step == "ne":
		ne += 1
		x+=1
		z-=1
	if step == "sw":
		sw += 1
		x-=1
		z+=1
	if step == "nw":
		nw += 1
		x-=1
		y+=1
	if step == "se":
		se += 1
		x+=1
		y-=1

print("N", n)
print("S", s)
print("NE", ne)
print("NW", nw)
print("SE", se)
print("SW", sw)

print("N", n-s)
print("NW", nw-se)
print("NE", ne-sw)


print((abs(x) + abs(y) + abs(z))/2)