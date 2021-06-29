import numpy as np


def lergrafo():
		try:
			file = open("instancia1.txt", "rt")
			
		except:
			print("Erro ao ler o arquivo")
			file.close()

		else:
			x = int(file.readline())
			grafo = np.zeros((x,x)) #Cria uma matriz de tamanho NxN
			for i in range(int(file.readline())): #for percorendo o número de arestas 
				x = file.readline()
				x = x.split(" ")
				x = [int(x) for x in x]
				grafo[x[0] - 1, x[1] - 1] = 1
				grafo[x[1] - 1, x[0] - 1] = 1	
			file.close()
			print(grafo)
			return grafo

def lerpesos():
		try:
			file = open("instancia1.txt", "rt")

		except:
			print("Erro ao ler o arquivo.")
			file.close()
			
		else:
			x = int(file.readline())
			pesos = np.ones(x)
			file.close()
			print(pesos)
			return pesos

x = lergrafo()
x = lerpesos()