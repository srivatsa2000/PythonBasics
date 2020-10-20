secretNumber = 7
counter = 0

while counter < 3:
    inputvalue = int(input('Guess the Number : '))
    if counter > 2:
        print('You have exceeded the number of try')
        break
    elif inputvalue == secretNumber:
        print('You have guessed it ! ')
        break
    counter += 1

print('Closing Problem')