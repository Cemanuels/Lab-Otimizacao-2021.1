#Classe que represnta cada nó do DD, e guarda as informações necessárias(estado, custo, e solução parcial)
class No:
	def __init__(self, estado, custo, solParcial, camada):
		self.estado = estado
		self.custo = custo
		self.solParcial = solParcial
		self.camada = camada

