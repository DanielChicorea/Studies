# GENERATOR EXPRESSION, ITERABLES E ITERATORS EM PYTHON

import sys

iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable)

generator = (n for n in range(100000))
lista = [n for n in range(100000)]

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))

print(next(generator))
print(next(generator))
print(next(generator))

# for n in generator:
#   print(n)





