
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import os

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/cb5392c35661370d95f300086accea51/raw/8e0768211f6b747c0db42a9ce9a0937dafcbd8b2/indicators.csv')

# 
df = pd.read_csv(os.getcwd() + '/datasets/6_2-indicators.csv')

available_indicators = df['Indicator Name']


app.layout = html.Div([

    dcc.Markdown(children='''
#### [Interactive Graph with Multiple Inputs](https://dash.plot.ly/getting-started-part-2)
    '''),
    html.Label('Interactive Graph with Multiple-Input'),
    
    html.Hr(),

    # markdown
    html.Div([
        dcc.Markdown('''
In this example, the `update_graph` function gets called whenever the `value` property of the `Dropdown`, `Slider`, or `RadioItems` components change.

The input arguments of the `update_graph` function are the new or current value of each of the `Input` properties, in the order that they were specified.

Even though only a single Input changes at a time (a user can only change the value of a single Dropdown in a given moment), Dash collects the current state of all of the specified Input properties and passes them into your function for you. Your callback functions are always guaranteed to be passed the representative state of the app.

    '''),
    ]),

    html.Hr(),


    # 下拉菜单组件等
    html.Div([

        html.Div([
            html.Label(children="选择x轴的列:"),
            # dropdown
            dcc.Dropdown(
                id="crossfilter-xaxis-column",
                # # Key:Value dictionaries list, key must be String
                # [{k1:v, k2:v}, {k1:v, k2:v}, {k1:v, k2:v} ...]
                options=[dict(label=i, value=i) for i in available_indicators],
                value = 'Fertility rate, total (births per woman)',
            ),

            # Radio, 选择X轴的类型
            html.Label(children="选择x轴的类型："),
            dcc.RadioItems(
                id="crossfilter-xaxis-type",
                options=[
                    dict(label='Linear', value='Linear'),
                    dict(label='Log', value='Log'),
                ],
                value = 'Linear',
                labelStyle=dict(display='inline-block'), # ???
            ),

        ], style=dict(width='49%',display="inline-block")),

        html.Div([
            # dropdown
            html.Label(children="选择y轴的列:"),
            dcc.Dropdown(
                id="crossfilter-yaxis-column",
                options=[dict(label=i, value=i) for i in available_indicators],
                value = 'Life expectancy at birth, total (years)',
            ),

            # Radio, 选择y轴的类型
            html.Label(children="选择y轴的类型："),
            dcc.RadioItems(
                id="crossfilter-yaxis-type",
                options=[
                    dict(label='Linear', value='Linear'),
                    dict(label='Log', value='Log'),
                ],
                value = 'Linear',
                labelStyle=dict(display='inline-block'), # ???
            ),
        ], style=dict(width='49%',display="inline-block")),

    ]),

    # ====== Graph =====
    dcc.Graph(id='indicator-graph'),
    dcc.Slider(
        id='year-slider',
        min = df['Year'].min(),
        max = df['Year'].max(),
        value = df['Year'].max(),
        marks = {str(year):str(year) for year in df['Year'].unique()},
    ),


    html.Hr(),

    dcc.Markdown('''
### [拓展学习1](https://dash.plot.ly/getting-started-part-2)
接下来还有 **Multiple Outputs**, **Chain outputs and input together**的学习，后期根据实践需求来参考.

### [拓展学习2 Interactive Graphing](https://dash.plot.ly/interactive-graphing)
**Update Graphs on Hover**， **Cross Filter**
    ''')

])

# Output 1: Figrue
@app.callback(
    Output('indicator-graph','figure'),
    [Input('crossfilter-xaxis-column','value'),
    Input('crossfilter-xaxis-type', 'value'),
    Input('crossfilter-yaxis-column','value'),
    Input('crossfilter-yaxis-type','value'),
    Input('year-slider','value'),])

def update_graph(xaxis_column_name, xaxis_type, 
                yaxis_column_name, yaxis_type,
                selected_year):
    selected_df_by_year = df[df['Year']==selected_year]

    figure = {
        'data': [go.Scatter(
            x= selected_df_by_year[selected_df_by_year['Indicator Name'] == xaxis_column_name]['Value'],
            y= selected_df_by_year[selected_df_by_year['Indicator Name'] == yaxis_column_name]['Value'],
            text=selected_df_by_year[selected_df_by_year['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker=dict(size=15,opacity=0.5,line=dict(width=0.5,color='white'))
        )],
        'layout':go.Layout(
            title="Global Data Bank",
            xaxis=dict(
                title = xaxis_column_name,
                type= 'linear' if xaxis_type == 'Linear' else 'log',
            ),
            yaxis=dict(
                title = yaxis_column_name,
                type= 'linear' if yaxis_type == 'Linear' else 'log',
            ),
            height=450,
            margin=dict(l=40,r=10,b=80,t=50),
            hovermode='closest',
        ),
    }
    return figure



if __name__ == "__main__":
    app.run_server(debug=True)