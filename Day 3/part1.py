import math
input_data = 368078

def ringmax(ring):
	return 1+(ring)*(ring+1)*4

def getring(numb):
	return math.ceil(math.sqrt(numb))//2

def getringpos(numb):
	ring = getring(numb)
	n = numb - ring - ringmax(ring-1)
	n = n%(ring*2)
	n = ring - math.fabs(ring - n)
	return int(n)

steps = getring(input_data) + getringpos(input_data)
print(steps)


################################
end = input("")