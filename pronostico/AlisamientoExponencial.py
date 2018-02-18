from random import random, randrange
 #NOTA!
# se estan tomando valores aleatorios generados por random en Xn, el metodo como se van
#a ingresar depende de cada uno, incluso podria hacer un for con un input para
#agregar cada uno de los valores de Xn o tomar los valores q se generen
#por medio de los metodos q ya vimos antes

#dudas abajo en la caja de comentarios

#borracho maricon v:

def calcularAliExpo ():
    # pide alfa
    a = float(input("Ingrese alfa"))
    # pide la cantidad de eventos N
    n = int(input("Ingrese la cantidad eventos "))

    listaXn = []
    listaN = []
    listaSn = []
    listaEr = []
    bandera = 1
    sn=0
    xn=0
    er=0
    for i in range(1, n + 1):  # repite n interaciones
        x = round(randrange(200,350))  # calcula el numero random con 3 interaciones
        listaXn.append(float(x))#guarda xn
        listaN.append(i)  # guarda xn

    for j in range(0,n):

        if (bandera == 1):  # en caso de ser la primera interacion asigna 0 en SN
            listaSn.append(0)
            listaEr.append(0)
            bandera=2
        else:
            if(bandera==2):
                sn=listaXn[0] #toma el primer valor de Xn
                listaSn.append(sn) #en caso de ser la segunda interacion asigna en valor anterior de Xn
                xn= listaSn[1] #guarda el valor actual de xn
                er= xn-sn #calcula el error
                listaEr.append(er)
                bandera = 0

            else:
                print("entro")
                sn0 = listaSn[j-1] #valor anterior de sn
                xn0 = listaXn[j-1] #valor anterior de xn
                sn= a*xn0+(1-a)*sn0
                xn=  listaXn[j]
                er= xn-sn
                listaSn.append(sn)
                listaEr.append(er)
                print("sn anterior"+str(sn0))
                print("xn anterior" + str(xn0))

    #para calcular el ultima valor
    sn0 = listaSn[n- 1]  # valor anterior de sn
    xn0 = listaXn[n- 1]  # valor anterior de xn
    sn = a * xn0 + (1 - a) * sn0
    listaXn.append(0)
    listaSn.append(sn)
    listaEr.append(0)
    listaN.append("final")

    for k in range(0, n+1):
        print(" "+str(listaN[k])+" "+str(listaXn[k])+" "+str(listaSn[k])+" "+str(listaEr[k]))

calcularAliExpo()
