# Gerenciador de Contatos

Este projeto é uma aplicação de gerenciamento de contatos desenvolvida em Python, utilizando os princípios de **Programação Orientada a Objetos (POO)** e uma arquitetura modular baseada no padrão **MVC (Model-View-Controller)**. A aplicação oferece funcionalidades de CRUD (Create, Read, Update, Delete) para gerenciamento de contatos via interface de linha de comando.

## Arquitetura do Projeto

A estrutura do projeto foi projetada para garantir **escalabilidade**, **testabilidade** e **manutenibilidade**, separando as responsabilidades em camadas distintas.

```
.
├── controller/
│   └── contato_controller.py
├── model/
│   ├── contato.py
│   └── contato_service.py
├── repository/
│   └── contato_repository.py
├── main.py
└── README.md
```

### Camadas do Sistema:

- **Controller Layer (controller/)**: Camada de controle que atua como intermediária entre a interface de usuário e as regras de negócio.
  - `contato_controller.py`: Gerencia as requisições do usuário e coordena chamadas aos serviços.
- **Service Layer (model/)**: Responsável por encapsular a lógica de negócio.
  - `contato.py`: Definição da entidade Contato.
  - `contato_service.py`: Regras de negócio e validações aplicadas aos contatos.
- **Repository Layer (repository/)**: Camada de persistência para abstração do armazenamento dos dados.
  - `contato_repository.py`: Operações de CRUD para armazenamento em memória.
- **Interface Layer (main.py)**: Ponto de entrada da aplicação, interagindo com o usuário via CLI.

---

## Tecnologias Utilizadas

- **Python 3.x**
- **Paradigma POO (Encapsulamento, Abstração, Herança e Polimorfismo)**
- **Padrões de Projeto: MVC, Repository Pattern**
- **Boas práticas de Clean Code e SOLID**

---

## Instalação e Execução

### Pré-requisitos:
- Ter o Python instalado (>= 3.8)

### Passos para execução:

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerenciador-contatos.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd gerenciador-contatos
   ```
3. Execute o programa:
   ```bash
   python main.py
   ```

---

## Funcionalidades

- **Cadastro de Contato:** Inserção de nome, telefone e e-mail.
- **Listagem de Contatos:** Exibição de todos os contatos cadastrados.
- **Edição de Contato:** Atualização dos dados existentes de um contato.
- **Exclusão de Contato:** Remoção de um contato a partir do seu identificador único.
- **Encerramento Seguro da Aplicação.**

---

## Exemplo de Uso

Ao executar o programa, será exibido o seguinte menu interativo:

```
==================================================
=========   M E N U  P R I N C I P A L   =========
'C' - Para Criar Novo Contato
'R' - Para Listar Contato
'U' - Para Editar Contato
'D' - Para Deletar Contato
'X' - Para Sair da Aplicação
Digite uma LETRA válida ('C','R','U','D','X'):
```

---

## Estrutura de Código

### Modelo de Contato (Entidade)

```python
class Contato:
    def __init__(self, name, phone, email):
        self.id = 0
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"ID: {self.id} | Nome: {self.name} | Telefone: {self.phone} | Email: {self.email}"
```

### Serviço de Contatos

```python
from model.contato import Contato
from repository.contato_repository import ContatoRepository

class ContatoService:
    def __init__(self):
        self.repository = ContatoRepository()

    def criar_contato(self, name, phone, email):
        contato = Contato(name, phone, email)
        self.repository.criar_contato(contato)
```

### Repositório de Contatos

```python
from model.contato import Contato

class ContatoRepository:
    contatos_dictionary = {}

    def criar_contato(self, contato: Contato):
        novo_id = max(self.contatos_dictionary.keys(), default=0) + 1
        contato.id = novo_id
        self.contatos_dictionary[contato.id] = contato
        print(f"Novo Contato {contato.name} criado com sucesso.")
```

### Controller de Contatos

```python
from model.contato_service import ContatoService

class ContatoController:
    def __init__(self):
        self.service = ContatoService()

    def criar_contato(self, name, phone, email):
        self.service.criar_contato(name, phone, email)

    def listar_contatos(self):
        self.service.listar_contatos()

    def listar_contato_por_id(self, id):
        return self.service.listar_contato_por_id(id)

    def editar_contato(self, id, name, phone, email):
        self.service.editar_contato(id, name, phone, email)

    def deletar_contato(self, id):
        self.service.deletar_contato(id)
```

---

## Contribuição

Para contribuir com o projeto:

1. Faça um fork do repositório.
2. Crie uma branch com a sua feature:
   ```bash
   git checkout -b minha-feature
   ```
3. Commit suas alterações:
   ```bash
   git commit -m "Adiciona nova funcionalidade"
   ```
4. Envie para o repositório remoto:
   ```bash
   git push origin minha-feature
   ```
5. Abra um Pull Request.

---

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais informações.

---

## Autor

Desenvolvido por [Leopoldo Barbato](https://github.com/lbarbatto).

