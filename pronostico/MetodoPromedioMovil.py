
def promedioMovil(periodo,datos,variable):
    l_pronostico=[]
    l_error=[]
    l_error2=[]

    inicio=0
    final=variable
    suma=0.0
    promedio=0.0
    suma_error=0.0
    suma_error2=0.0
    pronostico=0.0
    n=len(datos)
    for i in range(0,variable):
        l_pronostico.append(0)
        l_error.append(0)
        l_error2.append(0)

    for calc in range(variable-1,n):
        suma=0.0
        for k in range(inicio,final):
            suma=round(suma+datos[k],3)

        promedio=round(suma/variable,3)
        l_pronostico.append(promedio)
        inicio=inicio+1
        final=final+1

    for  sa in range(0,len(l_pronostico)-1):
        if l_pronostico[sa]>0:
            xn = datos[sa]
            pro=l_pronostico[sa]
            er = round(xn - pro, 3)
            l_error.append(er)
            er2 = round(er * er, 3)
            l_error2.append(er2)

    for er in l_error:
        suma_error=round(suma_error+er,3)

    for  er2 in l_error2:
        suma_error2=round(suma_error2+er2,3)

    pronostico=l_pronostico[len(l_pronostico)-1]

    return periodo,datos,l_pronostico,l_error,l_error2,suma_error,suma_error2,pronostico
