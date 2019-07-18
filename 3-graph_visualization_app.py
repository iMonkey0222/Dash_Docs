# -*- coding:utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# df = pd.read_csv('https://raw.githubusercontent.com/yankev/test/master/life-expectancy-per-GDP-2007.csv') 
df = pd.read_csv('datasets/life-expectancy-per-GDP-2007.csv')

app.layout = html.Div([

    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data':[
                go.Scatter(
                    x=df[df['continent'] == i]['gdp_percap'],
                    y=df[df['continent'] == i]['life_exp'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker=dict(size=15,
                        line=dict(width=0.5,color='white')
                        ),
                    # marker={'size':15,'line':{'width':0.5, 'color':'white'}},
                    name=i,
                ) for i in df.continent.unique()
            ],
            'layout':go.Layout(
                xaxis=dict(
                    type='log',             # 对数坐标轴 ** Logarithmic Axes
                    title='GDP Per Capita'),
                yaxis=dict(title ='Life Expectancy'),
                margin=dict(l=40, b=40,t=10,r=10),
                legend=dict(x=0.1, y=1),    # legend position
                hovermode='closest'
            )
        }
    )

])

if __name__ == '__main__':
    app.run_server(debug=True)