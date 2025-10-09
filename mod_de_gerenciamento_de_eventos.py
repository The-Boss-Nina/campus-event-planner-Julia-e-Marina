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