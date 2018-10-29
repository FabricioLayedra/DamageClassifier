#!/usr/local/bin/python
# coding: latin-1
import sys
from math import log

input_file = sys.argv[1] #name of the csv with distances
f = open(input_file)

output_file = sys.argv[2] #name of the output csv with data to create the graph
f2 = open(output_file, 'w')

#read the headers of the csv with distances
f.readline() 
pares = {}
f2.write('source,target,weight\n')

max_distance = 0 #maxima distancia entre todas las actividades del dataset

for record in f:
    record = record.strip()
    fields = record.split(',')
    date = fields[1]
    #obtener GeoIdEvento 
    id_evento=fields[-2]
    #Obtener GeoIdCliente (estas torres van a apuntar a la torre con GeoIdEvento)
    id_cliente = fields[-3]
    #obtener num clientes
    usuarios = fields[-4]
    #obtener distancia
    distancia = fields[-1]

    if (date == '2016-04-15'):
    #if (id_evento != '?' and id_cliente != '?' and (fields[1] == '2016-07-16' or fields[1] == '2016-07-15')):
        if (id_evento, id_cliente) in pares:
            print("I AM HERE")
            pares[(id_evento, id_cliente)][0] += int(usuarios)
        else:
            print("I AM ALREADY")
            info =[int(usuarios),float(distancia)]
            pares[(id_evento, id_cliente)] = info
            #refrescar el valor de la maxima distancia dentro del dataset
            if(float(distancia)>max_distance):
                max_distance = float(distancia)
f.close()

#create the file to form the graph
for k,v in pares.items():
    if(v[0]==1):
        weight = log(v[0]) * (v[1]/max_distance)
    else:
        weight = log(v[0] + 1) * (v[1]/max_distance)

    print(k[1] + ',' + k[0] + ',' + str(weight) + '\n')
    f2.write(k[1] + ',' + k[0] + ',' + str(weight) + '\n')

f2.close()
