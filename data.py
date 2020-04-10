import pandas as pd
import numpy as np

import pathlib

df = pd.read_excel(str(pathlib.Path().absolute())+"/Data/Bengaluru.xls")

def test():
    print("working")
    
def locality():
    df = pd.read_excel(str(pathlib.Path().absolute())+"/Data/Bengaluru.xls")
    df = df.set_index('S.No.')
    df = df.dropna(subset=['PIN'])
    df.drop(df[df['PIN'] == '-' ].index , inplace=True)
    graph=df['PIN'].value_counts()
    graph=graph.dropna()
    x=(graph.tolist())
    y=[]
    for i in graph.index.tolist():
        y.append(str(i))
    return(x,y)

def country():
    df = pd.read_excel(str(pathlib.Path().absolute())+"/Data/Bengaluru.xls")
    country=df['Port of Origin of journey'].value_counts()
    y=(country[0:20].tolist())
    x=[]
    for i in country[0:20].index.tolist():
        x.append(str(i))
    return(x,y)

def gender():
    Diagonised = pd.read_excel(str(pathlib.Path().absolute())+"/Data/D_Bengaluru.xlsx")
    Gender=Diagonised["Gender"].value_counts()
    y=(Gender.tolist())
    x=[]
    for i in Gender.index.tolist():
        x.append(str(i))
    return(x,y)

def Type_of_Infection_source():
    Diagonised = pd.read_excel(str(pathlib.Path().absolute())+"/Data/D_Bengaluru.xlsx")
    Type_of_Infection_source=Diagonised["Type of Infection\nsource"].value_counts()
    y=(Type_of_Infection_source.tolist())
    x=[]
    for i in Type_of_Infection_source.index.tolist():
        x.append(str(i))
    return(x,y)

def age():
    Diagonised = pd.read_excel(str(pathlib.Path().absolute())+"/Data/D_Bengaluru.xlsx")
    Age=Diagonised["Age"].value_counts()
    y=(Age.tolist())
    x=[]
    for i in Age.index.tolist():
        x.append(str(i))
    return(x,y)