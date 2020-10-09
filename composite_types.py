# composite_types.py
# Lists, tuples, dicts

def listdemo():
    a = []
    a = list()
    a = ['A', 'B', 'C', 'D']
    print(a)
    b = [1, 2, 3, 4, 3, 2]
    print(b)
    c = ['A', 1, 4.3, True, 'Hello']
    print(c)
    d = a[1:3]
    print(d)
    e = a[1:]
    print(e)
    f = a[:3]
    print(f)
    a.append('E')
    print(a)
    g = a + b
    print(g)
    g.pop()
    print(g)
    h = g[3]
    print(h)
    g.remove(g[3])
    print(g)

def tupledemo():
    a = ('A', 'B', 'C', 'D')
    print(a[3])
    b = a[1:]
    print(b)

def dictdemo():
    a = {}
    a = dict()
    a[4] = 123
    print(a)
    a[4] = 'abcd'
    print(a)
    a['hello'] = 'world'
    print(a)
    print(a['hello'])


if __name__ == '__main__':
    listdemo()
    # tupledemo()
    # dictdemo()
