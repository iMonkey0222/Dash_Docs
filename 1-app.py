# -*- coding:utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html # dash_html_components library has a component for every HTML tag

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

colors = {
    'background':'#111131',
    'text': '#7FDBFF',
    }


# The layout is composed of a tree of "components" like html.Div and dcc.Graph.
app.layout=html.Div(style={'backgroundColor':colors['background']}, children=[

    # generates a <h1>Hello Dash</h1> HTML element in your application.
    html.H1(children='Hello Dash hahahh',
            style={
                    'textAlign':'center',
                    'color':colors['text'],
                    },
    ),
    
    html.Div(children='DASH: A web application framework for Python.',
            style={
                'textAlign':'center',
                'color':colors['text'],
            },
    ),
    
    # dash_core_components describe higher-level components that are 
    # interactive and are generated with 
    # JavaScript, HTML, and CSS through the React.js library.
    dcc.Graph(
        id='example-graph-2',
        figure={
            'data':[
                {'x':[1,2,3], 'y':[4,1,2],'type':'bar','name':'SF'},
                {'x':[1,2,3], 'y':[3,12,6],'type':'bar','name':u'Montréal'},
            ],
            'layout':{
                'title':'Dash Data Visualization',
                'plot_bgcolor':colors['background'],
                'paper_bgcolor':colors['background'],
                'font':{
                    'color':colors['text']
                }
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)