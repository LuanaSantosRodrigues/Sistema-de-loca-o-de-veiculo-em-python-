import pymongo
from menu import Menu
from locadora import Locadora

def main():
    # Conectar ao MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["locadora_db"]

    # Criar coleções (se ainda não existirem)
    if "clientes" not in db.list_collection_names():
        db.create_collection("clientes")
    if "veiculos" not in db.list_collection_names():
        db.create_collection("veiculos")

    locadora = Locadora(db)

    while True:
        Menu(locadora, db)
        if input("Deseja encerrar? (S/N): ").upper() == 'S':
            break

if __name__ == "__main__":
    main()
