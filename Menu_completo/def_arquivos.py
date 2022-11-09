#formatação do cabeçalho de opções
def padrao(texto):
	print('-'*50)
	print(f'{texto}'.center(50))

#verifica se existe o arquivo onde os registros vão ser salvos
def arquivoexiste(arq):
	try:
		arquivo = open(arq,'r')
		arquivo.close()
	except FileNotFoundError:
		print('Arquivo não encontrado!')
		arquivo = open(arq,'a+')
		print('Arquivo criado')
		arquivo.close()
