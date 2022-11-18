import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from Connection import Connection
import querys as sql



external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

# Inicializacion app dash
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# Casos por pais
con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.presupuesto_dt(), con.connection)
con.closeConnection()
ptecnicos = pd.DataFrame(query, columns=["id_j", "nombre", "presupuesto_en_miles"])

# Grafico barras
figpietecnicos = px.pie(ptecnicos.head(20), names="nombre", values="presupuesto_en_miles")

# Layout
app.layout = html.Div(children=[
    html.H1(children='Tabla presupuesto tecnicos'),
    dcc.Graph(
        id='piepresupuesto',
        figure=figpietecnicos
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)