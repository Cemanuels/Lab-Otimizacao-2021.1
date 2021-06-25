import numpy as np
	

class Grafo:
	def __init__(self):
		self.grafo = self.lergrafo() #Matriz do grafo 
		self.pesos = self.lerpesos() #pesos dos vértices(sempre 1)


	def lergrafo():
		try:
			file = open("instancia1.txt", "rt")
		
		except:
			print("Erro ao ler o arquivo.")
			file.close()

		else:
			x = int(file.readline())
			grafo = np.zeros((x,x)) #Cria uma matriz de tamanho NxN
			for i in range(int(file.readline())): #for percorendo o número de arestas e prenchendo a matriz
				x = file.readline()
				x = line.split(" ")
				x = [int(x) for x in x]
				grafo[x[0] - 1, x[1] - 1] = 1
				#grafo[x[1] - 1, x[0] - 1] = 1
			file.close()
			return grafo


	def lerpesos():
		try:
			file = open("instancia1.txt", "rt")

		except:
			print("Erro ao ler o arquivo.")
			file.close()

		else:
			x = int(file.readline())
			pesos = no.ones(x) #Vetor de tamanho N com somente 1's.
			file.close()
			return pesos
