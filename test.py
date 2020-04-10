# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

import data as DATA
DATA.test()


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


data = pd.read_csv('complete.csv')
##############################Pie Chart - Percentage of States Affected###################################
state=28
UT=8
total_states_UT=state+UT

No_afftected_states=len(pd.unique(data['Name of State / UT']))
States_not_affected=total_states_UT-No_afftected_states
    
labels=['Number of afftected States','Number of Unafftected States'] 
values=[No_afftected_states, States_not_affected]
##############################Pie Chart - Percentage of States Affected###################################


##############################Scatter Chart - People affected###################################
df=pd.read_csv('complete.csv')
df['datetime'] = pd.to_datetime(df['Date'])
df.index = df['datetime']
line=df.resample('D').sum()

res_list = [] 
for i in range(0, len(line)): 
    res_list.append(line['Total Confirmed cases (Indian National)'][i] + line['Total Confirmed cases ( Foreign National )'][i])
##############################Scatter Chart - People affected###################################

##############################Bar Chart - State Variation###################################
state=pd.read_csv('complete.csv')
state=state.groupby(['Name of State / UT']).max()
statewise=(state['Total Confirmed cases (Indian National)']+state['Total Confirmed cases ( Foreign National )']).tolist()
##############################Bar Chart - State Variation###################################


markdown_text = '''
An Analytical Dashboard by [Vishnu Prasad P](Vishnu:vp.vishnu269@gmail.com)
'''

# fig=go.Figure(go.Scatter(x=line.index.tolist(), y=res_list))

fig = go.Figure(data=go.Scatter(name='Diagonised',x=line.index.tolist(), y=res_list,mode='lines+markers'))
fig.add_trace(go.Bar(name='Cured', x=line.index.tolist(), y=line['Cured/Discharged/Migrated'].tolist()))
fig.update_layout(title='Number of CORONA cases')

PercentageofStates = go.Figure(go.Pie(labels=labels, values=values, hole=.3))
PercentageofStates.update_layout(title='Percentage of states and UT affected')

State_wise=go.Figure(go.Bar(x=state.index.tolist(), y=statewise))
State_wise.update_layout(title='Variation Across States')

loc_x,loc_y=DATA.locality()
Locality=go.Figure(go.Bar(x=loc_y, y=loc_x))

Country_x,Country_y=DATA.country()
Country=go.Figure(go.Bar(x=Country_x, y=Country_y))
Country.update_layout(title='No. of people Quarantined on the basis of Port of Origin of journey')

Gen_labels,Gen_values=DATA.gender()
Gender_ratio = go.Figure(go.Pie(labels=Gen_labels, values=Gen_values, hole=.3))
Gender_ratio.update_layout(title='Gender ratio of the Diagonised')

IS_x,IS_y=DATA.Type_of_Infection_source()
Infection_Source = go.Figure(go.Pie(labels=IS_x, values=IS_y, hole=.3))
Infection_Source.update_layout(title='Infection_Source')

age_x,age_y=DATA.age()
Age=go.Figure(go.Bar(x=age_x, y=age_y))
Age.update_layout(title='Age matters')

# import plotly.express as px
# data_canada = px.data.gapminder().query("country == 'Canada'")
# fig1 = px.bar(data_canada, x='year', y='pop')

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='#coronaindia',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),

    html.Div(dcc.Markdown(children=markdown_text), style={
        'textAlign': 'center',
        'color': colors['text']
    }),

    html.Div(
    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
    ),
    html.Div(
    dcc.Graph(
        id='example-graph',
        figure=PercentageofStates
    )
    ),
    html.Div(
    dcc.Graph(
        id='example-graph_3',
        figure=State_wise
    )
    ),
    html.Div(
    dcc.Graph(
        id='example-graph_4',
        figure=Country
    )
    ),
    html.Div(
    dcc.Graph(
        id='example-graph_5',
        figure=Gender_ratio
    )
    ),
     html.Div(
    dcc.Graph(
        id='example-graph_6',
        figure=Infection_Source
    )
    ),
    html.Div(
    dcc.Graph(
        id='example-graph_7',
        figure=Age
    )
    ),
])

if __name__ == '__main__':
    app.run_server(port='8989',debug=True)