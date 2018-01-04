import json
#data=({"resistencia a la traccion" : 188 }, {"Alargamiento" : 3.3 }, {" Coeficiente de dillatacion termica" : 18.6})
#with open ("constante.json", 'w') as f: #w de write, r de read
#	json.dump(data, f)

with open("constante.json") as g:
	c = json.load(g)

constresist= c[0]
constalargamiento = c[1]
constcoeficiente = c[2]
constresist= constresist['resistencia'] 
print (constresist)

