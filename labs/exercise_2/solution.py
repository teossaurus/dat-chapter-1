fibo = [1]
evens = []

for n in fibo:
#adds n to its predecessor in the list to get i
	i = n + fibo[fibo.index(n)-1]
#populates fibo with i up to four million so the loop can continue
	if i <= 4000000:
		fibo.append(i)
#populates evens with the even numbers in the Fibonacci sequence
	if i % 2 == 0 and i <= 4000000:
		evens.append(i)

print evens
print sum(evens)




