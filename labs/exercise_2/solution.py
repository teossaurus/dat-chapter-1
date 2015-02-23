fibo = [1]

for n in fibo:
	i = n + fibo[fibo.index(n)-1]
	if i <= 4000000:
		fibo.append(i)

print sum(i for i in fibo if not i % 2)