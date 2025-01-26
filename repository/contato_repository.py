from model.contato import Contato

class ContatoRepository:
    """
    Classe responsável pela persistência dos contatos. 
    Essa classe mantém um dicionário em memória para armazenar e manipular os contatos.
    """

    contatos_dictionary = {}

    def __init__(self):
        """
        Inicializa o repositório de contatos. Neste caso, o repositório é armazenado em memória.
        """
        pass

    def criar_contato(self, contato: Contato):
        """
        Cria um novo contato e o adiciona ao repositório de contatos.
        
        Args:
            contato (Contato): Instância da classe Contato contendo as informações do novo contato.
        """
        # Gerar um novo ID para o contato
        novo_id = max(self.contatos_dictionary.keys(), default=0) + 1
        contato.id = novo_id  # Atribui o ID gerado ao contato
        self.contatos_dictionary[contato.id] = contato  # Adiciona o contato ao dicionário
        print(f"Novo Contato {contato.name} criado com sucesso.")

    def listar_contatos(self):
        """
        Lista todos os contatos armazenados no repositório.
        Caso não haja contatos, imprime uma mensagem informando.
        """
        if not self.contatos_dictionary:
            print("Nenhum contato cadastrado.")
            return
        
        print("\nLista de Contatos:")
        for contato in self.contatos_dictionary.values():
            # Exibe os dados do contato. Pode ser melhorado para mostrar dados formatados.
            print(contato)

    def listar_contato_por_id(self, id):
        """
        Busca um contato específico pelo ID.
        
        Args:
            id (int): O ID do contato que se deseja buscar.
        
        Returns:
            Contato: O contato encontrado, ou None caso o contato não exista.
        """
        if id in self.contatos_dictionary:
            print(f"Contato {self.contatos_dictionary[id]} foi encontrado.")
            return self.contatos_dictionary[id]
        else:
            print("Nenhum contato encontrado com este ID.")
            return None

    def editar_contato(self, id, contato: Contato):
        """
        Edita um contato existente no repositório, substituindo seus dados pelo novo contato.
        
        Args:
            id (int): O ID do contato a ser editado.
            contato (Contato): O novo objeto de contato com as informações atualizadas.
        """
        if id in self.contatos_dictionary:
            self.contatos_dictionary[id] = contato  # Atualiza o contato no repositório
            print(f"Contato {contato.name} atualizado com sucesso.")
        else:
            print("ID não encontrado.")

    def deletar_contato(self, id):
        """
        Deleta um contato do repositório usando o ID fornecido.
        
        Args:
            id (int): O ID do contato a ser deletado.
        """
        if id in self.contatos_dictionary:
            contato_deletado = self.contatos_dictionary.pop(id)  # Remove o contato
            print(f"Contato {contato_deletado.name} removido com sucesso.")
        else:
            print("ID não encontrado.")

    