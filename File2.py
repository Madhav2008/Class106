import csv
import plotly.express as px
import numpy as np

file = open("Data2.csv")
df = csv.DictReader(file)
fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
fig.show()

def getDataSource():
    Coffee = []
    Sleep = []
    file = open("Data2.csv")
    df = csv.DictReader(file)
    
    for i in df:
        Coffee.append(float(i["Coffee in ml"]))
        Sleep.append(float(i["sleep in hours"]))

    return {"x" : Coffee, "y" : Sleep}

def FindCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation B/W Coffee And Sleep Is :", correlation[0,1])

def setup():
    datasource = getDataSource()
    FindCorrelation(datasource)

setup()
