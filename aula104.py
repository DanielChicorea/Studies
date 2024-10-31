# INTRODUÇÃO ÀS GENERATOR FUNCTIONS EM PYTHON
# GENERATOR = (N FOR N IN RANGE(1000000))

def generator(n = 0, maximum = 10):
  while True:
    yield n
    n += 1
    
    if n > maximum:
      return
    
gen = generator(n = 5, maximum = 10)
for n in gen:
  print(n)

