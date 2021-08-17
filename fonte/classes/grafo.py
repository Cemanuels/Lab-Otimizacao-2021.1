import numpy as np
	

class Grafo:
	def __init__(self):
		self.grafo = self.lergrafo() #Matriz do grafo 
		self.pesos = self.lerpesos() #pesos dos vértices

	#Lê o arquivo texto e retorna a matriz que representa o grafo do problema
	def lergrafo(self):
		try:
			file = open("./instancias/instancia1.txt", "rt") #Alterar o nome do arquivo para alterar a instância
		
		except:
			print("Erro ao ler o arquivo.")
			file.close()

		else:
			x = int(file.readline())
			grafo = np.zeros((x,x)) 
			for i in range(int(file.readline())):
				x = file.readline()
				x = x.split(" ")
				x = [int(x) for x in x]
				grafo[x[0] - 1, x[1] - 1] = 1
				grafo[x[1] - 1, x[0] - 1] = 1
			file.close()
			return grafo

	#Lê o arquivo texto e retorna os pesos de cada vértice
	def lerpesos(self):
		try:
			file = open("./instancias/instancia1.txt", "rt")

		except:
			print("Erro ao ler o arquivo.")
			file.close()

		else:
			x = int(file.readline())
			pesos = np.ones(x) #Vetor de tamanho N com somente 1's.
			file.close()
			return pesos
