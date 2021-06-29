import no
import grafo
import copy
# import numpy as np

class DDconjuntoDominanteMinimo:
	def __init__(self):
		anterior = []
		proxima = []
		t = no.No([], 0, [])


	def atualizarEstado(self, j, estado, grafo):
		estado[j] = 0
		for i in range(len(estado)):
			if grafo[j, i] == 1:
				estado[i] = 0
		return estado


	def verificarNoIgual(self, proxima):
		for u in range(len(proxima) - 1):
			if proxima[u].estado == proxima[- 1].estado:
				if proxima[u].custo <= proxima[- 1].custo:
					proxima.pop()
				else:
					proxima.pop(u)
		return proxima	


	def testeInviavel(self, j, estado, grafo):
		inviavel = False
		for i in range(len(estado)):
			if estado[i] == 1:
				maior = i
				for k in range(len(estado)):
					if grafo[i, k] == 1:
						if k > maior:
							maior = k
				if maior == j:
					inviavel = True
		print(inviavel)
		return inviavel


	def encontrarNoOtimo(self):
		gf = grafo.Grafo()
		estado = [1 for x in gf.pesos]
		solParcial = [1 for x in gf.pesos]
		self.proxima = [no.No([], 0, [])]
		self.proxima.pop()
		self.anterior = [no.No(estado, 0, solParcial)]
		for j in range(len(gf.pesos)):
			for u in range(len(self.anterior)):
				if self.testeInviavel(j, self.anterior[u].estado, gf.grafo) == False:
					novoNo = no.No(self.anterior[u].estado, self.anterior[u].custo, self.anterior[u].solParcial)
					novoNo.solParcial[j] = 0
					self.proxima.append(copy.deepcopy(novoNo))
					self.proxima = self.verificarNoIgual(self.proxima)
				novoNo = no.No(self.anterior[u].estado, self.anterior[u].custo, self.anterior[u].solParcial)
				novoNo.solParcial[j] = 1
				novoNo.estado = self.atualizarEstado(j, novoNo.estado, gf.grafo)
				novoNo.custo += gf.pesos[j]
				self.proxima.append(copy.deepcopy(novoNo))
				self.proxima = self.verificarNoIgual(self.proxima)
			self.anterior = self.proxima.copy()
			# print(len(self.anterior))
			self.proxima.clear()
		t = self.anterior[0]
		return t