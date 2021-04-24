#Filter out all of the empty strings from the list below

#Output: ['Argentina', 'San Diego', 'Boston', 'New York']

places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

new_places = list(filter(lambda place: True if place[0].lower() == " " else False, places))

print(new_places)

#Write an anonymous function that sorts this list by the last name...
#Hint: Use the ".sort()" method and access the key"

#Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']








#Convert the list below from Celsius to Farhenheit, using the map function with a lambda...

#Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]

#Write a recursion function to perform the fibonacci sequence up to the number passed in.

def fibonacci(n):
	if n <= 1:
		return n
	else:
		return(fibonacci(n-1) + fibonacci(n-2))

n = int(input('Enter a number, N, N>=2 : '))

fibo_series = []

for i in range(0,n):
	fibo_series.append(fibonacci(i))
	
print(fibo_series)
