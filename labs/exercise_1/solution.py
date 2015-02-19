sublist = []

def divider(bucket):
	for n in bucket:
		if n % 33 == 0:
			sublist.append(n)
		else:
			exit

divider([33, 45, 66])

print sublist

