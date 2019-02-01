#!/usr/local/bin/python
# coding: latin-1
import sys
from math import log

"""script that reads a csv with distances and create a file with node A, node B and Weight fields, in order to create a graph afterwards.
The calculation of the edges weights has the formula:
wij = log (usersi) * distanceij / max_distance
 """
 
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
    date = fields[2]
    #obtener GeoIdEvento 
    id_evento=fields[-2]
    #Obtener GeoIdCliente (estas torres van a apuntar a la torre con GeoIdEvento)
    id_cliente = fields[-3]
    #obtener num clientes
    usuarios = fields[-4]
    #obtener distancia
    distancia = fields[-1]
    #obtener provincia cliente
    prov_cliente = fields[3]
    #obtener provincia evento
    prov_evento = fields[10]
    #obtener parroquia evento
    parr_evento = fields[13]
    #obtener parroquia cliente
    parr_cliente = fields[6]
    #obtener canton cliente
    canton_cliente = fields[4]
    #obtener canton evento
    canton_evento = fields[11]

    #if (parr_cliente!=parr_evento):
    #if (canton_cliente!=canton_evento):
    #if (parr_cliente==parr_evento):
    #if(prov_evento!=prov_cliente):
    if (id_evento, id_cliente) in pares:
        pares[(id_evento, id_cliente)][0] += int(usuarios)
    else:
        info =[int(usuarios),float(distancia)]
        pares[(id_evento, id_cliente)] = info
        #refrescar el valor de la maxima distancia dentro del dataset
        if(float(distancia)>max_distance):
            max_distance = float(distancia)
f.close()

#create the file to form the graph
#v is [users,distance]
#k is (event_tower,home_tower)
for k,v in pares.items():
    #if there was just one user
    if(v[0]==1):
        weight = log(v[0]+1)
    else:
        weight = log(v[0])
    if(v[1]==0):
        weight = weight*(v[1]+1/max_distance)
    else:
        weight = weight*(v[1]/max_distance)

    print(k[1] + ',' + k[0] + ',' + str(weight) + '\n')
    f2.write(k[1] + ',' + k[0] + ',' + str(weight) + '\n')

f2.close()
