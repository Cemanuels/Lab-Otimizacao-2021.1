from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()

metodo = int(input('Olá! Digite o número do método a ser realizado: \n 1 - Diagrama Relaxado \n 2 - Diagrama Restrito \n Opção: '))

conjunto = int(input('Digite o tamanho do conjunto: '))
# listaDeNos = cdm.encontrarNoOtimo()
# print("Custo:", listaDeNos[0].custo, "\n")
# print("Conjuntos solucao otimo:")
# for t in listaDeNos:
# 	print(t.solParcial)
if metodo == 1:
	listaDeNos = cdm.encontrarNoRelaxado(conjunto)
	print("Custo:", listaDeNos[0].custo, "\n")
	print("Conjuntos solucao restrito:")
	for t in listaDeNos:
		print(t.solParcial)
elif metodo == 2:
  listaDeNos = cdm.encontrarNoRestritoMaxW(conjunto)
  print("Custo:", listaDeNos[0].custo, "\n")
  print("Conjuntos solucao restrito:")
  for t in listaDeNos:
    print(t.solParcial)


# Instruções para rodar o código:
# Instalar a biblioteca "numpy" EM "Ferramentas" -> "Gerenciar Pacotes" ->
# -> digitar "numpy" no campo de testo e clicar em pesquisar ->
# clicar na primeira versão e depois em "instalar"
