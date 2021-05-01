import plotly.express as pe
import pandas as pd
import csv

df = pd.read_csv('data1.csv')
Mean = df.groupby(['student_id', 'level'], as_index = False)['attempt'].mean()

Diagram = pe.scatter(Mean, x ='student_id', y = "level", color = 'attempt', size = 'attempt')
Diagram.show()