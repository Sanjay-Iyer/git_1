# from dash import Dash, html, dcc

# app = Dash(__name__)

# app.layout = html.Div([
#     dcc.Dropdown(['New York City', 'Montréal', 'San Francisco'], 'Montréal')
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)


import plotly.graph_objects as go # or plotly.express as px
fig = go.Figure() # or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

app.run_server(debug=True, use_reloader=False)