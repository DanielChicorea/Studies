# TRY EXCEPT ELSE FINALLY
# FINALLY SEMPRE SERÁ EXECUTADO

try:
  print(1)
  8 / 0

except ZeroDivisionError:
  print('DIVIDIU ZERO')

else:
  print('CONCLUIDO!')

finally:
  print(2)

