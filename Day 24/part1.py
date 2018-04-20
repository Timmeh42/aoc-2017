import copy
with open("input.txt","r",newline="") as archive:
	input_data = archive.readlines()

parts = [[int(n) for n in l.split('/')] for l in input_data]
print(parts)
maxstr = 0
longbr = 0

def build_bridge(bridge, parts, port):
	global maxstr, longbr
	extended = False
	used = []
	for part in parts:
		if port in part and part not in bridge and part not in used:
			extended = True
			next_port = part[1 - part.index(port)]
			bridge.append(part)
			build_bridge(bridge, parts+used, next_port)
			used.append(bridge.pop())
	leng = len(bridge)
	mystr = sum([oport for opart in bridge for oport in opart])
	print(leng, mystr)
	if not extended:
		#print(bridge)
		if leng >= longbr:
			longbr = leng
			maxstr = max(maxstr, mystr)
build_bridge([], parts, 0)
print(longbr, maxstr)