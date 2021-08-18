from classes import conjuntoDominanteMinimo as CDM

cdm = CDM.DDconjuntoDominanteMinimo()
instancias = ['instancia1', 'instancia2', 'instancia3', 'instancia4']

while True:
	number = 1

	metodo = int(input('Olá! Digite o número do método a ser realizado: \n1 - Diagrama Relaxado \n2 - Diagrama Restrito \n3 - Diagrama Exato\n Opção: '))
 
	while metodo != 1 and metodo != 2 and metodo != 3:
		number = int(input('Número de instância invalido. Digite um número dentre as opções ou digite 0 (zero) para encerrar o programa \n Opção: '))
		if number == 0:
			break
	
	if number == 0:
		break
 
	numero_instancia = int(input('Digite o número da Instância a ser utilizada para o método: \n1 - Instância de tamanho 6 \n2 - Instância de tamanho 7 \n3 - Instância de tamanho 300\n4 - Instância de tamanho 9\nOpção: '))
 
	while numero_instancia != 1 and numero_instancia != 2 and numero_instancia != 3 and numero_instancia != 4:
		number = int(input('Número de instância invalido. Digite um número dentre as opções ou digite 0 (zero) para encerrar o programa \n Opção: '))
		if number == 0:
			break
		numero_instancia = number

	if number == 0:
		break
  
	if metodo == 1 or metodo == 2:
		largura_diagrama = int(input('Digite a largura do diagrama: '))
  
	if metodo == 1:
		listaDeNos = cdm.encontrarNoRelaxado(largura_diagrama, instancias[numero_instancia-1])
		print("Custo:", listaDeNos[0].custo, "\n")
		print("Conjuntos solução do diagrama relaxado:")
		for t in listaDeNos:
			print(t.solParcial)
	if metodo == 2:
		listaDeNos = cdm.encontrarNoRestritoMaxW(largura_diagrama, instancias[numero_instancia-1])
		print("Custo:", listaDeNos[0].custo, "\n")
		print("Conjuntos solução do diagrama restrito:")
		for t in listaDeNos:
			print(t.solParcial)
	if metodo == 3:
		listaDeNos = cdm.encontrarNoOtimo(instancias[numero_instancia-1])
		print("Custo:", listaDeNos[0].custo, "\n")
		print("Conjuntos solução do diagrama restrito:")
		for t in listaDeNos:
			print(t.solParcial)
	else:
		print('Opção inválida.')
  
	opcao = input('Deseja terminar o programa? (s/n): ')
  
	if opcao == 's':
		break
	
      

# Instruções para rodar o código:
# Instalar a biblioteca "numpy" EM "Ferramentas" -> "Gerenciar Pacotes" ->
# -> digitar "numpy" no campo de testo e clicar em pesquisar ->
# clicar na primeira versão e depois em "instalar"
