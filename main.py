from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()
listaDeNos = cdm.encontrarNoOtimo()

print("custo:", listaDeNos[0].custo)
for t in listaDeNos:
	print(t.solParcial)