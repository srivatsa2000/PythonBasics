housePrice = 1000
buyerHasGoodCredit = False
highIncome = False
downPayment = 0

if buyerHasGoodCredit:
    downPayment = housePrice * 0.1
else:
    downPayment = housePrice * 0.2
print(f'Down payment value is {downPayment}')

if buyerHasGoodCredit and highIncome:
    print('Both Should be True')

if buyerHasGoodCredit or highIncome:
    print('Or condition')

# Negating the values

if not buyerHasGoodCredit:
    print('No loan')
