#print("ingrese array de x")
#x = input()
#x = eval('[' + x + ']')
#print("ingrese array de y")
#y = input()
#y = eval('[' + y + ']')

x=[100,200,300,400,500,600,700]
y=[40,50,50,70,65,65,80]

xcuad=0
xy=0
ycuad=0
n=0
sumx=0
sumy=0
sumxcuad=0
sumxy=0
sumycuad=0

if len(x) != len(y):
	print("los valores de x no coinciden con los valores de y")
else:
	print("N"," ", "X","     ","Y","  ","X^2","     ","XY","     ","Y^2")
	#calculando
	for i in range(len(x)):
		#hacemos todos los calculos respectivos
		#x^2
		xcuad = x[i]*x[i]
		#xy
		xy=x[i]*y[i]
		#y^2
		ycuad=y[i]*y[i]
		# mostramos los datos por pantalla n, x , y , x^2 , xy , y^2
		print(i+1," ", x[i],"  ",y[i]," ",xcuad,"   ",xy,"   ",ycuad)
		#numeros
		n=n+1
		#suma de x
		sumx= sumx+x[i]
		#suma de y
		sumy= sumy+y[i]
		#suma de x^2
		sumxcuad = sumxcuad+xcuad
		#suma de xy
		sumxy = sumxy+xy
		#suma de y^2
		sumycuad = sumycuad+ycuad

	print("N=",n, "Σx=",sumx ,"Σy=", sumy,"Σx^2=",sumxcuad,"Σxy=",sumxy,"Σy^2=",sumycuad)
	print("Calculando ecuaciones - Metodo determinante")
	#calculo la determinante
	deter = round((n*sumxcuad)-(sumx*sumx),3)
	#calculo de a0
	a0 = round(((sumy*sumxcuad)-(sumx*sumxy))/deter,3)
	#calculo de a1
	a1 = round(((n*sumxy)-(sumx*sumy))/deter,3)

	#Pedimos el valor a predecir en funcion de X
	#valor_predecir=800
	valor_predecir = int (input("ingrese valor a predecir en funcion de X: "))

	#mostrando valor de a0 y x1
	print("El valor de a0 es:",a0)
	print("El valor de a1 es:",a1)
	##calculando pronostico
	pron= round(a0+a1*valor_predecir,3)

	print("El pronostico es:",pron)
