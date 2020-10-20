def find_max(list_of_numbers):
    highest_number = 0
    for number in list_of_numbers:
        if number > highest_number:
            highest_number = number
    return highest_number