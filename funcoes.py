def displayMenu():
    print("=== Planejador de Eventos do Campus ===\n" \
    "1. Adicionar Evento\n" \
    "2. Ver Todos os Eventos\n" \
    "3. Filtrar por Categoria\n" \
    "4. Marcar Evento como Participado\n" \
    "5. Gerar Relatório\n" \
    "6. Deletar Evento\n" \
    "7. Procurar Evento\n" \
    "8. Sair")

def getEscolhaDoUsuario(): # op = opção
    op = input("\nEscolha uma opção: ").strip()
    if op.isnumeric():
        op = int(op)
        return op

def filtrarEventosPorCategoria(listaEventos, categoria):
    print(f"\nOs Eventos marcados como {categoria.capitalize()}, são:\n")
    categoria= categoria.lower().strip()
    existemEventos= False

    for evento in listaEventos:
        if evento["categoria"].lower().strip() == categoria:
            existemEventos = True
            print(evento["nome"].capitalize())
              
    if existemEventos == False: 
            print("****Não existem Eventos com essa categoria!****")

def marcarEventoAtendido(listaEventos, id):

    for evento in listaEventos:
        if int(evento["id"]) == id:

            if evento["participado"] == True:
                resposta= input("\nEsse evento já foi marcado como participado, deseja desmarcar?(s/n): ").lower().strip()
                if resposta in ["sim", "s"]:
                    evento["participado"] = False
                    print(f"\nO Evento {evento['nome']} foi desmarcado!")

            else:
                evento["participado"] = True
                print(f"\nO Evento {evento['nome']} foi marcado como participado!")
        else:
            print("ID inexistente!")


def gerarRelatorio(listaEventos):
    print("\n--- RELATÓRIO DE EVENTOS ---")
    listaCategoria = {}
    participados = 0
    if len(listaEventos) == 0:
        print("Nenhum evento cadastrado!")
    else:
        print("Total de Eventos: ", len(listaEventos))
        
        for evento in listaEventos:
            verifica = evento["categoria"].strip().capitalize()
            if verifica in listaCategoria:   
                listaCategoria[verifica] = listaCategoria[verifica] + 1
            else:                  
                listaCategoria[verifica] = 1
        for evento in listaEventos:
            if evento['participado'] == True:
                participados += 1

        print("Por Categoria:",listaCategoria)
        porcentagem = (participados/(len(listaEventos)) * 100) 
        print(f"Participados: {porcentagem:.0f}% ({participados}/{len(listaEventos)})")


def adicionarEvento(listaEventos, nome, data, local, categoria): #fiz isso aqui temporáriamente só pra poder testar as partes que eu fiz 
    novoID = len(listaEventos) 
    evento = {  
            "id": novoID+1,
            "nome": nome,
            "data": data, 
            "local": local,
            "categoria": categoria,
            "participado": False
            }
    listaEventos.append(evento.copy())
    print(f"O Evento {nome.capitalize()} foi adicionado com sucesso!")
    return evento

displayMenu()
listaEventos = []
op = 0
while op != 8:

    op = getEscolhaDoUsuario()

    if op == 1:
        
        nome = input("Nome do Evento: ")
        data = input("Data (AAAA-MM-DD): ") 
        local = input("Local: ")
        categoria = input("Categoria: ")
        
        adicionarEvento(listaEventos, nome, data, local, categoria)

    #elif op == 2:
    #listarEventos(listaEventos)

    elif op == 3:
        listaCategoria =[]
        if len(listaEventos) == 0:
            print("Nenhum evento cadastrado ainda, não há o que filtrar!")
        else: 
            print("=====CATEGORIAS=====")
            for evento in listaEventos:
                categoria = evento["categoria"].strip().capitalize()
                if categoria not in listaCategoria:   
                    listaCategoria.append(categoria)
        
            for categorias in listaCategoria:
                print(categorias)

            categoria = input("Digite a categoria de eventos que deseja filtrar: ")
            filtrarEventosPorCategoria(listaEventos, categoria)

    elif op == 4:
        if len(listaEventos) == 0:
            print("Nenhum evento cadastrado ainda, não há o que marcar!")
        else:
            print("=====EVENTOS=====")
            for evento in listaEventos:
                print(f"{evento['id']} - {evento['nome']}")
        
            id = int(input("\nDigite o ID do evento que deseja marcar como atendido: "))
            marcarEventoAtendido(listaEventos, id)

    elif op == 5:
        gerarRelatorio(listaEventos)

    elif op == 6:
        if len(listaEventos) == 0:
            print("Nenhum evento cadastrado ainda, não há o que deletar!")
        else:
            print("=====EVENTOS=====")
            for evento in listaEventos:
                print(f"{evento['id']} - {evento['nome']}")
            
            id = int(input("\n Digite o ID do evento que você gostaria de deletar: "))
            #deletarEvento(listaEventos, id)
    
    elif op == 7:
        if len(listaEventos) == 0:
            print("Nenhum evento cadastrado ainda, não há o que procurar!")
        else:
            nome = input("\nDigite o nome do evento: ")
            #procurarEventoPorNome(listaEventos, nome)

    elif op == 8:
        print("Programa encerrado!")
        
    else:
        print("Valor inválido, tente novamente!")

