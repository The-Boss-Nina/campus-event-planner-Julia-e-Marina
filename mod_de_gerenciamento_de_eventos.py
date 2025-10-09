from datetime import datetime

# Lista principal que armazena os eventos
listaEventos = []

# Validação de data no formato AAAA-MM-DD
def validarData(dataStr):
    try:
        datetime.strptime(dataStr, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Adiciona novo evento com validação
def adicionarEvento(listaEventos, nome, data, local, categoria):
    if not nome or not data or not local or not categoria:
        print("Todos os campos devem ser preenchidos.")
        return

    if not validarData(data):
        print("Data inválida. Use o formato AAAA-MM-DD.")
        return

    novoEvento = {
        "id": len(listaEventos) + 1,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False
    }
    listaEventos.append(novoEvento)
    print(f"O Evento '{nome}' foi adicionado com sucesso!")

# Listar todos os eventos
def listarEventos(listaEventos):
    if not listaEventos:
        print("Nenhum evento cadastrado.")
        return

    print("\n--- LISTA DE EVENTOS ---")
    for evento in listaEventos:
        print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']} | Participado: {evento['participado']}")

# Buscar eventos por nome
def procurarEventoPorNome(listaEventos, nome):
    encontrados = [e for e in listaEventos if nome.lower() in e['nome'].lower()]
    if not encontrados:
        print("Nenhum evento encontrado com esse nome.")
    else:
        print("\n--- EVENTOS ENCONTRADOS ---")
        for evento in encontrados:
            print(f"ID: {evento['id']} | Nome: {evento['nome']} | Data: {evento['data']} | Local: {evento['local']} | Categoria: {evento['categoria']} | Participado: {evento['participado']}")

# Deletar evento por ID
def deletarEvento(listaEventos, id):
    for evento in listaEventos:
        if evento['id'] == id:
            listaEventos.remove(evento)
            print(f"Evento '{evento['nome']}' removido com sucesso.")
            return
    print("Evento não encontrado.")