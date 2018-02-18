  
print ("***********Metodo de regresion lineal*************")  

Z = int (input("Ingrese la cantidad de datos que desea ingresar: "))
X_lista=[]
Y_lista=[]
X2_lista=[]
Y2_lista=[]
XY=[]
lista_x=[]
lista_y=[]
calculo=[]
Sx=0
Sy=0
Sx2=0
Sy2=0
Sxy=0

#Ingreso de 
for i in range(Z):
	Xn = float (input("Ingrese el valor de X(ventas): "))
	Xn=round(Xn,3)
	X_lista.append(Xn)
	y=float (input("Ingrese el valor de Y (eventos): "))
	y=round(y,3)
	Y_lista.append(y)

#Multiplicando x2
i=0
for i in range(Z):
	x=X_lista[i]
	x=round(x*x,3)
	X2_lista.append(x)

#multiplicando Y2
i=0
for i in range(Z):
	a=Y_lista[i]
	z=round(a*a,3)
	Y2_lista.append(z)

#Multiplicando XY
i=0
for i in range(Z):
	x=X_lista[i]
	y=Y_lista[i]
	z=round(x*y,3)
	XY.append(z)

#Multiplicando Sumatorias
i=0
for i in range(Z):
	a=X_lista[i]
	Sx=round(Sx+a,3)
	a=Y_lista[i]
	Sy=round(Sy+a,3)
	a=X2_lista[i]
	Sx2=round(Sx2+a,3)
	a=Y2_lista[i]
	Sy2=round(Sy2+a,3)
	a=XY[i]
	Sxy=round(Sxy+a,3)

#Calculando ecuaciones - Metodo determinante
deter = round((Z*Sx2)-(Sx*Sx),3)
equi = round((Sx*Sxy)-(Sx2*Sy),3)
ye = round((Z*Sy)-(Sx*Sxy),3)
equis = round(equi/deter,3)
yes = round(ye/deter,3)

print ("Sumatoria de valores: ")
print (" X  -  Y  -  X2  -  XY  -  Y2")
valores =(Sx, Sy, Sx2, Sxy, Sy2)
print valores


print ("Resultado del sistema de ecuaciones:")
valorx =("valor de x= ",equis)
valory =("valor de y= ",yes)
print valorx
print valory

i=0
for i in range(Z):
	x=X_lista[i]
	mul = yes*x
	suma =round(mul+equis,3)
	calculo.append(suma)
total=0
i=0
print ("-- Pronostico --")
for i in range(Z):
	c=calculo[i]
	print (c)
