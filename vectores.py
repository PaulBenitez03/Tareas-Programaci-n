import math
class Vector3D:
 def __init__ (self,x,y,z):
    self.x = x
    self.y = y
    self.z = z
#El nombre _add_ es util dado que ademas de servir como etiqueta para realizar la operacion, python permite activar la funcion con 
#el signo +
 def __add__ (self,other):
  return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)
#De igual forma _sub_ remplaza el nombre de la funcion por el signo -
 def __sub__ (self,other):
  return Vector3D(self.x - other.x,self.y - other.y,self.z - other.z)
 def multiply_by_scalar (self,scalar):
  return Vector3D(scalar*self.x,scalar*self.y,scalar*self.z)
 def dot_product (self,other):
  return self.x*other.x + self.y*other.y + self.z*other.z
 def cross_product (self, other):
  return Vector3D(self.y*other.z - self.z*other.y,self.x*other.z -self.z*other.x,self.x*other.y - self.y*other.x)
 def __repr__ (self):
  return '({},{},{})'.format(self.x,self.y,self.z)
 def div_scalar (self,scalar):
  return Vector3D(self.x/scalar,self.y/scalar,self.z/scalar)
 def magnitud (self):
  return math.sqrt(self.x**2 + self.y**2 + self.z**2)
 def norma (self):
  mgnt = self.magnitud()
  if mgnt == 0:
   return Vector3D(0,0,0)
  else:
   return Vector3D((self.x/mgnt),(self.y/mgnt),(self.z/mgnt))

#Agregar el angulo polar del vector
#Un metodo que encuentre los angulos con los tres ejes cordenados
class Vector2D:
 def __init__(self,x,y):
  self.x = x
  self.y = y


 def __add__(self,other):
  return Vector2D(self.x + other.x,self.y + other.y)
 def __sub__ (self,other):
  return Vector2D(self.x-other.x,self.y-other.y)
 def multiply_by_scalar (self,scalar):
  return Vector2D(self.x*scalar,self.y*scalar) 
 def dot_product (self,other):
  return self.x*other.x + self.y*other.y
 
 def div_scalar (self,scalar):
  return Vector2D(self.x/scalar ,self.y/scalar)

 def __repr__ (self):
  return '({},{})'.format(self.x,self.y)
 def magnitud (self):
  return math.sqrt(self.x**2 + self.y**2)
 def norma (self):
  mgnt = self.magnitud()
  if mgnt == 0:
   return Vector2D(0,0)
  else:
   return Vector2D((self.x/mgnt),(self.y/mgnt))

#Prueba de vectores 3D
V1 = Vector3D(1,2,2)
V2 = Vector3D(5,7,8)
V0 = Vector3D(0,0,0)
a = 2
#Suma
vs = Vector3D.__add__(V1,V2)
print(vs)
#Resta 
vr = Vector3D.__sub__(V1,V2)
print(vr)
#Producto escalar
P = Vector3D.multiply_by_scalar(V2,a)
print(P)
#Producto punto
pp = Vector3D.dot_product(V1,V2)
print(pp)
#Producto cruz
pc = Vector3D.cross_product(V1,V2)
print(pc)
#Division por un escalar
dp = Vector3D.div_scalar(V1,a)
print(dp)
#Magnitud del vector
man = Vector3D.magnitud(V1)
print(man)
#Norma del vector
norm = Vector3D.norma(V1)
print(norm)
norm2 = Vector3D.norma(V0)
print(norm2)

#Vectores en 2D
v1 = Vector2D(1,2)
v2 = Vector2D(8,9)
v0 = Vector2D(0,0)
#Suma
Suma = Vector2D.__add__(v1,v2)
print(Suma)
#Resta
Resta = Vector2D.__sub__(v1,v2)
print(Resta)
#Multiplicacion escalar
Esclr = Vector2D.multiply_by_scalar(v1,5)
print(Esclr)
#Producto punto
Punto = Vector2D.dot_product(v1,v2)
print(Punto)
#Division por un escalar 
Division = Vector2D.div_scalar(v1,7)
print(Division)
#Magnitud
magntpp = Vector2D.magnitud(v1)
print(magntpp)
#Norma
nmr = Vector2D.norma(v1)
mer = Vector2D.norma(v0)
print(nmr)
print(mer)