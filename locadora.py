import pymongo

class Veiculo:
    def __init__(self, marca, modelo, ano, disponivel=True, locador=None):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = disponivel
        self.locador = locador  # Adiciona um campo para armazenar o locador do veículo

    def __str__(self):
        disponibilidade = "disponível" if self.disponivel else "alugado"
        locador_info = f" (Locado por: {self.locador})" if not self.disponivel else ""
        return f"{self.marca} {self.modelo} ({self.ano}) - {disponibilidade}{locador_info}"

class Locadora:
    def __init__(self, db):
        self.db = db

    def adicionar_veiculo(self, veiculo):
        novo_veiculo = {
            "marca": veiculo.marca,
            "modelo": veiculo.modelo,
            "ano": veiculo.ano,
            "disponivel": veiculo.disponivel,
            "locador": veiculo.locador  # Adiciona o locador do veículo ao documento
        }
        self.db.veiculos.insert_one(novo_veiculo)

    def mostrar_veiculos(self):
        return self.db.veiculos.find()

    def alugar_veiculo(self, marca, modelo, locador_nome, locador_cpf):
        veiculo = self.db.veiculos.find_one({"marca": marca, "modelo": modelo, "disponivel": True})
        if veiculo:
            self.db.veiculos.update_one(
                {"_id": veiculo["_id"]},
                {"$set": {"disponivel": False, "locador": f"{locador_nome} (CPF: {locador_cpf})"}}
            )
            self.db.clientes.update_one(
                {"cpf": locador_cpf},
                {"$set": {"carro_alugado": f"{veiculo['marca']} {veiculo['modelo']} ({veiculo['ano']})"}}
            )
            print(f"Você alugou o veículo {marca} {modelo}")
        else:
            print(f"Desculpe, o veículo {marca} {modelo} não está disponível para locação.")
