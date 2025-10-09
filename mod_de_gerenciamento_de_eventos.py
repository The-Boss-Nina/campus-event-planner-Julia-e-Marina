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