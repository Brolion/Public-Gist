bitcoin = input('What is Bitcoin price today? ')
cash = input('How much $ do you have? ')
res = f'You can buy {(float(cash)/float(bitcoin))} BTC'
print(res)
