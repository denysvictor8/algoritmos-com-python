import numpy as np
import math

'''
f(x) = (28cos( (x−6)/4) + 20)
intervalo [-12, 12]
'''

def f(x):
  i = (x-6)/4
  return 28 * math.cos(i) + 20

passo = 0.5
# gera um inteiro aleatorio
x0 = np.random.randint(-12, 12)
y0 = f(x0)
print("valor aleatório do X e de: ", x0)

x1 = ( x0 + passo )
x2 = ( x0 - passo )
y1 = f(x1)
y2 = f(x2)
#------------------------------------ os passos ------------------------------------
if ( y1 > y0 ):
  x0 = x1
  y0 = y1
  passo  *= 1

elif ( y2 > y0 ):
  x0 = x2
  y0 = y2
  passo *= -1
#------------------------------------ achando o maximo ------------------------------------
if ( y1 < y0 and y2 < y0):
  print("o valor maximo e de: ", x0)

else:
  xx = x0; # varivel x linha
  while ( xx > -12 and xx < 12 ):
    xx += passo
    yy = f(xx)
    if ( yy > y0 ):
      x0 = xx
      y0 = yy
    else:
      break;
#-------------------------------------
print("o valor maximo e de: ", x0)
