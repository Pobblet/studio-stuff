pizzas = ["hawian", "pepperoni", "veggie"]

for pizza in pizzas:
    print(f"I like {pizza} pizza.") 

for pizza in pizzas:
    x = len(pizzas)
    print("there are " + str (x) + " pizzas on the menu.")

digits = [1,2,3,4,5,6,7,8,9,0]

############################################################

print(min(digits))
print(max(digits))
print(sum(digits))

############################################################

for num in range(1,21):
    print(num)

list1 = []
for num in range(1,1_000_001):
    list1.append(num)

#for num in list1:
#    print(num)
print("\n")
print(min(list1))
print(max(list1))
print(sum(list1))

#############################################################
print("\n")

for num in range(1,21,2):
    print(num)   

list2 = []

for num in range(0,31,3):
    list2.append(num)
print(list2)    


