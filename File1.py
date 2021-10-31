import csv
import plotly.express as px
import numpy as np

file = open("Data1.csv")
df = csv.DictReader(file)
fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
fig.show()

def getDataSource():
    Temperature = []
    IceCream = []
    file = open("Data1.csv")
    df = csv.DictReader(file)
    
    for i in df:
        Temperature.append(float(i["Temperature"]))
        IceCream.append(float(i["Ice-cream Sales"]))

    return {"x" : Temperature, "y" : IceCream}

def FindCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation B/W Temperature And Ice-Cream Sales Is :", correlation[0,1])

def setup():
    datasource = getDataSource()
    FindCorrelation(datasource)

setup()
