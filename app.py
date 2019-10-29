import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_table
import pandas as pd


########### Define your variables ######
myheading = "Best Craft Beers in DC"
mysubheading = "August 2019"
tabtitle = 'python rocks'
filename = 'dc-breweries.csv'
sourceurl = 'https://www.beeradvocate.com/beer/top-rated/us/dc/'
githublink = 'https://github.com/calijason76/dash-table-example'
mytitle = 'Beer Comparison'
label1 = 'Beer Ratings'
label2 = 'ABV'
color1='lightblue'
color2='darkgreen'

########### Set up the data
df = pd.read_csv(filename)
beers = df['Beer Name']
ratings = df['Ratings (Averag)']
abv = df['Alcohol By Volume (ABV)']

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    html.H3(mysubheading),

    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    ),
    html.Br(),
    dcc.Graph(
        id = 'beer_compare'
        figure = beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    html.Br(),
    html.A("Plotly Dash", href='https://plot.ly/python/pie-charts/')
    ]
)

########### Set up the chart
bratings = go.Bar(
    x=beers,
    y=ratings,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv,
    name=label2,
    marker={'color':color2}
)

beer_data = [bratings, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

############ Deploy
if __name__ == '__main__':
    app.run_server()
