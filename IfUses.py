housePrice = 1000
buyerHasGoodCredit = True
downPayment = 0

if buyerHasGoodCredit:
    downPayment = housePrice * 0.1
else:
    downPayment = housePrice * 0.2
print(f'Down payment value is {downPayment}')
