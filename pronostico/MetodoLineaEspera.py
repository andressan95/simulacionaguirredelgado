import  math
li1=[0.870,0.770,0.040,0.190,0.350,0.400,0.560,0.460,0.120,0.110,0.790,0.230,0.280,0.020,0.960,0.860]
li2=[0.710,0.350,0.070,0.160,0.900,0.620,0.540,0.730,0.450,0.690,0.970,0.780,0.590,0.850,0.880,0.960]

def metodo_linea_espera(landa,mi_u,lista_alea_llegada,lista_aleatorieo_servicio):
    l_t_llegada=[]
    l_t_servicio=[]
    l_t_exa_llegada=[0]
    l_h_iniciacion=[0]
    l_h_teriacion=[0]
    l_t_espera=[0]
    l_t_sistema=[0]
    t_llegada = 0
    t_servicio = 0
    h_exata_llegada=0
    h_iniciacion = 0
    h_termiacion = 0
    t_espera = 0
    t_sistema = 0

    for llegada in range(0,len(lista_alea_llegada)):
        t_llegada= round((-(1/landa) * math.log(lista_alea_llegada[llegada])),3)
        l_t_llegada.append(t_llegada)

    for servicio in range(0,len(lista_aleatorieo_servicio)):
        t_espera= round((-(1/mi_u)* round(math.log(lista_aleatorieo_servicio[servicio]),3)),3)
        l_t_servicio.append(t_espera)

    for h_exacta in l_t_llegada:
        h_exata_llegada= round(h_exacta+h_exata_llegada,4)
        l_t_exa_llegada.append(h_exata_llegada)

    bandera = len(lista_alea_llegada)
    contador = 0
    while (bandera>0):
        h_iniciacion=max(round(l_t_exa_llegada[contador+1],3), round(l_h_teriacion[contador],3))
        l_h_iniciacion.append(h_iniciacion)
        h_termiacion=round(l_t_servicio[contador]+l_h_iniciacion[contador+1],3)
        l_h_teriacion.append(h_termiacion)
        contador=contador+1
        bandera = bandera - 1

    bandera = len(l_h_teriacion)
    contador2 = 0
    while (bandera>0):
        t_espera=round(l_h_iniciacion[contador2]-l_t_exa_llegada[contador2],3)
        l_t_espera.append(t_espera)
        contador2=contador2+1
        bandera = bandera - 1



    bandera=len(lista_alea_llegada)
    contador3 = 0
    while (bandera>0):
        t_sistema=round(l_t_espera[contador3+2]+l_t_servicio[contador3],3)
        l_t_sistema.append(t_sistema)
        contador3=contador3+1
        bandera = bandera - 1


    # Funcion que recibe una lista de valores y retorna el promedio de ellos
    def promedio(lista):
        sumaParcial = 0
        for valor in lista:
            sumaParcial += valor
        cantidadValores = len(lista)
        return round(sumaParcial / float(cantidadValores),3)

    print("\n", lista_alea_llegada, "\n", lista_aleatorieo_servicio, "\n", l_t_llegada, "\n", l_t_servicio, "\n",
              l_t_exa_llegada, "\n", l_h_iniciacion, "\n", l_h_teriacion, "\n", l_t_espera, "\n", l_t_sistema,"\n Este metodo lo pueden utilizar para las listas",promedio(l_t_sistema))

    #return l_alea_llegada,l_alea_servicio,l_t_llegada,l_t_servicio,l_t_exa_llegada,l_h_iniciacion, l_h_teriacion,l_t_espera,l_t_espera

