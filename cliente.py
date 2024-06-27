import re
import pymongo
import requests

class Cliente:
    def __init__(self, nome, telefone, endereco, metodo_pagamento, email, cpf, carro_alugado=None):
        self.nome = nome
        self.telefone = self.validar_telefone(telefone)
        self.endereco = endereco
        self.metodo_pagamento = metodo_pagamento
        self.email = email
        self.cpf = self.validar_cpf(cpf)
        self.carro_alugado = carro_alugado

    @staticmethod
    def validar_telefone(telefone):
        if re.match(r'^\d{11}$', telefone):
            return telefone
        else:
            raise ValueError("Telefone inválido. Deve conter 11 dígitos.")

    @staticmethod
    def validar_cpf(cpf):
        # Adicione aqui a lógica de validação de CPF
        if re.match(r'^\d{11}$', cpf):  # Simplificação para exemplo, adicione validação correta
            return cpf
        else:
            raise ValueError("CPF inválido. Deve conter 11 dígitos.")

    def cadastrar_cliente(self, db):
        novo_cliente = {
            "nome": self.nome,
            "telefone": self.telefone,
            "endereco": self.endereco,
            "metodo_pagamento": self.metodo_pagamento,
            "email": self.email,
            "cpf": self.cpf,
            "carro_alugado": self.carro_alugado
        }
        db.clientes.insert_one(novo_cliente)
        print(f"Cliente {self.nome} cadastrado com sucesso!")

    @staticmethod
    def listar_clientes(db):
        return db.clientes.find()

    @staticmethod
    def atualizar_cliente(db, cpf, dados_atualizados):
        db.clientes.update_one({"cpf": cpf}, {"$set": dados_atualizados})

    @staticmethod
    def remover_cliente(db, cpf):
        db.clientes.delete_one({"cpf": cpf})


def buscar_endereco_por_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            endereco = data.get('logradouro') or ''
            bairro = data.get('bairro') or ''
            cidade = data.get('localidade') or ''
            uf = data.get('uf') or ''
            return f"{endereco}, {bairro}, {cidade} - {uf}"
        else:
            print(f"Erro ao consultar CEP: {response.status_code}")
            return ""
    except Exception as e:
        print(f"Erro na consulta do CEP: {str(e)}")
        return ""
