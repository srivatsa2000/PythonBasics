x = int(input('x>'))
y = int(input('y>'))
z = int(input('z>'))
n = int(input('total>'))

possibles_values=[]

for x_value in range(0, x+1):
    for y_value in range(0, y+1):
        for z_value in range(0, z+1):
            if not (x_value+y_value+z_value) == n:
                possibles_values.append([x_value, y_value, z_value])
print(possibles_values)


