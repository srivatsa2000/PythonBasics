char = input()

output = ""

for each_letter in char:
    if each_letter == 'G':
        output += 'C'
    elif each_letter == 'C':
        output += 'G'
    elif each_letter == 'T':
        output += 'A'
    else:
        output += 'U'
print(output)
