from model.contato_service import ContatoService

class ContatoController:
    """
    Classe responsável por gerenciar as interações entre a aplicação e o serviço de contatos.
    Serve como intermediário entre o usuário e os métodos de negócios, fornecendo operações
    como criar, listar, editar e deletar contatos.
    """
    
    def __init__(self):
        """
        Inicializa o controlador de contatos, instanciando o serviço de contatos.
        """
        self.service = ContatoService()

    def criar_contato(self, name, phone, email):
        """
        Cria um novo contato utilizando o serviço de contatos.
        
        Args:
            name (str): Nome do contato.
            phone (str): Número de telefone do contato.
            email (str): Endereço de e-mail do contato.
        """
        self.service.criar_contato(name, phone, email)

    def listar_contatos(self):
        """
        Lista todos os contatos cadastrados através do serviço de contatos.
        """
        self.service.listar_contatos()

    def listar_contato_por_id(self, id):
        """
        Busca e retorna um contato específico pelo ID utilizando o serviço de contatos.
        
        Args:
            id (int): ID do contato a ser buscado.
        
        Returns:
            Contato: O contato com o ID especificado, se encontrado.
        """
        return self.service.listar_contato_por_id(id)

    def editar_contato(self, id, name, phone, email):
        """
        Edita um contato existente, alterando seus dados através do serviço de contatos.
        
        Args:
            id (int): ID do contato a ser editado.
            name (str): Novo nome do contato.
            phone (str): Novo número de telefone do contato.
            email (str): Novo endereço de e-mail do contato.
        """
        self.service.editar_contato(id, name, phone, email)

    def deletar_contato(self, id):
        """
        Deleta um contato existente pelo ID utilizando o serviço de contatos.
        
        Args:
            id (int): ID do contato a ser deletado.
        """
        self.service.deletar_contato(id)
