import pandas as pd
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics as s
import random
df = pd.read_csv("C:/Users/Krithi/Desktop/Python/medium_data.csv")

data = df["reading_time"].tolist()

def randomSetOfMeans(Counter):
    dataSet = []
    for i in range(0, Counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = s.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    mean = s.mean(df)
    fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
    fig.add_trace(go.Scatter(x = [mean, mean], y = [0, 1], mode = "lines", name = "mean"))
    fig.show()

def setUp():
    meanList = []
    for i in range(0, 1000):
        setOfMeans = randomSetOfMeans(30)
        meanList.append(setOfMeans)
    showFig(meanList)
    mean = s.mean(meanList)
    print("samplingMean = ", mean)
setUp()
