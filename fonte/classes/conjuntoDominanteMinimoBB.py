from classes import conjuntoDominanteMinimo as CDM
from classes import grafo


class BBconjuntoDominanteMinimo:
	def __init__(self):
		self.Q = []


	#Retorna a solução ótima utilizando Bracnh and Bound dos diagramas de decisão
	def encontrarNoOtimoBB(self, largura_diagrama, instancia):
		cdm = CDM.DDconjuntoDominanteMinimo() #Cria um objeto do diagrama de decisão
		cdm.gf = grafo.Grafo(instancia) #Carrega a intancia e cria um grafo dele
		self.Q = [cdm.criarRaiz()] #Adiciona a raiz inicial ao vetor de raizes
		solução = cdm.criarRaiz() #Cria um no pra solução inicial
		solução.custo = 10000000000000000000000 #O custo da solução inicial recebe um valor grande
		while len(self.Q) > 0: #Percorre até que o vetor esteja vazio
			restrito = cdm.encontrarNoRestritoCutSet(largura_diagrama, self.Q[0], self.Q[0].camada)	
			if(solução.custo > restrito[0].custo): #Testa se o diagrama restrito obteve uma solução melhor, pra subtituir a atual
				solução = restrito[0]
			restrito.pop(0) #Apaga solução do diagrama restrito, e mantém apenas o CutSet
			if(len(restrito) > 0): #Se o Cuset não é vazio calcula o diagrama relaxado
				relaxado = cdm.encontrarNoRelaxado(largura_diagrama, self.Q[0], self.Q[0].camada)
				if(solução.custo > relaxado[0].custo): #Testa se o diagrama relaxado é pior que a solução atual para poda
					self.Q.extend(restrito)
			self.Q.pop(0)
		return solução

			
