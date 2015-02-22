import csv

eighty_one = []
top_twenty = {}

with open ('rock.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if row['Release Year'] == '1981':
			eighty_one.append(1)
		top_twenty[row['Song Clean']] = int(row['PlayCount'])

print 'There were %s songs released in 1981.' % sum(eighty_one)
print 'The top 20 songs by playcount are:'
for i in sorted(top_twenty, key=top_twenty.__getitem__, reverse=True)[:20]: 
	print i


