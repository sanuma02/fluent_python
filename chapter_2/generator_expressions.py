import array

symbols = '$§%&/('
tup = tuple(ord(symbol) for symbol in symbols)
print(tup)

# () needed
j = array.array('I', (ord(symbol) for symbol in symbols))
print(j)

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

# generator list with all combination is never built
for x in tuple('{} {}'.format(c,s) for c in colors for s in sizes):
    print(x)