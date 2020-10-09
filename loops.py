# loops.py
# Demonstration of for and while loops

def forloop():
    x = 10
    for i in range(0, x): # 0, 1, 2, .., x-1
        print(i)

def whileloop():
    i = 0
    x = 10
    while i < x:
        print(i)
        i = i + 1 # i += 1


if __name__ == '__main__':
    forloop()
    # whileloop()
