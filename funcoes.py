
def displayMenu():
    print("=== Planejador de Eventos do Campus ===\n" \
    "1. Adicionar Evento\n" \
    "2. Ver Todos os Eventos\n" \
    "3. Filtrar por Categoria\n" \
    "4. Marcar Evento como Participado\n" \
    "5. Gerar Relatório\n" \
    "6. Sair")

def getEscolhaDoUsuario(): # op = opção
    op = (input("Escolha uma opção: "))
    if op.isnumeric():
        op = int(op)
        return op
    else:
        print("Opção inexistente, tente novamente!")

def filtrarEventosPorCategoria(listaEventos, categoria):

    return

#def marcarEventoAtendido(listaEventos, id):


    #return


#def gerarRelatorio(listaEventos):
    
    #return 

displayMenu()
listaEventos = []
op = 0
while op != 6:

    op = getEscolhaDoUsuario()


    if op == 1:
        nome = input("Nome do Evento: ")
        data = input("Data (AAAA=MM=DD): ")
        local = input("Local: ")
        categoria = input("Categoria: ")
            
        #adicionarEvento(listaEventos, nome, data, local, categoria)
        print("\nEvento adicionado com sucesso!")

    #elif op == 2:
    #listarEventos(listaEventos)

    elif op == 3:
        categoria = input("Digite a categoria de eventos que deseja filtrar: ")
        filtrarEventosPorCategoria(listaEventos, categoria)

    elif op == 4:
        id = int(input("Digite o ID do evento que deseja marcar como atendido: "))
        #marcarEventoAtendido(listaEventos, id)

    #elif op == 5:
        #gerarRelatorio(listaEventos)

    else:
        print("Opção inexistente, tente novamente!")

print("Programa encerrado!")
