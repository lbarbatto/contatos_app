

class Contato:
    """
    Classe responsável por representar um contato, com informações como nome, telefone e e-mail.
    A classe armazena um ID único, que é atribuído automaticamente quando o contato é criado.
    """
    
    def __init__(self, name, phone, email):
        """
        Inicializa um novo objeto de contato com os parâmetros fornecidos.
        
        Args:
            name (str): Nome do contato.
            phone (str): Número de telefone do contato.
            email (str): E-mail do contato.
        """
        self.id = 0  # O ID será atribuído externamente, quando o contato for salvo em um repositório.
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        """
        Define como o objeto Contato será representado como string quando for impresso.
        
        Returns:
            str: A representação em string do contato, com ID, nome, telefone e e-mail.
        """
        return f"ID: {self.id} | Nome: {self.name} | Telefone: {self.phone} | Email: {self.email}"

