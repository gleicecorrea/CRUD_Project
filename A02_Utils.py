########################################################
# Passo 04: Funções Utilitárias (utils.py)
########################################################
########################################################
# utils.py (funções utilitárias para
#          - validação
#          - sanitização
#          de dados):
########################################################

from datetime import datetime

def validate_date(date_str):
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def validate_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def validate_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#Sanitizar a entrada de dados, removendo espaços em branco extras no início e no final da string.
def sanitize_input(input_str):
    return input_str.strip()

def sanitize_input_capital(input_str):
    return input_str.strip().title() #Formata o nome para primeira letra maiúscula

# Verifica se a entrada fornecida é uma hora válida no formato HH:MM:SS.
def validate_time(time_str):
    try:
        datetime.strptime(time_str, '%H:%M:%S')
        return True
    except ValueError:
        return False
