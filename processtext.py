import string

text = []				
for i in open('data.txt'):
	for char in string.punctuation:	#replace all punctuation by " " 
		i = i.replace(char," ")	
	text.append(i)			#save line in paper into text

data = []
ini1 = 0
for i in text:
	i = i.split()			#split text by " "
	data.extend(i)

print(data)
