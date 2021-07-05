from classes import no
from classes import grafo
import copy


class DDconjuntoDominanteMinimo:
	def __init__(self):
		self.anterior = [] #Camada anterior do DD
		self.proxima = [] #Proxima camada do DD

	
	#Atualiza o estado se um elemento J receber 0
	def atualizarEstado(self, j, estado, grafo):
		estado[j] = 0
		for i in range(len(estado)):
			if grafo[j, i] == 1:
				estado[i] = 0
		return estado


	#Elimina nós redundantes
	def eliminarNoIgual(self, proxima):
		for u in range(len(proxima) - 1):
			if proxima[u].estado == proxima[- 1].estado:#Testa se o ultimo nó adicionado tem estado igual algum nó antigo
				if proxima[u].custo < proxima[- 1].custo:#Testa se o ultimo nó adicionado tem custo pior
					proxima.pop()
				elif proxima[u].custo != proxima[- 1].custo:#Caso contrário testa se o nó com estado igual tem custo pior
					proxima.pop(u)
		return proxima	
		#OBS:Não exclui nenhum nó com custos iguais.Substituir != por >= para manter apenas um nó, mesmo com custos iguais


	#Dado um estado verifica se é possivel o elemento j receber valor 0
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
		return inviavel

	#Adiciona nó a lista proxima com j = 0 
	def adicionarZero(self, u, j):
		novoNo = copy.deepcopy(u)
		novoNo.solParcial[j] = 0
		self.proxima.append(copy.deepcopy(novoNo))


	#Adiciona nó a lista proxima com j = 1 e atualiza o estado	
	def adicionarUm(self, u, j, gf):
		novoNo = copy.deepcopy(u)
		novoNo.solParcial[j] = 1
		novoNo.estado = self.atualizarEstado(j, novoNo.estado, gf.grafo)
		novoNo.custo += gf.pesos[j]
		self.proxima.append(copy.deepcopy(novoNo))
		self.proxima = self.eliminarNoIgual(self.proxima)


	#Retorna a solução para o problema do conjunto dominante minimo 
	def encontrarNoOtimo(self):
		gf = grafo.Grafo()
		estado = [1 for x in gf.pesos]
		solParcial = [1 for x in gf.pesos]
		self.anterior = [no.No(estado, 0, solParcial)] #Cria a primeira camada com o nó r
		for j in range(len(gf.pesos)):#Percorre as j + 1 camadas
			for u in self.anterior:#Percorre todos os nós da camada anterior
				if self.testeInviavel(j, u.estado, gf.grafo) == False:
					self.adicionarZero(u, j)
					self.proxima = self.eliminarNoIgual(self.proxima)
				self.adicionarUm(u, j, gf)
				self.proxima = self.eliminarNoIgual(self.proxima)
			self.anterior = self.proxima.copy()#anterior recebe uma copia de proxima
			self.proxima.clear()#Limpa proxima antes de passar para próxima camada
		return self.anterior
	