from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()
t = cdm.encontrarNoOtimo()
print(t.custo)
print(t.solParcial)
