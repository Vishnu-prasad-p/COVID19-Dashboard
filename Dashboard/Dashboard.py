from flask import Flask, render_template,request
from plotly.subplots import make_subplots
import plotly
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import json

import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

app = Flask(__name__)


@app.route('/')
def index():
    bar = create_plot()
    return render_template('index.html', plot=bar)

def create_plot():
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
    df['datetime'] = pd.to_datetime(data['Date'])
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
    
    fig = make_subplots(
    rows=2, cols=4,
    specs=[[{"type": "pie"}, {"colspan": 3},None,None],
           [{"colspan":2},None, {"colspan":2},None]],
    subplot_titles=("Percentage of States affected","Rise trend","Number of Patients Cured","Variation Across States"))

    fig.add_trace(go.Pie(labels=labels, values=values, hole=.3),
                  row=1, col=1)

    fig.add_trace(go.Scatter(x=line.index.tolist(), y=res_list),
                  row=1, col=2)
    
    fig.add_trace(#go.Bar(name='Affected', x=line.index.tolist(), y=res_list),
                  go.Scatter(name='Cured', x=line.index.tolist(), y=line['Cured'].tolist()),
                  row=2, col=1)
    fig.add_trace(go.Bar(name='Affected', x=line.index.tolist(), y=res_list),
                  row=2, col=1)
    
    fig.add_trace(go.Bar(x=state.index.tolist(), y=statewise),
                  row=2, col=3)

    fig.update_layout(height=700, showlegend=False)
    
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON

if __name__ == '__main__':
    app.run(debug=True)