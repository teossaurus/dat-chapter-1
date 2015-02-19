fibo = [1]

for n in fibo if not n => 4000000:
	i = n + fibo[fibo.index(n)-1]
	if i <= 4000000:
		fibo.append(i)

print [i for i in fibo if not i % 2]
print sum(i for i in fibo if not i % 2)
