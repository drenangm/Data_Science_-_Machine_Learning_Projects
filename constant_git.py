# Modulo de valores constantes

# Importacao
import json

# Constantes
APP_LOGO = "imagens/logo.png"
MAPPING_FILE = "config/mapeamento_campos_dataset.json"
DATAFILE = "datasets/dataset.csv"

# Formatacao dos argumentos da barra lateral
SIDEBAR_STYLE = {"position": "fixed",
                 "top": 0,
                 "left": 0,
                 "bottom": 0,
                 "width": "15rem",
                 "padding": "0rem 0rem",
                 "background-color": "dark"}

# Formatacao dos itens de navegacao
NAVITEM_STYLE = {"padding": "0rem 1rem"}

# Os estilos do conteudo principal posicionam-se a direita da barra lateral e adicionamos um preenchimento
CONTENT_STYLE = {"margin-left": "15rem", "padding": "0rem 0rem"}


# Inicializa os nomes das colunas do dataset
ID = "ID"
STATUS = "Status"
CRIADO_POR = "Criado Por"
ATRIBUIDO_A = "Atribuido A"
ATENDIDO_POR = "Atendido Por"
SEVERIDADE = "Severidade"
PRIORIDADE = "Prioridade"
CLIENTE = "Cliente"
DATA_CRIACAO = "Data Criacao"
DATA_FECHAMENTO = "Data Fechamento"
TIPO_CHAMADO = "Tipo Chamado"

# Nomes dos arquivos csv
CSV_ID = "ID"
CSV_STATUS = "Status"
CSV_CRIADO_POR = "Criado Por"
CSV_ATRIBUIDO_A = "Atribuido A"
CSV_ATENDIDO_POR = "Atendido Por"
CSV_SEVERIDADE = "Severidade"
CSV_PRIORIDADE = "Prioridade"
CSV_CLIENTE = "Cliente"
CSV_DATA_CRIACAO = "Data Criacao"
CSV_DATA_FECHAMENTO = "Data Fechamento"
CSV_TIPO_CHAMADO = "Tipo Chamado"  

# Dicionario pra mapeamento dos campos (para quando o usuario altera criar a correspondencia)
FIELD_MAP = {"ID": "ID",
             "Status": "Status",
             "Criado Por": "Criado Por",
             "Atribuido A": "Atribuido A",
             "Atendido Por": "Atendido Por",
             "Severidade": "Severidade",
             "Prioridade": "Prioridade",
             "Cliente": "Cliente",
             "Data Criacao": "Data Criacao",
             "Data Fechamento": "Data Fechamento",
             "Tipo Chamado": "Tipo Chamado"}

# Formato das datas
DATE_FORMAT = "%d-%m-%Y %H:%M"

# Variaveis customizadas
CREATED_TIME = 'CreatedTime'
CREATED_DT = 'CreatedDT'
STATUS_TYPE = 'StatusType'
CLOSED_ISSUE_STATUS = ["Fechado", "Resolvido", "Solucao Proposta", "Pesquisa Realizada", "Solucao Aplicada", "Solucao Documentada"]


# Funcao para leitura das configuracoes
def read_config():

    # Variaveis
    global ID
    global STATUS
    global CRIADO_POR
    global ATRIBUIDO_A
    global ATENDIDO_POR
    global SEVERIDADE
    global PRIORIDADE
    global CLIENTE
    global DATA_CRIACAO
    global DATA_FECHAMENTO
    global TIPO_CHAMADO

    global CSV_ID
    global CSV_STATUS
    global CSV_CRIADO_POR
    global CSV_ATRIBUIDO_A
    global CSV_ATENDIDO_POR
    global CSV_SEVERIDADE
    global CSV_PRIORIDADE
    global CSV_CUSTOMER
    global CSV_DATA_CRIACAO
    global CSV_DATA_FECHAMENTO
    global CSV_TIPO_CHAMADO

    global FIELD_MAP
    global DATE_FORMAT


    # Carrega o arquivo de mapeamento (JSON)
    with open(MAPPING_FILE) as f:
        CONFIG_OBJECT = json.load(f)

# Mapeamento de campos
FIELD_MAP = CONFIG_OBJECT["KeyMapping"]["FieldMapping"]
ID = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["id"]
STATUS = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["status"]
CRIADO_POR = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["criado_por"]
ATRIBUIDO_A = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["atribuido_a"]
ATENDIDO_POR = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["atendido_por"]
SEVERIDADE = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["severidade"]
PRIORIDADE = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["prioridade"]
CLIENTE = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["cliente"]
DATA_CRIACAO = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["data_criacao"]
DATA_FECHAMENTO = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["data_fechamento"]
TIPO_CHAMADO = CONFIG_OBJECT["KeyMapping"]["VarMapping"]["tipo_chamado"]
DATE_FORMAT = CONFIG_OBJECT["DateFormat"]

