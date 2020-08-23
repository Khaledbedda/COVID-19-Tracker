import os
import sys

env_p = sys.prefix  # path to the env
print("Env. path: {}".format(env_p))

new_p = ''
for extra_p in (r"Library\mingw-w64\bin",
    r"Library\usr\bin",
    r"Library\bin",
    r"Scripts",
    r"bin"):
    new_p +=  os.path.join(env_p, extra_p) + ';'

os.environ["PATH"] = new_p + os.environ["PATH"]  # set it for Python
import numpy as np
import pandas as pd
import plotly.offline
import plotly.graph_objs as go
import plotly.express as px

url = 'https://github.com/owid/covid-19-data/blob/master/public/data/owid-covid-data.csv?raw=true'
reader = pd.read_csv(url)
df = reader[["iso_code","location","new_cases","new_deaths","date"]]





fig2 = px.bar(df, x="iso_code", y="new_deaths", color="location", animation_frame="date", animation_group="location")
fig2.write_html("Graphs/chart by deaths.html") 


fig3 = px.bar(df, x="iso_code", y="new_cases", color="location", animation_frame="date", animation_group="location")
fig3.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'}, yaxis=dict(range=[0, 20000]))
fig3.write_html("Graphs/chart by cases.html") 


fig4 = px.choropleth(df, locations="iso_code", color="new_deaths", hover_name="location", animation_frame="date", color_continuous_scale='Inferno', projection="natural earth")
fig4.write_html("Graphs/map graph by deaths.html") 


fig5 = px.choropleth(df, locations="iso_code", color="new_cases", hover_name="location", animation_frame="date", color_continuous_scale='Inferno', projection="natural earth")
fig5.update_layout(showlegend=False)                    
fig5.write_html("Graphs/map graph bycases.html") 
