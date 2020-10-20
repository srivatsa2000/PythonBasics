inputValue = input("Type some Digits > ")
numbersToTextMapping = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

valuesToPrint = ""

for digits in inputValue:
    valuesToPrint += numbersToTextMapping.get(digits, "!") + " "
print(valuesToPrint)
