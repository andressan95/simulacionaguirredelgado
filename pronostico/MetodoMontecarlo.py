
def montacarlo(v,f,n):
    valor=[]
    frecuencia=[]
    numeros_aleatoreos=[]
    for item1 in v:
        valor.append(float(item1))

    for item2 in f:
        frecuencia.append(float(item2))

    for item3 in n:
        numeros_aleatoreos.append(float(item3))


    l_acumulada=[]
    l_desde=[0]
    l_valor_simulado=[]
    acumulada=0.0
    suma=0.0
    promedio=0.0
    contador=0
    for fre in frecuencia:
        acumulada=round(acumulada+frecuencia[contador],3)
        l_acumulada.append(acumulada)
        contador=contador+1

    contador_d=0
    for des in l_acumulada:
        l_desde.append(round(l_acumulada[contador_d]+0.001,3))
        contador_d=contador_d+1

    conrador3=0
    rango=len(numeros_aleatoreos)
    for nu in range(0, rango):
        valor_simulado=calculo(numeros_aleatoreos[conrador3],l_desde,l_acumulada,valor)
        l_valor_simulado.append(valor_simulado)
        suma=suma+valor_simulado
        conrador3=conrador3+1


    promedio=round(suma/len(numeros_aleatoreos),3)
    return valor,frecuencia,l_acumulada,l_desde,l_acumulada,numeros_aleatoreos,l_valor_simulado,suma,promedio


def calculo(numero_aleatoreo, lista_desde, lista_hasta, lista_valor):
    valor_simulado=0

    for i in range(0, len(lista_valor)):
        if numero_aleatoreo >= lista_desde[i] and numero_aleatoreo < lista_hasta[i]:
            valor_simulado = lista_valor[i]
    return valor_simulado

