import os

os.system('clear')

age = 41.4
age2 = '41'

print(type(age))

names = ['bob', 'john', 'alice']
print(names[2])

fav_pizza = {
	"john": "Pepperoni",
	"bob": "Mushroom",
	'alice': 'Cheese',

}

print(fav_pizza)
print(fav_pizza['john'])

to_old = True
if to_old:
	print('go away, old guy')
