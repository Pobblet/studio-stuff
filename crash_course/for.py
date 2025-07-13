pizzas = ["hawian", "pepperoni", "veggie"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.") 

for pizza in pizzas:
    x = len(pizzas)
    print("there are " + str (x) + " pizzas on the menu.")

digits = [1,2,3,4,5,6,7,8,9,0]

print(min(digits))
print(max(digits))
print(sum(digits))

list = []

for num in range(1, 11):
    list.append(num)
print(list)

squares = [value**2 for value in range(1,11)]
print(squares)

