from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()

# listaDeNos = cdm.encontrarNoOtimo()
# print("Custo:", listaDeNos[0].custo, "\n")
# print("Conjuntos solucao otimo:")
# for t in listaDeNos:
# 	print(t.solParcial)


listaDeNos = cdm.encontrarNoRelaxado(10)
print("Custo:", listaDeNos[0].custo, "\n")
print("Conjuntos solucao restrito:")
for t in listaDeNos:
	print(t.solParcial)


# Instruções para rodar o código:
# Instalar a biblioteca "numpy" EM "Ferramentas" -> "Gerenciar Pacotes" ->
# -> digitar "numpy" no campo de testo e clicar em pesquisar ->
# clicar na primeira versão e depois em "instalar"