readfile = open('./ml-100k/u.user', 'r')

for line in readfile:
	(id, age, gender, occupation, zipcode) = line.split('|')
	if age == '21' and gender == 'F' and occupation == 'student':
		print (id, age, gender, occupation, zipcode)
