x = int(input())
y = int(input())

y_hun = y//100
y_ten = (y-100*y_hun)//10
y_one = y-100*y_hun-10*y_ten

print(x*y_one)
print(x*y_ten)
print(x*y_hun)
print(x*y)