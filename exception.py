try:
    age = int(input("Enter your age : "))
    print(age)
except ValueError:
    print('Invalid Value')
except ZeroDivisionError:
    print('You can not devide by Zero')
