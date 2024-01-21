total = 0
for i in range(5):
	for j in range(3):
		if i+j== 5:
			total  += 1+ j
		else:
			total -= 1 - j

counter = 0
while counter < 5: 
	if total < 13:
		total += 1
	elif total > 13:
		total -= 1 
	else:
		counter += 2

# to print the key number
print("The Key is ",total)