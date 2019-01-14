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
    
    #if (prov_evento=="MANABI" and prov_cliente=="MANABI" and parr_cliente!=parr_evento):
    #if (parr_cliente==parr_evento):
    #if(prov_evento!=prov_cliente):
    if (id_evento, id_cliente) in pares:
        pares[(id_evento, id_cliente)][0] += int(usuarios)
    else:
        info =[int(usuarios)]
        pares[(id_evento, id_cliente)] = info
        
f.close()

#create the file to form the graph
#v is [users,distance]
#k is (event_tower,home_tower)
for k,v in pares.items():
    weight = v[0]
    f2.write(k[1] + ',' + k[0] + ',' + str(weight) + '\n')

f2.close()
