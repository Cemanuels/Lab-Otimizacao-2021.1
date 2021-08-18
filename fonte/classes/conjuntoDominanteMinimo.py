from classes import no
from classes import grafo
from operator import attrgetter
import copy


class DDconjuntoDominanteMinimo:
	def __init__(self):
		self.anterior = [] #Camada anterior do DD
		self.proxima = [] #Proxima camada do DD
	
	#Atualiza o estado se um elementode indice J receber 1
	def atualizarEstado(self, j, estado, grafo):
		estado[j] = 0
		for i in range(len(estado)):
			if grafo[j, i] == 1:
				estado[i] = 0
		return estado


	#Elimina nós redundantes
	def eliminarNoIgual(self, proxima):
		u = 0
		while u < (len(proxima) - 1):
			if proxima[u].estado == proxima[- 1].estado:#Testa se o ultimo nó adicionado tem estado igual algum nó antigo
				if proxima[u].custo < proxima[- 1].custo:#Testa se o ultimo nó adicionado tem custo pior
					proxima.pop()
				elif proxima[u].custo >= proxima[- 1].custo:#Caso contrário testa se o nó com estado igual tem custo pior
					proxima.pop(u)
			u += 1
		return proxima	
		#OBS:Não exclui nenhum nó com custos iguais.Substituir != por >= para manter apenas um nó, mesmo com custos iguais


	#Dado um estado verifica se é possivel o elemento de indice j receber valor 0
	def testeInviavel(self, j, estado, grafo):
		for i in range(len(estado)):
			if estado[i] == 1:
				maior = i
				for k in range(i,len(estado)):
					if grafo[i, k] == 1:
						if k > maior:
							maior = k
				if maior == j:
					return True
		return False
		

	#Adiciona nó a lista proxima com x[j] = 0 
	def adicionarZero(self, u, j):
		novoNo = copy.deepcopy(u)
		novoNo.solParcial[j] = 0
		self.proxima.append(novoNo)


	#Adiciona nó a lista proxima com x[j] = 1 e atualiza o estado	
	def adicionarUm(self, u, j, gf):
		novoNo = copy.deepcopy(u)
		novoNo.solParcial[j] = 1
		novoNo.estado = self.atualizarEstado(j, novoNo.estado, gf.grafo)
		novoNo.custo += gf.pesos[j]
		self.proxima.append(novoNo)


	#Retorna a solução do diagrama exato para o problema do conjunto dominante minimo 
	def encontrarNoOtimo(self, instancia):
		gf = grafo.Grafo(instancia)
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
			self.anterior = self.proxima #anterior recebe uma copia de proxima
			self.proxima = []#Limpa proxima antes de passar para próxima camada
		return self.anterior


	#Retorna a solução do diagrama restrito(aléatorio) para o problema do conjunto dominante minimo 
	def encontrarNoRestrito(self, w, instancia):
		gf = grafo.Grafo(instancia)
		estado = [1 for x in gf.pesos]
		solParcial = [1 for x in gf.pesos]
		self.anterior = [no.No(estado, 0, solParcial)] #Cria a primeira camada com o nó r
		for j in range(len(gf.pesos)):#Percorre as j + 1 camadas
			for u in self.anterior:#Percorre todos os nós da camada anterior
				if len(self.proxima) == w:
					break
				if self.testeInviavel(j, u.estado, gf.grafo) == False:
					self.adicionarZero(u, j)
					self.proxima = self.eliminarNoIgual(self.proxima)
				if len(self.proxima) == w:
					break
				self.adicionarUm(u, j, gf)
				self.proxima = self.eliminarNoIgual(self.proxima)
			self.anterior = self.proxima #anterior recebe uma copia de proxima
			self.proxima = [] #Limpa proxima antes de passar para próxima camada
		return self.anterior


	#Junta os nós para que a camada tenha no maximo largura W
	def unirNos(self, w, proxima):
		proxima = sorted(proxima, key = attrgetter('custo'), reverse = True)#Ordena a camada de acordo com o custo decrescente
		aux = proxima[-w].estado
		proxima[-w].estado = [0 for x in aux]
		while w < len(proxima):#Percorre a camada até que ela tenha tamanho W 
			j = 0
			while j < len(proxima[0].estado):#Percorre o estado
				if aux[j] == proxima[0].estado[j] == 1:#Testa se a variavel j é 1 nos dois estados
					proxima[-w].estado[j] = 1 #Atualiza o a variavel j do novo estado para 1 
				j += 1
			proxima.pop(0)
		return proxima

	def apagarNos(self, w, proxima):
		proxima = sorted(proxima, key = attrgetter('custo'))	#Ordena a camada de acordo com o custo decrescente
		while w < len(proxima):
			proxima.pop()
		return proxima

	#Retorna a solução do diagrama relaxado para o problema do conjunto dominante minimo 
	def encontrarNoRelaxado(self, w, instancia):
		gf = grafo.Grafo(instancia)
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
			if w < len(self.proxima):
				self.proxima = self.unirNos(w, self.proxima)
			self.anterior = self.proxima #anterior recebe uma copia de proxima
			self.proxima = []#Limpa proxima antes de passar para próxima camada
		return self.anterior

	def encontrarNoRestritoMaxW(self, w, instancia):
		gf = grafo.Grafo(instancia)
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
			if len(self.proxima) > w:
				self.proxima = self.apagarNos(w, self.proxima)
			self.anterior = self.proxima #anterior recebe uma copia de proxima
			self.proxima = [] #Limpa proxima antes de passar para próxima camada
		return self.anterior