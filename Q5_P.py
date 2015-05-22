divisors=[]
for i in range(2,11):
	divisors.append(i)

print divisors

to_remove=[]
for i in divisors:
	m=divisors[:divisors.index(i)]
	for x in m:
		if i%x == 0:
			to_remove.append(i)

print to_remove

for i in to_remove:
	if i in divisors:
		divisors.remove(i)

print divisors

number=1
for i in divisors:
	number=number*i
print number
