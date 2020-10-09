# conditionals.py
# Demonstration of if/else statements

def ifelse():
    x = -1
    if x > 1: # If x is greater than 1
        print('x is greater than 1')
    elif x < 1: # If x is less than 1
        print('x is less than 1')
    else: # If x is equal to 1
        print('x is equal to 1')

def ifelse2():
    a = 1
    b = 2
    if a == 1 and b == 2:
        print('a is 1 and b is 2')
    if a == 1 or b == 0:
        print('a is 1 or b is 0')
    if not a == 0:
        print('a is not 0')
    if a != 1: # != means 'not equals'
        print('a is not 1')
    if not a != 1:
        print('a is 1')
    if not (a == 1 and b == 0):
        print('a is not 1 or b is not 0')
    if (a == 1 and b == 0) or (a == 1 and b == 2):
        print('a is 1 and b is 0, or a is 1 and b is 2')


if __name__ == '__main__':
    ifelse()
    # ifelse2()
