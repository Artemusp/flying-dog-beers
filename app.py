from datetime import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


def serve_layout():
    return html.Div(
        [dcc.Interval(id="interval", interval=10000), html.P(id="output")]
    )


app = dash.Dash()

#app = dash.Dash()
server = app.server

app.layout = serve_layout


@app.callback(Output("output", "children"), [Input("interval", "n_intervals")])
def display_time(n):
    return datetime.now().strftime("The time is: %H:%M:%S")


if __name__ == "__main__":
    app.run_server()
