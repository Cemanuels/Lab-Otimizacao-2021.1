from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()
listaDeNos = cdm.encontrarNoOtimo()

print("custo:", listaDeNos[0].custo)

for t in listaDeNos:
    print(t.solParcial)

# Instruções para rodar o código:
# Instalar a biblioteca "numpy" EM "Ferramentas" -> "Gerenciar Pacotes" ->
# -> digitar "numpy" no campo de testo e clicar em pesquisar ->
# clicar na primeira versão e depois em "instalar"
