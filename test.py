import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

data = pd.read_csv('complete.csv')
state=28
UT=8
total_states_UT=state+UT
No_afftected_states=len(pd.unique(data['Name of State / UT']))
States_not_affected=total_states_UT-No_afftected_states
pie_data= [['Number of afftected States', No_afftected_states], ['Number of Unafftected States', States_not_affected]]

df = pd.DataFrame(pie_data,columns = ['Status', 'Number'])
fig = px.pie(df,values='Number', names='Status')
fig.show()

df_1=pd.read_csv('complete.csv')
df_1['datetime'] = pd.to_datetime(data['Date'])
df_1.index = df_1['datetime']
line=df_1.resample('D').sum()
fig = px.line(line,x=line.index.tolist(), y='Total Confirmed cases (Indian National)')
fig.show()

fig = go.Figure(data=go.Scatter(x=line.index.tolist(), y=line['Total Confirmed cases (Indian National)']))
fig.show()