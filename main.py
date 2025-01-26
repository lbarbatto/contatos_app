from controller.contato_controller import ContatoController

# Função para iniciar a aplicação e servir como menu principal
def main():
    """
    Função que exibe o menu principal da aplicação, permitindo ao usuário
    realizar as operações de criação, edição, deleção e listagem de contatos.
    O loop continua até o usuário escolher a opção de sair.
    """
    print("="*50)  # Exibe uma linha de separação
    while True:
        # Exibe o menu de opções para o usuário
        print("=========   M E N U  P R I N C I P A L   =========")
        print("'C' - Para Criar Novo Contato")
        print("'R' - Para Listar Contato")
        print("'U' - Para Editar Contato")
        print("'D' - Para Deletar Contato")
        print("'X' - Para Sair da Aplicação")

        menu = ""
        while menu == "":
            # Solicita que o usuário escolha uma opção válida
            menu = str(input("Digite uma LETRA válida ('C','R','U','D','X'): ")).upper()

            if menu == "C":
                # Solicita os dados do novo contato
                contato_nome = input("Digite o nome: ")
                contato_phone = input("Digite o phone: ")
                contato_email = input("Digite o email: ")

                # Chama o método para criar o novo contato
                controller.criar_contato(contato_nome, contato_phone, contato_email)

            elif menu == "R":
                # Exibe todos os contatos cadastrados
                controller.listar_contatos()

            elif menu == "U":
                # Solicita o ID do contato a ser editado
                contato_id = int(input("Para editar um contato, digite o ID: "))
                
                # Tenta listar o contato com o ID fornecido
                contato = controller.listar_contato_por_id(contato_id)
                
                if contato:
                    # Exibe os dados atuais do contato
                    print(f"Nome atual: {contato.name}")
                    contato_nome = input("Novo nome (deixe em branco para manter): ")
                    contato_phone = input("Novo telefone (deixe em branco para manter): ")
                    contato_email = input("Novo e-mail (deixe em branco para manter): ")

                    # Se o usuário não digitar nada, mantém os valores antigos
                    contato_nome = contato_nome if contato_nome else contato.name
                    contato_phone = contato_phone if contato_phone else contato.phone
                    contato_email = contato_email if contato_email else contato.email

                    # Chama o método para editar o contato com os novos dados
                    controller.editar_contato(contato_id, contato_nome, contato_phone, contato_email)
                else:
                    print("Contato não encontrado.")

            elif menu == "D":
                # Solicita o ID do contato a ser deletado
                contato_id = int(input("Para deletar um contato, digite um ID válido: "))
                
                # Chama o método para deletar o contato com o ID fornecido
                controller.deletar_contato(contato_id)

            elif menu == "X":
                # Exibe uma mensagem de saída e encerra o programa
                print("Saindo da aplicação...")
                return  # Encerra o loop principal e sai do programa

            else:
                # Caso o usuário digite uma opção inválida, repete a solicitação
                menu = ""

# Verifica se o script está sendo executado diretamente e chama a função main
if __name__ == "__main__":
    controller = ContatoController()  # Instancia o controlador de contatos
    main()  # Inicia a aplicação
