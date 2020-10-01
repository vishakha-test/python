# This programs tells you if the number entered by user is even or odd.

print('Even & Odd Game') # Prints the name of game at top
while True: #This loop runs infintly 
    num = int(input('enter your number: ')) # gets input from user and converts in into number
    rem = num%2 # calculates the remender by using modulo operator
    if rem == 0: # if condition to check is remender is zero and prints EVEN if true
        print('THIS IS EVEN')
    else: # this is excuted if the number is even
        print('THIS IS ODD')

