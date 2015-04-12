
divisors=[]
for i in range(1,21):
	divisors.append(i)

for i in divisors:
	m=divisors[:divisors.index(i)]
	for x in m:
		if i%x == 0:
			divisors.remove(x)

number=1
for i in divisors:
	number=number*i
print number
