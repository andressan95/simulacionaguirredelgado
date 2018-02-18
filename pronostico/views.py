# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
mpromedio = []
def promedio(listadatos, listaeventos, Ndatos):
    su1 = []
    su = 0.0
    su2 = 0.0
    contador = 0
    er = 0.0
    fd = 0.0
    bn = 2
    n = 0

    print "\tPERIODO\t\tACCION\t\tPROMEDIO MOVIL"
    print""
    for i in range(0, Ndatos):
        a = i+1
        pro = 0.0
        su = su + su2 + listaeventos[n]

        if n == bn:
            bn = bn - 1
            pro = su / 3
            su = listaeventos[n]
            n = n + 1
            su2 = listaeventos[n]
            n = n - 3

        n = n + 1

        print "\t", listadatos[i], "\t\t{0:.2f}".format(listaeventos[i]);
        print;
        print"\t\t\t\t\t\t{0:.2f}".format(pro)
        mpromedio.append([a,listadatos[i],format(listaeventos[i]),pro])

def promedio_movil(request):
    if request.method == 'POST':
        del mpromedio[:]

        metodo = request.POST['metodo']

        if metodo == 'promediomovil':
            listadatos = []
            listaeventos = []
            num = []
            n = int(request.POST['n'])
            neventos = request.POST.getlist('eventos')
            ndatos = request.POST.getlist('datos')

            Ndatos = int(n)
            del num[:]
            nume = n
            num.append(nume)
            for i in range(0, Ndatos):

                eventos = float(neventos[i])
                datos = float(ndatos[i])
                listaeventos.append(eventos)
                listadatos.append(datos)

            promedio(listadatos, listaeventos, Ndatos)

            return render(request, 'pronostico/index.html',
                          {'promedio': mpromedio})

    return render(request, 'pronostico/index.html')


