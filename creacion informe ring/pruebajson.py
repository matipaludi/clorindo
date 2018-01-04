import json
import time
dia = time.strftime("%d/%m/%y") 
fecha = time.strftime("%d/%m/%y") 

#data=({"fecha" : fecha}, {"contador" : 1})
#with open ("contador.json", 'w') as f: #w de write, r de read
#	json.dump(data, f)

with open("contador.json") as g:
	c = json.load(g)


fecha= c[0]# fecha del json
contador = c[1]
fecha= fecha['fecha']
contador = int(contador['contador'])
if fecha == dia: #dia actual
	contador += 1

else:
	contador = 1 
	fecha = dia

data = ({"fecha" : fecha}, {"contador" : contador})
with open ("contador.json", 'w') as f: #w de write, r de read
	json.dump(data, f)	
