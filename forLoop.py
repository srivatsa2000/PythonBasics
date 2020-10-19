xcordinateMax = 3
yCordinateMax = 5

for item in range(xcordinateMax):
    for yitem in range(yCordinateMax):
        print(item, yitem)

numbers = [5, 2, 5, 2, 2]
print(numbers[0])

for num in range(len(numbers)):
    print('*' * numbers[num])
