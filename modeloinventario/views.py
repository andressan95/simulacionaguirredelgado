# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render
# Create your views here.
from aleatorios.views import metodo_multiplicativo, op_metodo_lineal

num = []
datos = []
mx = []
mprob = []
mfreca = []
mfrecd = []
mfrecda = []
mdesde = []
mfrecd2 = []
matrizNueva = []
mfreha2 = []
mresultado = []
mnume = []
# Matrices Modelo Inventario
numDemanda = []
numTiempo = []
msumDemanda = []
msumTiempo = []
mfrecaDemanda = []
mfrecaTiempo = []

datosDemanda = []
datosTiempo = []
mdesdeTiempo = []
mdesdeDemanda = []
mdhDemanda = []
mdhTiempo = []

matrizDemanda = []
matrizTiempo = []
xDemanda = []
xTiempo = []

mresultadoDemanda = []
mresultadoTiempo = []


invdatos = []
mDemanda = []

mInventario = []

#absoluta

datosInventarioA = []
datosInventarioDemA = []
datosInventarioProbA = []
datosTiempoProbA = []
datosTiempoDemA = []
smx = []
smprob = []
def monte_carlo(request):
    del numDemanda[:]
    del numTiempo[:]
    del datosTiempo[:]
    del datosDemanda[:]
    del mfrecaDemanda[:]
    del mfrecaTiempo[:]
    del mdesdeTiempo[:]
    del mdesdeDemanda[:]
    del mdhDemanda[:]
    del mdhTiempo[:]

    del matrizDemanda[:]
    del matrizTiempo[:]

    del xDemanda[:]
    del xTiempo[:]

    del mresultadoDemanda[:]
    del mresultadoTiempo[:]

    del invdatos[:]
    del mDemanda[:]

    del mInventario[:]

    if request.method == 'POST':



        metodo = request.POST['metodo']

        if metodo == 'numeros':

            nDemanda = int(request.POST['nDemanda'])
            nTiempo = int(request.POST['nTiempo'])

            numeDemanda = nDemanda + 1
            numeTiempo = nTiempo + 1

            numDemanda.append(nDemanda)
            numTiempo.append(nTiempo)

            if nDemanda <= 0 or nTiempo <= 0:
                messages.error(request, "Ingrese valores mayores a 0")

            return render(request, 'modeloInventario/index.html',
                          {'numeDemanda': range(1, numeDemanda), 'numeTiempo': range(1, numeTiempo)})

        elif metodo == 'inventario':

            metodofrecuencia = request.POST['metodofrecuencia']
            metodoa = request.POST['metodoa']

            if metodofrecuencia == 'FrecuenciaAbsoluta':
                del mprob[:]
                del mfreca[:]
                del datos[:]
                del mfrecd[:]
                del mfrecd2[:]
                del mfreha2[:]
                del mresultado[:]
                del mx[:]
                del datosInventarioDemA[:]
                del datosInventarioProbA[:]
                del datosTiempoProbA[:]
                del datosTiempoDemA[:]
                del smx[:]
                del smprob[:]

                demandaInventarioA = request.POST.getlist('demandaInventarioA')
                valorInventarioA = request.POST.getlist('valorInventarioA')


                demandaTiempoA = request.POST.getlist('demandaTiempoA')
                valorTiempoA = request.POST.getlist('valorTiempoA')

                print(valorInventarioA,valorTiempoA,demandaInventarioA,demandaTiempoA)

                sumLlegadasA = 0
                sumServicioA = 0
                # matriz de suma para valores de frecuencia
                msumLlegada = []
                # se realiza recorrido y se suman los valores de frecuencia
                # suma de frecuencia
                for i in range(len(valorInventarioA)):
                    sumLlegadasA = sumLlegadasA + float(valorInventarioA[i])
                    msumLlegada.append(sumLlegadasA)
                for i in range(len(valorTiempoA)):
                    sumServicioA = sumServicioA + float(valorTiempoA[i])
                    msumLlegada.append(sumServicioA)
                for i in range(len(valorInventarioA)):
                    # valores de frecuencia y valores de x
                    # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                    x = int(demandaInventarioA[i])

                    # Metodo de probabilidad
                    # se divide el valor de frecuencia sobre la suma
                    prob = float(valorInventarioA[i]) / sumLlegadasA
                    # se guarda en matriz mprob la probabilidad
                    mprob.append(prob)
                    # se guarda en matriz mx los valores de x
                    mx.append(x)
                    # Le damos formato al float solo con 3 decimales
                    # para frecuencia HASTA
                    freh = float(mprob[i])
                    prob = round(float(freh), 3)

                    # Hacemos matriz datos y guardamos todos los datos generados
                    datosInventarioProbA.append(prob)
                    datosInventarioDemA.append(x)
                for i in range(len(valorTiempoA)):
                    # valores de frecuencia y valores de x
                    # se vx[i] siendo i inical 0 hasta el ultimo valor de frecuencia
                    sx = int(demandaTiempoA[i])
                    # Metodo de probabilidad
                    # se divide el valor de frecuencia sobre la suma
                    sprob = float(valorTiempoA[i]) / sumServicioA
                    # se guarda en matriz mprob la probabilidad
                    smprob.append(sprob)
                    # se guarda en matriz mx los valores de x
                    smx.append(sx)
                    # Le damos formato al float solo con 3 decimales
                    # para frecuencia HASTA
                    sfreh = float(smprob[i])
                    sprob = round(float(sfreh), 3)

                    # Hacemos matriz datos y guardamos todos los datos generados
                    datosTiempoProbA.append(sprob)
                    datosTiempoDemA.append(sx)

                valorInventario = datosInventarioProbA
                valorTiempo = datosTiempoProbA
                demandaInventario = datosInventarioDemA
                demandaTiempo = datosTiempoDemA

            elif metodofrecuencia == 'FrecuenciaRelativa':
                demandaInventario = request.POST.getlist('demandaInventario')
                valorInventario = request.POST.getlist('valorInventario')

                demandaTiempo = request.POST.getlist('demandaTiempo')
                valorTiempo = request.POST.getlist('valorTiempo')

            if metodoa == 'Lineal':
                riLlegadas = []
                riServicio = []
                # variables de numeros Demanda
                a = int(request.POST['a'])
                n = int(request.POST['n'])
                xo = int(request.POST['xo'])
                m = int(request.POST['m'])
                xoinicial = xo
                riDemanda = metodo_multiplicativo(a, xo, xoinicial, m, n)

                # variables de numeros Servicio
                ab = int(request.POST['ab'])
                nb = int(request.POST['nb'])
                xob = int(request.POST['xob'])
                mb = int(request.POST['mb'])
                xoinicialb = xob
                riTiempo = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

                print (riLlegadas, riServicio, len(riLlegadas), len(riServicio))

            elif metodoa == 'Multiplicativo':

                # variables de numeros Llegadas
                a = int(request.POST['a'])
                n = int(request.POST['n'])
                xo = int(request.POST['xo'])
                m = int(request.POST['m'])
                xoinicial = xo
                riDemanda = metodo_multiplicativo(a, xo, xoinicial, m, n)

                # variables de numeros Servicio
                ab = int(request.POST['ab'])
                nb = int(request.POST['nb'])
                xob = int(request.POST['xob'])
                mb = int(request.POST['mb'])
                xoinicialb = xob
                riTiempo = metodo_multiplicativo(ab, xob, xoinicialb, mb, nb)

            elif metodoa == 'Manual':
                riDemanda = request.POST.getlist('riDemanda')
                riTiempo = request.POST.getlist('riTiempo')


            sum = 0
            frecaTiempo = 0
            frecaDemanda = 0




            Q = int(request.POST['q'])
            R = int(request.POST['r'])
            IN = int(request.POST['inventario'])
            CH = int(request.POST['ch'])
            CO = int(request.POST['co'])
            CF = int(request.POST['cf'])

            invdatos.append([Q,R,IN,CH,CO,CF])


            # for in para tabla demanda, Mayor Menor y frecuencia
            for i in range(len(valorInventario)):
                a = int(demandaInventario[i])
                xDemanda.append(i)

                frecaDemanda = frecaDemanda + float(valorInventario[i])
                demanda = float(valorInventario[i])
                msumDemanda.append(frecaDemanda)

                mfrecaDemanda.append(frecaDemanda)
                hastaDemanda = float(mfrecaDemanda[i])
                desdeDemanda = float(hastaDemanda) + 0.001

                if mfrecaDemanda[i] == mfrecaDemanda[0]:
                    mdesdeTiempo.insert(int(desdeDemanda), 0)
                    mdesdeDemanda.insert(int(desdeDemanda), 0)
                mdesdeDemanda.append(desdeDemanda)

                datosDemanda.append([a, demanda, frecaDemanda, mdesdeDemanda, hastaDemanda])

            # for in para tabla Tiempo, Mayor Menor y frecuencia
            for i in range(len(valorTiempo)):
                a = int(demandaTiempo[i])
                xTiempo.append(a)

                frecaTiempo = frecaTiempo + float(valorTiempo[i])
                Tiempo = float(valorTiempo[i])
                msumTiempo.append(sum)

                mfrecaTiempo.append(frecaTiempo)
                hastaTiempo = float(mfrecaTiempo[i])
                desdeTiempo = float(hastaTiempo) + 0.001

                mdesdeTiempo.append(desdeTiempo)
                datosTiempo.append([a, Tiempo, frecaTiempo, mdesdeTiempo, hastaTiempo])

            # montecarlo demanda
            for i in range(len(riDemanda)):
                a = i + 1
                demanda = float(riDemanda[i])
                matrizDemanda.append(demanda)
                # recorrido para seleccionar valores de x
                for j in range(len(mfrecaDemanda)):
                    # hacemos un if que compare los datos con la matriz y las frecuencias DESDE y HASTA
                    # si se cumple la funcion se guardan los datos en la matriz mresultado

                    if matrizDemanda[i] >= mdesdeDemanda[j] and  matrizDemanda[i] <=  mfrecaDemanda[j]:
                        # se guardan los datos en la matriz , de numeros aleatorios matrizNueva[i]
                        #  y de la matriz de frecuencia mfreca[j] y matriz de valores de x mx[j]
                        mDemanda.append(xDemanda[j])
                        mresultadoDemanda.append([a, matrizDemanda[i],xDemanda[j]])



            #inventario
            ingresos = 0
            final = 0
            inicial=0
            faltante=0

            sumFaltante=0
            sumMantener=0
            sumOrdenar=0
            costoMantener = 0
            ordenar=0
            entrega=0
            a = 0
            for i in range(len(riDemanda)):
             a = int(i)


             if riDemanda[i] == riDemanda[0]:
                 inicial = int(IN)
                 final = int(IN) - int(mDemanda[i])
                 print "posicion 0"


             elif inicial > 0 and ingresos == 0 and final <= 0:
                 inicial = 0
                 ingresos =0
                 ordenar =0
                 final = 0
                 faltante = int(CF)


                 print "ingresos 0"
             elif inicial == 0 and ingresos == 0 and final <= 0:
                 inicial = 0
                 ingresos = int(IN)
                 ordenar = int(CO)
                 final = ingresos - int(mDemanda[i])
                 faltante=0
                 print "ingresos "

             elif inicial == 0 and ingresos != 0 and final !=0:
                 inicial = final
                 ingresos = 0
                 ordenar = 0
                 final = 0
                 faltante =0
                 print "ingres final"


             else:
                 ingresos = 0
                 faltante = 0
                 ordenar = 0
                 inicial = final
                 final = final - int(mDemanda[i])
                 print "jh"



             costoMantener = final * int(CH)
             sumOrdenar = sumOrdenar + ordenar
             sumMantener = sumMantener + costoMantener
             sumFaltante = sumFaltante + faltante

             mInventario.append([inicial,ingresos,final,faltante,costoMantener,ordenar])
            mdhDemanda.append([mdesdeDemanda, [mfrecaDemanda]])
            mdhTiempo.append([mdesdeTiempo, mfrecaTiempo])

            # montecarlo Tiempo
            for i in range(len(riTiempo)):
                 a = i + 1
                 Tiempo = float(riTiempo[i])
                 matrizTiempo.append(Tiempo)

                 # recorrido para seleccionar valores de x
                 for j in range(len(mfrecaTiempo)):
                     # hacemos un if que compare los datos con la matriz y las frecuencias DESDE y HASTA
                     # si se cumple la funcion se guardan los datos en la matriz mresultado
                     if matrizTiempo[i] >= mdesdeTiempo[j] and matrizTiempo[i] <= mfrecaTiempo[j]:
                         # se guardan los datos en la matriz , de numeros aleatorios matrizNueva[i]
                         #  y de la matriz de frecuencia mfreca[j] y matriz de valores de x mx[j]
                         entrega = a + xTiempo[j] + 1

                         mresultadoTiempo.append([matrizTiempo[i], xTiempo[j],entrega])


            return render(request, 'modeloInventario/index.html',
                          {'sumFaltante':sumFaltante,'sumMantener':sumMantener,'sumOrdenar':sumOrdenar,'mInventario':mInventario,'invdatos':invdatos,
                              'mresultadoDemanda': mresultadoDemanda,'mresultadoTiempo': mresultadoTiempo,  'matrizDemanda': matrizDemanda, 'matrizTiempo': matrizTiempo,
                           'frecaTiempo': mfrecaTiempo, 'frecaDemanda': mfrecaDemanda,
                           'mdhDemanda': mdhDemanda,'xTiempo':xTiempo, 'mdhTiempo': mdhTiempo,
                           'datosDemanda': datosDemanda, 'datosTiempo': datosTiempo,
                           'desdeDemanda': mdesdeDemanda, 'desdeTiempo': mdesdeTiempo})



        # si ocurre un error mostrara mensaje error
        else:
            messages.error(request, "error")
        # renderizamos pagina html
        return render(request, 'modeloInventario/index.html')

        # renderizamos pagina index.html
    return render(request, 'modeloInventario/index.html', {'datosDemanda': datosDemanda, 'datosTiempo': datosTiempo})
