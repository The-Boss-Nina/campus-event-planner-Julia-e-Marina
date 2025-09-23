def displayMenu():
    print("=== Planejador de Eventos do Campus ===\n" \
    "1. Adicionar Evento\n" \
    "2. Ver Todos os Eventos\n" \
    "3. Filtrar por Categoria\n" \
    "4. Marcar Evento como Participado\n" \
    "5. Gerar Relatório\n" \
    "6. Sair")

def getEscolhaDoUsuario(op): # op = opção

    match op:
        case 1:
            nome = input("Nome do Evento: ")
            data = input("Data (AAAA=MM=DD): ")
            local = input("Local: ")
            categoria = input("Categoria: ")

            #adicionarEvento(listaEventos, nome, data, local, categoria)
            print("\nEvento adicionado com sucesso!")

        case 2:
            #listarEventos(listaEventos)
        
        #case 3:
            #categoria = input("Digite qual categoria deseja buscar: ")
            #filtrarEventosPorCategoria(listaEventos, categoria)
        
        #case 4:
            #marcarEventoAtendido(listaEventos, id)

        #case 5:
            #gerarRelatorio(listaEventos)

        #case 6:


    #return 


def filtrarEventosPorCategoria(listaEventos, categoria):

    return

def marcarEventoAtendido(listaEventos, id):

    return


def gerarRelatorio(listaEventos):
    return 

displayMenu()