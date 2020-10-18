weight = int(input('Enter your weight : '))
unitType = input('(L)bs or (K)g : ')
output = 0

if unitType == 'L' or unitType == 'l':
    output = weight * 0.453592
    print(f'You are {output} Kgs')
elif unitType == 'K' or unitType == 'k':
    output = weight * 2.20462
    print(f'You are {output} lbs')
else:
    print('Unable to understand the Unit Type')
