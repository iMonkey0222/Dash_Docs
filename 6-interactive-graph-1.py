import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go


# df = pd.read_csv(
#     'https://raw.githubusercontent.com/plotly/'
#     'datasets/master/gapminderDataFiveYear.csv')

df = pd.read_csv('datasets/gapminderDataFiveYear.csv')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([

    # ========================== 1. Single Input ==================
    dcc.Markdown(children='''
## Basic Dash Callbacks Study: 
#### [1.Interactive Graph with Single Input](https://dash.plot.ly/getting-started-part-2)
X轴以Log对数的形式显示： 
$$ xaxis= dict(**type='log'**,title='GDP Per Capita') $$.
    '''),

    html.Label("Interactive Graph with Single Input"),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(), # default value
        step = 5,               # 5年一个跨度
        # A key:value pairs dictionary, key must be String
        # {k:v,k:v,k:v}
        marks={str(year): str(year) for year in df['year'].unique()}
    ),

])

# ========================== 1. Single Input ==================
# 写callbacks
@app.callback(
    Output('graph-with-slider', 'figure'),  # 图部分
    [Input('year-slider', 'value')],         # 年份滑条的值
)
def update_figure(selected_year):
    filtered_df = df[df.year == selected_year]
    traces = []
    for country in filtered_df.continent.unique():
        df_by_country = filtered_df[filtered_df.continent == country]
        trace = go.Scatter(
            x = df_by_country.gdpPercap,
            y = df_by_country.lifeExp,
            name = country,
            mode='markers',  # 点图， 否则的话是线图
            opacity=0.7,
            marker=dict(size = 15, line = dict(width=0.5, color='white')),
        )
        traces.append(trace)
    
    figure = {
        'data': traces,
        'layout': go.Layout(
            xaxis= dict(type='log',title='GDP Per Capita'),
            yaxis= dict(title = 'Life Expectency', range=[20,90]),
            margin=dict(l=40, r=10, t=10, b= 40),
            legend=dict(x=0, y=1),
            hovermode='closest',
            height=400
        )
    }
    return figure


if __name__ == '__main__':
    app.run_server(debug=True)


