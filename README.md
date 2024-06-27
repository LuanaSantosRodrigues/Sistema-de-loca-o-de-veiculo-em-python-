# Sistema de Gerenciamento de Locação de Veículos

## Descrição
Este projeto é um sistema de gerenciamento de locação de veículos, desenvolvido em Python com uma interface de linha de comando. Ele permite cadastrar clientes e veículos, alugar veículos, atualizar e remover informações de clientes e veículos, e listar registros. Os dados são armazenados em um banco de dados MongoDB, garantindo a persistência das informações e facilitando a integração com outras aplicações. O sistema inclui validações para CPF e telefone, assegurando a integridade dos dados fornecidos pelos usuários.

## Funcionalidades
- Cadastrar clientes com validação de CPF e telefone.
- Listar clientes cadastrados.
- Adicionar veículos ao inventário.
- Listar veículos disponíveis e alugados.
- Alugar veículos para clientes.
- Atualizar informações dos clientes.
- Remover clientes do sistema.

## Requisitos
- Python 3.8+
- MongoDB

## Configuração do Ambiente Virtual

1. Criação do Ambiente Virtual:
    ```sh
    python -m venv env
    ```

2. Ativação do Ambiente Virtual:
    - No Windows:
      ```sh
      .\env\Scripts\activate
      ```
    - No MacOS/Linux:
      ```sh
      source env/bin/activate
      ```

3. Instalação das Dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Estrutura do Projeto

- `cliente.py`: Define a classe Cliente e suas operações.
- `locadora.py`: Define a classe Veiculo e Locadora com suas operações.
- `menu.py`: Implementa o menu de interação com o usuário.
- `main.py`: Ponto de entrada do aplicativo.

## Execução do Projeto

1. Certifique-se de que o MongoDB está em execução localmente ou configure a URL de conexão apropriada.
2. Ative o ambiente virtual:
    - No Windows:
      ```sh
      .\env\Scripts\activate
      ```
    - No MacOS/Linux:
      ```sh
      source env/bin/activate
      ```
3. Execute o projeto:
    ```sh
    python main.py
    ```

## Autores
- [Luana Rodrigues](https://github.com/LuanaSantosRodrigues)
