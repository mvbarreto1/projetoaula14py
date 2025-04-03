class Cliente:
    def __init__(self, id: int, nome: str, email: str, telefone: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.telefone = telefone


class Quarto:
    def __init__(self, numero: int, tipo: str, preco: float, status_disponibilidade: bool):
        self.numero = numero
        self.tipo = tipo  # pode ser 'single', 'double', 'suite'
        self.preco = preco
        self.status_disponibilidade = status_disponibilidade


class Reserva:
    def __init__(self, cliente: Cliente, quarto: Quarto, data_checkin: str, data_checkout: str, status: str):
        self.cliente = cliente
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = status  # pode ser 'confirmada', 'cancelada', 'pendente'


class GerenciadorDeReservas:
    def __init__(self, nome: str):
        self.nome = nome
        self.lista_clientes = []
        self.lista_quartos = []
        self.lista_reservas = []
        self.id_cliente = 1
        self.id_reserva = 1

    def cadastrarCliente(self, nome: str, email: str, telefone: str):
        cliente = Cliente(self.id_cliente, nome, email, telefone)
        self.lista_clientes.append(cliente)
        self.id_cliente += 1
        print(f"Cliente {nome} cadastrado com sucesso!")

    def verTodosClientes(self):
        for cliente in self.lista_clientes:
            print(f"ID: {cliente.id}, Nome: {cliente.nome}, Email: {cliente.email}, Telefone: {cliente.telefone}")

    def editarCliente(self, id_cliente: int, nome: str, email: str, telefone: str):
        for cliente in self.lista_clientes:
            if cliente.id == id_cliente:
                cliente.nome = nome
                cliente.email = email
                cliente.telefone = telefone
                print(f"Cliente {id_cliente} atualizado com sucesso!")

    def excluirCliente(self, id_cliente: int):
        self.lista_clientes = [cliente for cliente in self.lista_clientes if cliente.id != id_cliente]
        print(f"Cliente {id_cliente} excluído com sucesso!")

    def cadastrarQuarto(self, numero: int, tipo: str, preco: float):
        quarto = Quarto(numero, tipo, preco, True)
        self.lista_quartos.append(quarto)
        print(f"Quarto {numero} cadastrado com sucesso!")

    def verTodosQuartos(self):
        for quarto in self.lista_quartos:
            print(f"Quarto {quarto.numero}, Tipo: {quarto.tipo}, Preço por diária: R${quarto.preco}, Disponível: {quarto.status_disponibilidade}")

    def verificarDisponibilidade(self, tipo: str, data_checkin: str, data_checkout: str):
        # Verifica disponibilidade do quarto com base no tipo
        for quarto in self.lista_quartos:
            if quarto.tipo == tipo and quarto.status_disponibilidade:
                return quarto
        return None

    def realizarReserva(self, id_cliente: int, tipo_quarto: str, data_checkin: str, data_checkout: str):
        cliente = next((cliente for cliente in self.lista_clientes if cliente.id == id_cliente), None)
        if cliente:
            quarto = self.verificarDisponibilidade(tipo_quarto, data_checkin, data_checkout)
            if quarto:
                reserva = Reserva(cliente, quarto, data_checkin, data_checkout, 'confirmada')
                self.lista_reservas.append(reserva)
                quarto.status_disponibilidade = False
                print(f"Reserva realizada com sucesso para {cliente.nome} no quarto {quarto.numero}")
            else:
                print("Não há quartos disponíveis no tipo solicitado.")
        else:
            print("Cliente não encontrado.")

    def cancelarReserva(self, id_reserva: int):
        for reserva in self.lista_reservas:
            if reserva.id_reserva == id_reserva:
                reserva.quarto.status_disponibilidade = True
                self.lista_reservas.remove(reserva)
                print(f"Reserva {id_reserva} cancelada com sucesso!")
                break

    def listarReservas(self):
        for reserva in self.lista_reservas:
            print(f"Reserva ID: {reserva.id_reserva}, Cliente: {reserva.cliente.nome}, Quarto: {reserva.quarto.numero}, "
                  f"Check-in: {reserva.data_checkin}, Check-out: {reserva.data_checkout}, Status: {reserva.status}")


# Exemplo de uso do sistema
hotel = GerenciadorDeReservas(nome="Refúgio dos Sonhos")

while True:
    menu = input("""
        Escolha uma opção:
        1 - Gestão de Clientes
        2 - Gestão de Quartos
        3 - Gestão de Reservas
        0 - Sair
    """)
    match menu:
        case "1":
            submenu_clientes = input("""
            Escolha uma opção:
            1 - Adicionar Cliente
            2 - Ver todos os Clientes
            3 - Editar Cliente
            4 - Excluir Cliente
            0 - Voltar
            """)
            match submenu_clientes:
                case "1":
                    nome = input("Digite o nome do cliente: ")
                    email = input("Digite o email do cliente: ")
                    telefone = input("Digite o telefone do cliente: ")
                    hotel.cadastrarCliente(nome, email, telefone)
                case "2":
                    hotel.verTodosClientes()
                case "3":
                    id_cliente = int(input("Digite o ID do cliente: "))
                    nome = input("Digite o novo nome: ")
                    email = input("Digite o novo email: ")
                    telefone = input("Digite o novo telefone: ")
                    hotel.editarCliente(id_cliente, nome, email, telefone)
                case "4":
                    id_cliente = int(input("Digite o ID do cliente a ser excluído: "))
                    hotel.excluirCliente(id_cliente)
                case "0":
                    break
                case _:
                    print("Opção inválida")

        case "2":
            submenu_quartos = input("""
            Escolha uma opção:
            1 - Adicionar Quarto
            2 - Ver todos os Quartos
            0 - Voltar
            """)
            match submenu_quartos:
                case "1":
                    numero = int(input("Digite o número do quarto: "))
                    tipo = input("Digite o tipo do quarto (single, double, suite): ")
                    preco = float(input("Digite o preço por diária do quarto: "))
                    hotel.cadastrarQuarto(numero, tipo, preco)
                case "2":
                    hotel.verTodosQuartos()
                case "0":
                    break
                case _:
                    print("Opção inválida")

        case "3":
            submenu_reservas = input("""
            Escolha uma opção:
            1 - Realizar Reserva
            2 - Ver todas as Reservas
            3 - Cancelar Reserva
            0 - Voltar
            """)
            match submenu_reservas:
                case "1":
                    id_cliente = int(input("Digite o ID do cliente: "))
                    tipo_quarto = input("Digite o tipo de quarto desejado (single, double, suite): ")
                    data_checkin = input("Digite a data de check-in (dd/mm/aaaa): ")
                    data_checkout = input("Digite a data de check-out (dd/mm/aaaa): ")
                    hotel.realizarReserva(id_cliente, tipo_quarto, data_checkin, data_checkout)
                case "2":
                    hotel.listarReservas()
                case "3":
                    id_reserva = int(input("Digite o ID da reserva a ser cancelada: "))
                    hotel.cancelarReserva(id_reserva)
                case "0":
                    break
                case _:
                    print("Opção inválida")

        case "0":
            print("Saindo...")
            break

        case _:
            print("Opção inválida")
