class Veiculo:
    def __init__(self, marca, modelo, ano, disponivel=True):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.disponivel = disponivel

    def __str__(self):
        disponibilidade = "disponível" if self.disponivel else "alugado"
        return f"{self.marca} {self.modelo} ({self.ano}) - {disponibilidade}"
