""""
This file contains all app callbacks and pathname redirects. This is the app that is ran to start the server
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
from PageHomepage import Homepage
from PageAbout import About
from PageData import Data
from PageContact import Contact
from PageLogin import Login
from PageUpload import Upload
from navbar import NavBar


#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED])


external_stylesheets = ['/assets/main.css']
app = dash.Dash(__name__, external_stylesheets= external_stylesheets)


#app.config.suppress_callback_exceptions = True


app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    NavBar(),
    html.Div(id = 'page-content')
],
)


""""
This returns the page layout based on pathname; these are all defined in their respective .py files
"""


@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/PageHomepage':
        return Homepage()
    elif pathname == '/':
        return Homepage()
    if pathname == '/PageAbout':
        return About()
    elif pathname == '/PageData':
        return Data()
    elif pathname == '/PageContact':
        return Contact()
    elif pathname == '/PageLogin':
        return Login()
    elif pathname == '/PageUpload':
        return Upload()
    else:
        return Homepage()








""""
This sets which page is active based on the URL. This is used in navbar.py to determine the active page.
The active page is then set to have a 'pill' in the nav bar. This is just the box behind the nav link indicating 
which page you are on
"""

""""Commenting out until I can fix constant refresh
@app.callback(
    [Output(f"page-{i}-link", "active") for i in range(1, 6)],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    if pathname == "/PageHomepage":
        return True, False, False, False, False
    elif pathname == "/":
        return True, False, False, False, False
    elif pathname == "/PageAbout":
        return False, True, False, False, False
    elif pathname == "/PageData":
        return False, False, True, False, False
    elif pathname == "/PageContact":
        return False, False, False, True, False
    elif pathname == "/PageLogin":
        return False, False, False, False, True
    else:
        return False, False, False, False, False
"""




if __name__ == '__main__':
    app.run_server(debug=True)

