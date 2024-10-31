# TRY, EXCEPT, ELSE e FINALLY (PARTE 2)

# a = 18
# b = 0
# c = a / b
  
try: 
  a = 18
  b = 0
  print('Testando..., 1')
  print('Linha 1'[1000])
  
  c = a / b   
  print('Testando..., 2')

except ZeroDivisionError:
  print('Dividiu por Zero!')

except TypeError:
  print('Tipagem Errada!')

except(TypeError, IndexError) as error:
  print('TypeError + IndexError')
  print('Name: ', error.__class__.__name__)

except Exception:
  print('ERROR 404!')