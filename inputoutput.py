# inputoutput.py
# Demonstration of I/O

def userinput():
    # Reads user input and echoes it back
    x = input('Input something: ')
    print(x)

def fileread():
    filename = 'inputfile.txt'
    f = open(filename, 'r') # open file with name=filename for reading only
    x = f.read()
    print(x)
    f.close()

def fileread_singleline():
    filename = 'inputfile.txt'
    with open(filename, 'r') as f:
        x = f.readline()
        print(x)
        y = f.readline()
        print(y)

def fileread_multilines():
    filename = 'inputfile.txt'
    with open(filename, 'r') as f:
        x = f.readlines() # Returns a list of strings, where each string is a line in the file
        print(x)
        for line in x:
            print(line)

output = """
Hello, world!!

Software team is best team
"""

def filewrite():
    filename = 'outputfile.txt'
    with open(filename, 'w') as f:
        f.write(output)
        f.write('asdf')


if __name__ == '__main__':
    userinput()
    # fileread()
    # fileread_singleline()
    # fileread_multilines()
    # filewrite()
