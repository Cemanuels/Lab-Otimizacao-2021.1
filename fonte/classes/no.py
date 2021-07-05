#Classe que represnta cada nó do DD, e guarda as informações necessárias(estado, custo, e solução parcial)
class No:
	def __init__(self, estado, custo, solParcial):
		self.estado = estado
		self.custo = custo
		self.solParcial = solParcial

