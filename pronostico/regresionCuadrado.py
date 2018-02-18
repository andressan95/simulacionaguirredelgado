##############################################################
#si quieres pedir los datos por pantalla descomenta estas lineas
#print("ingrese array de x")
#x = input()
#x = eval('[' + x + ']')
#print("ingrese array de y")
#y = input()
#y = eval('[' + y + ']')

##############################################################
#si quieres pedir los datos por pantalla comenta  estas lineas
#Definir valores estaticamente
xgraf=[1850,1860,1870,1880,1890,1900,1910,1920,1930,1940,1950]
x=[-5,-4,-3,-2,-1,0,1,2,3,4,5]
y=[23.2,31.4,39.8,50.2,62.9,76.0,92.0,105.7,122.8,131.7,151.1]

##############################################################

#Declaro variables necesarias para metodo cuadrado
xcuad=0
xcub=0
xcuar=0
xy=0
xcuady=0
n=0
sumx=0
sumy=0
sumxcuad=0
sumxcub=0
sumxcuar=0
sumxy=0
sumxcuady=0


if len(x) != len(y):
	print("los valores de x no coinciden con los valores de y")
else:
	print("Datos")
	print("N"," ", "X","     ","Y","  ","X^2","     ","x^3","     ","x^4","     ","XY","     ","x^2 y")
	#calculando
	for i in range(len(x)):
		#hacemos todos los calculos respectivos
		#x^2
		xcuad = round(x[i]*x[i],1)
		#x^3
		xcub = round(x[i]*x[i]*x[i],1)
		#x^4
		xcuar = round(x[i]*x[i]*x[i]*x[i],1)
		#xy
		xy= round(x[i]*y[i],1)
		#y^2
		xcuady= round(x[i]*x[i]*y[i],1)
		# mostramos los datos por pantalla n, x , y , x^2 , xy , y^2
		print(i+1,"  ", x[i],"  ",y[i]," ",xcuad,"   ",xcub,"   ",xcuar,"   ",xy,"   ",xcuady)
		#numeros
		n=n+1
		
		#suma de x
		sumx= round(sumx+x[i],1)
		#suma de y
		sumy= round(sumy+y[i],1)
		#suma de x^2
		sumxcuad = round(sumxcuad+xcuad,1)
		#suma de x^3
		sumxcub = round(sumxcub+xcub,1)
		#suma de x^4
		sumxcuar = round(sumxcuar+xcuar,1)
		#suma de xy
		sumxy = round(sumxy+xy,1)
		#suma de y^2
		sumxcuady = round(sumxcuady+xcuady,1)

	print("Sumatorias")
	print("N=",n, "Σx=",sumx ,"Σy=", sumy,"Σx^2=",sumxcuad,"Σx^3=",sumxcub,"Σx^4=",sumxcuar,"Σxy=",sumxy,"Σx^2 y=",sumxcuady)
	print("Calculando ecuaciones - Metodo determinante")
	
	#metodo de determinantes en ecuacion de 3 incognitas
	#Calcular Determinante 
	dete1 =(n*sumxcuad*sumxcuar)+(sumx*sumxcub*sumxcuad)+(sumxcuad*sumx*sumxcub)
	dete2 =(sumxcuad*sumxcuad*sumxcuad)+(sumxcub*sumxcub*n)+(sumxcuar*sumx*sumx)
	dete =dete1-dete2
	#print(dete)
	
	#caluclar a0
	a001=(sumy*sumxcuad*sumxcuar)+(sumxy*sumxcub*sumxcuad)+(sumxcuady*sumx*sumxcub)
	a002=(sumxcuad*sumxcuad*sumxcuady)+(sumxcub*sumxcub*sumy)+(sumxcuar*sumx*sumxy)
	a00=a001-a002
	a0=round(a00/dete,2)
	print("El valor de a0 es: ",a0)
	
	#caluclar a1
	a011=(n*sumxy*sumxcuar)+(sumx*sumxcuady*sumxcuad)+(sumxcuad*sumy*sumxcub)
	a012=(sumxcuad*sumxy*sumxcuad)+(sumxcub*sumxcuady*n)+(sumxcuar*sumy*sumx)
	a01=a011-a012
	a1=round(a01/dete,2)
	print("El valor de a1 es: ",a1)

	#caluclar a2
	a021=(n*sumxcuad*sumxcuady)+(sumx*sumxcub*sumy)+(sumxcuad*sumx*sumxy)
	a022=(sumy*sumxcuad*sumxcuad)+(sumxy*sumxcub*n)+(sumxcuady*sumx*sumx)
	a02=a021-a022
	a2=round(a02/dete,4)
	print("El valor de a2 es: ",a2)

	#Pedimos el valor a predecir en funcion de X
	#valor_predecir=6
	valor_predecir = int (input("ingrese valor a predecir en funcion de X: "))

	##calculando pronostico
	pron= round(a0+a1*valor_predecir+a2*(valor_predecir*valor_predecir),2)

	print("El pronostico es:",pron)
