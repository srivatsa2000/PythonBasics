inputString = ""
hasCarStartedAlready = False

while True:
    command = input(">").lower()
    if command == "start":
        if hasCarStartedAlready:
            print('Car has already started !. What are you doing ? ')
        elif not hasCarStartedAlready:
            print('Starting the car')
            hasCarStartedAlready = True
    elif command == "stop":
        if hasCarStartedAlready:
            print('Stopping the car')
            hasCarStartedAlready = False
        elif not hasCarStartedAlready:
            print('Car is already Stopped. What are you doing ? ')
    elif command == "quit":
        break
    elif command == "help":
        print('help !! ')
    else:
        print("I did not understand what you mean ")


