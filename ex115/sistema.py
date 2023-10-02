from lib.interface import *
from lib.arquivo import *

arq = 'pessoas.txt'
if not arqexiste(arq):
    criararquivo(arq)
    
while True:
    lista = ['Ver pessoas cadastradas', 'Cadastrar pessoa nova', 'Sair do sistema']
    menu(lista)
    opc = leiaInt('Sua opção: ') 
    match opc: 
        case 1:
            cabecalho('PESSOAS CADASTRADAS')
            lerarquivo(arq)
        case 2:
            cabecalho('CADASTRO')
            nome = str(input('Nome: '))
            idade = leiaInt('Idade: ')
            cadastrar(arq, nome, idade)
        case 3:
            cabecalho('SAINDO DO SISTEMA...')
            break
        case _:
            print("OPÇÃO INVALIDADA!")
            