def displayMenu():
    print("=== Planejador de Eventos do Campus ===\n" \
    "1. Adicionar Evento\n" \
    "2. Ver Todos os Eventos\n" \
    "3. Filtrar por Categoria\n" \
    "4. Marcar Evento como Participado\n" \
    "5. Gerar Relatório\n" \
    "6. Sair")

def getEscolhaDoUsuario(): # op = opção
    op = input("Escolha uma opção: ").strip()
    if op.isnumeric():
        op = int(op)
        return op

def filtrarEventosPorCategoria(listaEventos, categoria):
    print(f"Os Eventos marcados como {categoria.capitalize()}, são:")
    categoria= categoria.lower().strip()
    existemEventos= False
    for evento in listaEventos:
        if evento["categoria"].lower().strip() == categoria:
            existemEventos = True
            print(evento["nome"].capitalize())
        #fazer validação de entradas com espaço 
        
    if not existemEventos: 
            print("Não existem Eventos com essa categoria!")

def marcarEventoAtendido(listaEventos, id):

    for evento in listaEventos:
        if int(evento["id"]) == id:
            evento["participado"] = True
            print(f"O Evento {evento['nome']} foi marcado como participado!")


def gerarRelatorio(listaEventos):
    print("--- RELATÓRIO DE EVENTOS ---")

    if len(listaEventos) == 0:
        print("Nenhum evento cadastrado!")
    else:
        porCategoria=[]
        participados = 0
        print("Total de Eventos: ", len(listaEventos))

        for evento in listaEventos:

            if evento['participado'] == True:
                participados= participados + 1
    
    #falta fazer por categoria e porcentagem de participados


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
while op != 6:

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
        categoria = input("Digite a categoria de eventos que deseja filtrar: ")
        filtrarEventosPorCategoria(listaEventos, categoria)

    elif op == 4:
        print("=====EVENTOS=====")
        for evento in listaEventos:
            print(f"{evento['id']} - {evento['nome']}")
        
        id = int(input("\nDigite o ID do evento que deseja marcar como atendido: "))
        marcarEventoAtendido(listaEventos, id)

    elif op == 5:
        gerarRelatorio(listaEventos)

    elif op == 6:
        print("Programa encerrado!")
        
    else:
        print("Valor inválido, tente novamente!")

