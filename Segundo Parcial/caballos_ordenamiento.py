import random
vel_cab = [ ]
for i in range (0,25):
	n= random.randint(1,100)
	vel_cab.append(n)
print("Lista de caballos y velocidades")
print(vel_cab)

print("\nGrupos desordenados")

grupos = [[],[],[],[],[]]
k=0
for j in range(0,5): 
	for i in range (0,5):
		grupos[j].append(vel_cab[k])
		k=k+1
	print(grupos[j])
k=k+5

print("\nGrupos ordenados, 5 carreras")

for j in range(0,5):
	grupos[j].sort()
	print(grupos[j])

for j in range(1,5):
	gactual=grupos[j]
	actual=grupos[j][4]
	i=j
	while i>0 and grupos[i-1][4]>actual:
		grupos[i]=grupos[i-1]
		i=i-1
	grupos[i]=gactual
	
print("\nGrupos ordenados por caballo mas rapido, 6ta carrera")
for j in range(0,5):
	print(grupos[j])
	
print("\n7ma carrera")
ult_grupo=[grupos[3][3],grupos[3][4],grupos[4][2],grupos[4][3],grupos[4][4]]
ult_grupo.sort(reverse=True)
print("Caballos mas veloces: ")
print(ult_grupo[0],ult_grupo[1])

print("\nComprobacion")
print("Lista de 25 sorteada")
vel_cab.sort(reverse=True)
print(vel_cab)
print("Caballos mas veloces: ")
print(vel_cab[0],vel_cab[1])
