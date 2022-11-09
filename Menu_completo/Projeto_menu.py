from def_arquivos import arquivoexiste, padrao

arq = 'pessoas_cadastradas.txt'
#Menu onde são mostradas as opções para o usuário
def MenuPrincipal():
	padrao('MENU PRINCIPAL')
	print('-'*50)
	print('''
1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do Sistema
	''')
	print('-'*50)

	while True:
		opcao = str(input('Qual a sua opção? '))
		#Opção que mostra pessoas que ja foram cadastradas
		if opcao == '1':
			opcao1()
		#Opção para cadastrarmais pessoas
		elif opcao == '2':
			while True:
				opcao2()
				continuar_cadastrando = input('Quer cadastrar mais alguém? [S/N]').strip().lower()
				if continuar_cadastrando in 'n':
					break
		#opção de encerramento do programa
		elif opcao == '3':
			print('Encerrando o programa...\nVolte Sempre!')
			break
		else:
			#Validação relacionada a entrada de dados numericos ou alfanum no input de opção
			if opcao.isnumeric():
				print('Escolha uma das opções válidas! 1, 2 ou 3!')
			else:
				print('Por favor, digite um número inteiro válido!')

#leitura de arquivo onde se encontram as pessoas já registradas
def opcao1():
	padrao('OPÇÃO 1')
	arquivoexiste(arq)
	arquivo = open(arq,'r')
	print(arquivo.read())
	arquivo.close()
#Adicionar registros a lista
def opcao2():
	padrao('OPÇÃO 2')
	arquivoexiste(arq)
	arquivo = open(arq,'a+')
	cadastro = str(input('Qual o nome da pessoa a ser cadastrada? '))
	arquivo.write(cadastro)
	arquivo.write('\n')
	print(arquivo.read())
	arquivo.close()


MenuPrincipal()
