import json
data = {"metal": [ {"Carbono": [ {"Minimo": 10,"Maximo":15}]}, {"Silicio" : [ {"Minimo":10, "Maximo":15}]},{"Silicio" : [ {"Minimo":10, "Maximo":15}]},{"Manganeso" : [ {"Minimo": 10, "Maximo":15}]}, {"Cromo": [ {"Minimo": 10,"Maximo":15}]},{"Niquel" : [ {"Minimo": 10,"Maximo":15}]}, {"Cobre": [ {"Minimo": 10,"Maximo":15}]},{"Azufre": [ {"Minimo": 10,"Maximo":15}]},{"Hierro": [ {"Minimo": 10,"Maximo":15}]} ]}

with open ("acumuladormetales.json", 'w') as f: #w de write, r de read
	json.dump(data, f)


#with open("acumuladormetales.json") as g:
#	c = json.load(g)
#fecha= c[0]# fecha del json
#contador = c[1]
#fecha= fecha['fecha']
#contador = int(contador['contador'])
#if fecha == dia: #dia actual
#	contador += 1

#else:
#	contador = 1
#	fecha = dia
#data = ({"fecha" : fecha}, {"contador" : contador})
#with open ("contador.json", 'w') as f: #w de write, r de read
#	json.dump(data, f)	

