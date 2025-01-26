# Gerenciador de Contatos

Este projeto implementa um gerenciador de contatos utilizando o paradigma de Programação Orientada a Objetos (POO) em Python. A aplicação permite ao usuário criar, listar, editar e deletar contatos de forma interativa via terminal.

## Estrutura do Projeto

A aplicação segue uma estrutura organizada em camadas para promover a separação de responsabilidades e facilitar a manutenção.

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

### Diretórios e Arquivos:

- \`\`: Contém a lógica de controle, recebendo comandos da interface e chamando serviços apropriados.
  - `contato_controller.py`: Classe que gerencia a comunicação entre a interface do usuário e os serviços.
- \`\`: Define as classes de domínio e os serviços relacionados aos dados.
  - `contato.py`: Classe de modelo para representar um contato.
  - `contato_service.py`: Serviço que contém a lógica de negócio.
- \`\`: Responsável pela persistência e manipulação dos dados.
  - `contato_repository.py`: Gerencia o armazenamento dos contatos.
- \`\`: Ponto de entrada da aplicação.
- \`\`: Documentação do projeto.

---

## Instalação

Para executar esta aplicação, você precisa ter o Python instalado em sua máquina. Siga as instruções abaixo para configurar o ambiente:

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/gerenciador-contatos.git
   ```

2. Acesse o diretório do projeto:

   ```bash
   cd gerenciador-contatos
   ```

3. Execute a aplicação:

   ```bash
   python main.py
   ```

---

## Funcionalidades

A aplicação oferece as seguintes funcionalidades:

1. **Criar Contato**: Adicionar um novo contato fornecendo nome, telefone e email.
2. **Listar Contatos**: Exibir todos os contatos cadastrados.
3. **Editar Contato**: Atualizar as informações de um contato existente.
4. **Deletar Contato**: Remover um contato pelo seu ID.
5. **Sair da Aplicação**: Encerrar o programa.

---

## Uso

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

## Estrutura de Classes

### Classe `Contato`

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

### Classe `ContatoService`

```python
class ContatoService:
    def __init__(self):
        self.repository = ContatoRepository()

    def criar_contato(self, name, phone, email):
        contato = Contato(name, phone, email)
        self.repository.criar_contato(contato)
```

### Classe `ContatoRepository`

```python
class ContatoRepository:
    contatos_dictionary = {}

    def criar_contato(self, contato: Contato):
        novo_id = max(self.contatos_dictionary.keys(), default=0) + 1
        contato.id = novo_id
        self.contatos_dictionary[contato.id] = contato
        print(f"Novo Contato {contato.name} criado com sucesso.")
```

---

## Contribuição

Se desejar contribuir para o projeto:

1. Faça um fork do repositório.
2. Crie uma nova branch com a sua feature:
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

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

Desenvolvido por [Seu Nome](https://github.com/lbarbatto).

