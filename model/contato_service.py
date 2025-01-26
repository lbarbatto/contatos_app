from model.contato import Contato
from repository.contato_repository import ContatoRepository

class ContatoService:
    """
    Classe responsável pela lógica de negócios relacionada aos contatos. 
    Interage com o repositório de contatos para criar, listar, editar e deletar contatos.
    """
    
    def __init__(self):
        """
        Inicializa o serviço de contatos, instanciando o repositório de contatos.
        """
        self.repository = ContatoRepository()

    def criar_contato(self, name, phone, email):
        """
        Cria um novo contato e o envia para o repositório para ser salvo.
        
        Args:
            name (str): Nome do contato.
            phone (str): Número de telefone do contato.
            email (str): Endereço de e-mail do contato.
        """
        # Cria uma instância de Contato
        contato = Contato(name, phone, email)
        # Envia o contato para ser salvo no repositório
        self.repository.criar_contato(contato)

    def listar_contatos(self):
        """
        Solicita ao repositório a lista de todos os contatos cadastrados e os exibe.
        """
        self.repository.listar_contatos()

    def listar_contato_por_id(self, id):
        """
        Busca um contato específico pelo ID no repositório.
        
        Args:
            id (int): ID do contato a ser buscado.
        
        Returns:
            Contato: O contato encontrado com o ID especificado, ou None se não encontrado.
        """
        # Solicita ao repositório o contato pelo ID
        contato_para_editar = self.repository.listar_contato_por_id(id)
        return contato_para_editar

    def editar_contato(self, id, name, phone, email):
        """
        Edita um contato existente. Atualiza os dados do contato e o envia para o repositório.
        
        Args:
            id (int): ID do contato a ser editado.
            name (str): Novo nome do contato.
            phone (str): Novo número de telefone do contato.
            email (str): Novo endereço de e-mail do contato.
        """
        # Cria uma instância de Contato com as novas informações
        contato = Contato(name, phone, email)
        # Atribui o ID do contato a ser editado
        contato.id = id        
        # Envia o contato editado para o repositório
        self.repository.editar_contato(id, contato)

    def deletar_contato(self, id):
        """
        Deleta um contato específico pelo ID no repositório.
        
        Args:
            id (int): ID do contato a ser deletado.
        """
        # Solicita ao repositório que deleta o contato com o ID especificado
        self.repository.deletar_contato(id)

