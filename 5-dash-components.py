# -*- coding:utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout=html.Div([

    dcc.Markdown(children='''
## Dash Components Study
All components are from [Dash Components](https://dash.plot.ly/dash-core-components),
还有很多没有包含，可以直接上网站找，比如交互式的表格，上传功能组件，Tab子页，确认对话框，存储，测量器（仪表盘）, Logout Button...
    '''),
    #====== Text Area =====
    html.Label("0.Text Area"),
    dcc.Textarea(
        placeholder="输入内容。。。",
        value="这是TextArea组件",
        style={'width':'100%'},
    ),

    # =========== Dropdown  ===========
    html.Label('1.Dropdown'),
    dcc.Dropdown(
        options=[
            dict(label='New York Çity', value='NYC'),
            dict(label=u'Montréal', value='MTL'),
            dict(label='San Francisco',value='SF'),
        ],
        value='MTL' # default value in dropdown
    ),

    # =========== Multi-Select Dropdown  ===========
    html.Label('2.Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            dict(label='New York Çity', value='NYC'),
            dict(label=u'Montréal', value='MTL'),
            dict(label='San Francisco',value='SF'),            
        ],
        value=['SF','NYC'],
        multi=True
    ),

    # =========== Radio  ===========
    html.Label('3.Radio Items'),
    dcc.RadioItems(
        options=[
            dict(label='New York City', value='NYC'),
            dict(label=u'Montréal', value='MTL'),
            dict(label='San Francisco',value='SF'),   
        ],
        value='SF'
    ),

    # html.Label('Checkboxes'),
    # dcc.Checklist(
    #     options=[
    #         {'label': 'New York City', 'value': 'NYC'},
    #         {'label': 'Montreal', 'value': 'MTL'},
    #         {'label': 'San Francisco', 'value': 'SF'}
    #     ],
    #     values=['MTL', 'SF']
    # ),
    html.Label('4.Checkboxes'),
    dcc.Checklist(
        options=[
            dict(label='New York City', value='NYC'),
            dict(label= 'Montréal', value='MTL'),
            dict(label='San Francisco',value='SF'),   
        ],
        values=['MTL', 'SF'] # 必须是有序的
    ),
    # =========== Text Input ===========
    html.Label('5.Text Input'),
    dcc.Input(value='MTL', type='text'),

    # =========== Slider ===========
    html.Label('6.Slider (Step = 0.5)'),
    dcc.Slider(
        min=0,
        max=9,
        step=0.5,
        # marks=dict(i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)),
        # Key:Value dictionary, key must be String
        marks={ i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
        value=8,
    ),

    # =========== Input box ===========
    # Button
    html.Label('7.输入框与按钮'),
    # html.Div(dcc.Input(id='input-box',type='text', value="Please enter value")), # 可以单独成一行
    dcc.Input(id='input-box',type='text', value="Please enter value"),             # 和button在同一行
    html.Button('Submit here', id='button', draggable=True),
    html.Div(id='output-container-button', children='显示在Input text并点击提交过后的内容'),


    # =========== 3 Button Combine Timestamp===========
    html.Label('8.按钮 与 点击次数、timestamp'),
    html.Button('按钮1', id="btn-1", n_clicks_timestamp='0'),
    html.Button('按钮2', id="btn-2", n_clicks_timestamp='0'),
    html.Button('按钮3', id="btn-3", n_clicks_timestamp='0'),
    html.Div(id='container-button-timestamp', children="默认显示值"),

    # =========== Date Picker Single ===========
    html.Label("9.单个日期选择"),
    dcc.DatePickerSingle(
        id='data-picker-single',
        date = datetime(1992,10,20)
    ),

    # =========== Date Picker Range ===========
    html.Label("10.日期范围选择"),
    dcc.DatePickerRange(
        id='data-picker-range',
        start_date = datetime(1992,10,20),
        end_date = datetime(2018,12,12)
        # end_date_placeholder_text='Select a date!',
    ),


    # ========== markdown ==========
    # markdown_text = 
    html.Label('11.Markfown'),
    dcc.Markdown(children = '''
### Dash and Markdown

Dash apps can be written in Markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of Markdown.
Check out their [60 Second Markdown Tutorial](http://commonmark.org/help/)
if this is your first introduction to Markdown!
'''),



    # ===== Graph ======
    html.Label('12.绘图'),
    dcc.Graph(
        figure = go.Figure(
            data = [
                go.Bar(
                    x = [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y = [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                    350, 430, 474, 526, 488, 537, 500, 439],
                    name="Rest of the world",
                    marker=go.bar.Marker(color='rgb(55,83,109)'),
                ),
                go.Bar(
                    x=[1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                    2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
                    y=[16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                    299, 340, 403, 549, 499],
                    name="China",
                    marker=go.bar.Marker(color='rgb(26,118,255)'),
                )
            ],
            layout=go.Layout(
                title="US Export pf Plastic Scrap",
                showlegend=True,
                legend=go.layout.Legend(x=0,y=1.0),
                margin=go.layout.Margin(l=40,r=0,t=40,b=30),
                width=1000,
                height=300,
            ),
        ),
        # style={'height':300},
        id='my-graph'
    ),

    # ===== Confirm Dialog =====
    html.Label("13. 确认对话框 Comfirm Dialog"),
    dcc.ConfirmDialogProvider(
        children=html.Button('Click Me',),
        id='danger-danger',
        message='Danger danger! Are you sure you want to continue?'
    ),

], style=dict(columnCount=1))


# =========== For Input box + Button ===========
@app.callback(
    Output('output-container-button', 'children'),
    [Input('button', 'n_clicks')],
    [State('input-box', 'value')], # 允许我在不触发回调（not fire callbacks）的情况下传递额外的值，即不会即时更新结果值
    )

def button_update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(value, n_clicks)


# ======= For 3 Button Combine Timestamp ===========
@app.callback(
    # output 是id为container-button-timestamp的一行
    Output('container-button-timestamp', 'children'),
    # 3 buttons是input
    [Input('btn-1','n_clicks_timestamp'),Input('btn-2','n_clicks_timestamp'),Input('btn-3','n_clicks_timestamp')]
    )
def displayClick_of_3buttons(btn1, btn2, btn3):
    if int(btn1) > int(btn2) and int(btn1) > int(btn3):
        msg = "上次点击按钮为按钮1"
    elif int(btn2) > int(btn1) and int(btn2) > int(btn3):
        msg = "上次点击按钮为按钮2"
    elif int(btn3) > int(btn1) and int(btn3) > int(btn2):
        msg = "上次点击按钮为按钮3"
    else:
        msg = "最近没有点击按钮"
    
    return html.Div([
        html.Div('btn1: {}'.format(btn1)), # 显示button1的n_clicks_timestamp
        html.Div('btn2: {}'.format(btn2)), # 显示button2的n_clicks_timestamp
        html.Div('btn3: {}'.format(btn3)), # 显示button3的n_clicks_timestamp
        html.Div(msg)       # 显示message
    ])
    

    


if __name__ == '__main__':
    app.run_server(debug=True)