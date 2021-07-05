from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()
listaDeNos = cdm.encontrarNoOtimo()

print("Custo:", listaDeNos[0].custo, "\n")
print("Conjuntos solucao otimo:")
for t in listaDeNos:
	print(t.solParcial)