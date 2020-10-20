numbers = [12, 13, 15, 16, 12, 34, 45, 78]
unique = []


for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)
