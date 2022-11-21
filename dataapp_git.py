# Arquivo principal do nosso programa

# Importacao das bibliotecas/pacotes
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

# Carrega o arquivo de conexao da app
from app_git import app_git
from app_git import server

# Conecta aos modulos de paginas e outros modulos
from paginas import dashboard_git, overview_git, settings_git
from modulos import navbar_git, constant_git

# Carregando as configuacoes
CONFIG_OBJECT = constant.read_config()

# Configura uma divisao de uma area do dashboard para acomodar um conteudo
content = html.Div(id = "page-content", style = constant.CONTENT_STYLE, className = "p-3 pt-4 pb-3")


# Configura o layout
app_git.layout = html.Div([dcc.Location(id = "url"), navbar.layout, content])

# Callback contendo as funcoes para carregar cada uma das paginas
@app_git.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/paginas/dashboard_git' or pathname == '/':
		return dashboard_git.get_layout()
	elif pathname == '/paginas/overview_git':
		return overview_git.get_layout()
	elif pathname == '/paginas/settings_git':
		return settings_git.get_layout()
	else:
		return dbc.Jumbotron(
			[
				html.Div([
					html.H1("404: Not Found", className = "text-danger"),
					html.Hr(),
					html.P(f"Pagina {pathname} nao encontrada...")
				],
				style = constant.NAVITEM_STYLE)
			]
		)

# Titulo
app_git.title = 'Data App - Dashboard Interativo para Analise de Chamados de Suporte'

# Executor do programa
if __name__ == '__main__':
	app_git.run_server(debug = False, port = 3000, host = '127.0.0.2', threaded = True)