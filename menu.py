import os
import re
import requests
from locadora import Locadora, Veiculo
from cliente import Cliente, buscar_endereco_por_cep

def Menu(locadora, db):
    TelaDoMenu()
    
    opc = input('Digite a opção desejada: ')
    if opc.isnumeric():
        if opc == '1':
            nome = input("Digite o nome do cliente: ")
            telefone = input("Digite o telefone do cliente: ")
            cep = input("Digite o CEP do cliente: ")
            numero_residencia = input("Digite o número da residência: ")
            endereco_completo = buscar_endereco_por_cep(cep)
            metodo_pagamento = input("Digite o método de pagamento do cliente: ")
            email = input("Digite o e-mail do cliente: ")
            cpf = input("Digite o CPF do cliente: ")
            try:
                cliente = Cliente(nome, telefone, endereco_completo, metodo_pagamento, email, cpf)
                cliente.cadastrar_cliente(db)
            except ValueError as e:
                print(e)
        elif opc == '2':
            print("Clientes cadastrados:")
            for cliente in Cliente.listar_clientes(db):
                print(cliente)
        elif opc == '3':
            marca = input("Digite a marca do veículo: ")
            modelo = input("Digite o modelo do veículo: ")
            ano = input("Digite o ano do veículo: ")
            veiculo = Veiculo(marca, modelo, ano)
            locadora.adicionar_veiculo(veiculo)
            print("Veículo cadastrado com sucesso!")
        elif opc == '4':
            print("Veículos cadastrados:")
            for veiculo in locadora.mostrar_veiculos():
                print(veiculo)
        elif opc == '5':
            marca = input("Digite a marca do veículo que deseja alugar: ")
            modelo = input("Digite o modelo do veículo que deseja alugar: ")
            locador_nome = input("Digite seu nome: ")
            locador_cpf = input("Digite seu CPF: ")
            locadora.alugar_veiculo(marca, modelo, locador_nome, locador_cpf)
        elif opc == '6':
            cpf = input("Digite o CPF do cliente que deseja atualizar: ")
            print("Digite os novos dados do cliente (deixe em branco para manter o valor atual):")
            nome = input("Novo nome: ")
            telefone = input("Novo telefone: ")
            cep = input("Digite o novo CEP do cliente: ")
            numero_residencia = input("Digite o novo número da residência: ")
            endereco_completo = buscar_endereco_por_cep(cep)
            metodo_pagamento = input("Novo método de pagamento: ")
            email = input("Novo e-mail: ")
            dados_atualizados = {}
            if nome: dados_atualizados["nome"] = nome
            if telefone: dados_atualizados["telefone"] = Cliente.validar_telefone(telefone)
            if endereco_completo: dados_atualizados["endereco"] = endereco_completo
            if metodo_pagamento: dados_atualizados["metodo_pagamento"] = metodo_pagamento
            if email: dados_atualizados["email"] = email
            Cliente.atualizar_cliente(db, cpf, dados_atualizados)
            print("Cliente atualizado com sucesso!")
        elif opc == '7':
            cpf = input("Digite o CPF do cliente que deseja remover: ")
            Cliente.remover_cliente(db, cpf)
            print("Cliente removido com sucesso!")
        elif opc == '8':
            print('Encerrando...')
        else:
            print('Opção inexistente!.')
    else:
        print('Apenas números')

def TelaDoMenu():
    input('Para entrar no Menu pressione enter.')
    os.system('cls' if os.name == 'nt' else 'clear')
    print()
    print('Digite a opção desejada')
    print()
    print('1 - Cadastrar Cliente:')
    print('2 - Listar Clientes:')
    print('3 - Adicionar Veículo:')
    print('4 - Listar Veículos:')
    print('5 - Alugar Veículo:')
    print('6 - Atualizar Cliente:')
    print('7 - Remover Cliente:')
    print('8 - Encerrar')