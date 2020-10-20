temperature = 30

if temperature > 30:
    print("It's a hot day !")
elif temperature < 20:
    print("It's a cold day ! ")
else:
    print("It's a good day")

# Learning

name = input(' What is your name ? ')

if len(name) < 3:
    print('Name must be at least 3 char long ')
elif len(name) > 50:
    print('Name is way too long !')
else:
    print('All looks good ! ')
