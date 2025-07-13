list = []

for num in range(1, 11):
    list.append(num**2)
print(list)
     
# COMPREHENSION OF ABOVE FORMULA

squares = [num**2 for num in range(1,11)]
print(squares)
