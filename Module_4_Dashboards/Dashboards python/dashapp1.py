from flask import Flask, render_template
import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import base64
import plotly.graph_objects as go

# import cdata.googlesheets as mod

# historical trends
df = pd.read_csv("Precipitation_1901-2002.csv")
df1 = pd.read_csv("Vapour pressure_1901-2002.csv")
df2 = pd.read_csv("Average temperature_1901-2002.csv")
df3 = pd.read_csv("Minimum temperature_1901-2002.csv")
df4 = pd.read_csv("Cloud cover_1901-2002.csv")
df5 = pd.read_csv('Maximum temperature_1901-2002.csv')
df["Sum"] = pd.to_numeric(df["Sum"])
df1["Sum"] = pd.to_numeric(df1["Sum"])
df2["Sum"] = pd.to_numeric(df2["Sum"])
df3["Sum"] = pd.to_numeric(df3["Sum"])
df4["Sum"] = pd.to_numeric(df4["Sum"])
all_states = df['State'].unique()
all_states = list(all_states)
all_districts = df['District'].unique()
all_districts = list(all_districts)
all_states_v = df1['State'].unique()
all_states_v = list(all_states_v)
all_districts_v = df1['District'].unique()
all_districts_v = list(all_districts_v)
all_states_a = df2['State'].unique()
all_states_a = list(all_states_a)
all_districts_a = df2['District'].unique()
all_districts_a = list(all_districts_a)
all_states_m = df3['State'].unique()
all_states_m = list(all_states_m)
all_districts_m = df3['District'].unique()
all_districts_m = list(all_districts_m)
all_states_c = df4['State'].unique()
all_states_c = list(all_states_c)
all_districts_c = df4['District'].unique()
all_districts_c = list(all_districts_c)
all_states_mx = df5['State'].unique()
all_states_mx = list(all_states_mx)
all_districts_mx = df5['District'].unique()
all_districts_mx = list(all_districts_mx)

# predictions data
pf = pd.read_csv('rainfall_prediction.csv')
pf1 = pd.read_csv('vapour_pressure_predictions.csv')
pf2 = pd.read_csv('avg_temp_predictions.csv')
pf3 = pd.read_csv('minimum_temp_predictions.csv')
pf4 = pd.read_csv('cloud_cover_predictions.csv')
pf5 = pd.read_csv('max_temp_predictions.csv')

# soil moisture predictions

soil_df = pd.read_csv('Soil-Moisture_Predictions.csv')
all_states_sm = soil_df['State'].unique()
all_states_sm = list(all_states_sm)
all_districts_sm = soil_df['District'].unique()
all_districts_sm = list(all_districts_sm)
year = soil_df["Year"].unique()

# Ground water data


gw = pd.read_csv("Groundwater.csv")
all_states_gw = gw['STATE'].unique()
all_states_gw = all_states_gw[:-1]
all_districts_gw = gw['DISTRICT'].unique()
all_districts_gw = list(all_districts_gw)
col_gw = gw.columns[3:]
col_gw = list(col_gw)
# cnxn = mod.connect("Spreadsheet=MySheet;InitiateOAuth=GETANDREFRESH;OAuthSettingsLocation=/PATH/TO/OAuthSettings.txt")

# storage

st = pd.read_excel("Res-Report_1 (1).xlsx", engine='openpyxl')
all_states_st = st['State'].unique()
all_states_st = list(all_states_st)
all_states_st = [x for x in all_states_st if str(x) != 'nan']
all_districts_st = st['District'].unique()
all_districts_st = list(all_districts_st)

# consumption
cf = pd.read_excel("Consumption Prediction.xlsx", engine='openpyxl')

# KPI PRECIPITATION


def kpi_1():
    n = len(pd.unique(df['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Precipitation data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="tomato", height=225)

    return fig


def kpi_2():
    n = len(pd.unique(df1['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Vapour Pressure data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="skyblue", height=225)

    return fig


def kpi_3():
    n = len(pd.unique(df2['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Avg Temp data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="mediumseagreen", height=225)

    return fig


def kpi_4():
    n = len(pd.unique(df3['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Min Temp data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="gold", height=225)

    return fig


def kpi_5():
    n = len(pd.unique(df4['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Cloud Cover data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="plum", height=225)

    return fig


def kpi_6():
    n = len(pd.unique(df5['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of districts in Max Temp data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="orangered", height=225)

    return fig


# Predicition kpi


def kpi_7():
    n = len(pd.unique(pf['District']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>Districts in rainfall prediction data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="orangered", height=225)

    return fig


def kpi_8():
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of Features used for prediction</b></span>"},
        value=5,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="deepskyblue", height=225)

    return fig


def kpi_9():
    n = len(pd.unique(pf['State']))
    fig = go.Figure(go.Indicator(
        mode="number",
        title={"text": "<span style='color:white'><b>No. of states in precipitation data</b></span>"},
        value=n,
        number={'font_color': 'white'},
        # delta={'position': "top", 'reference': 320},
        domain={'x': [0, 1], 'y': [0, 1]}))

    fig.update_layout(paper_bgcolor="gold", height=225)

    return fig


def consumption_forecast():
    fig = px.bar(cf, x="Year", y=["Overall Consumption", "Irrigation", "Household Consumption",
                                  "Industrial Water Demand ", "Energy", "Other"], barmode="group")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
image_filename = 'Circle-icons-water.svg.png'  # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

page_0_layout = html.Div(children=[
    dbc.Navbar(
        [
            # Use row and col to control vertical alignment of logo / brand
            html.Img(src="https://freesvg.org/img/1413121417.png", height=30, width=30),
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand(html.B(html.I("PAWA"), style={"color": "DodgerBlue"})), className="ml-2"),
                    # dbc.NavLink("Home", href="#"),
                    # dbc.NavLink("Dash1", href="#"),
                    # dbc.NavLink("Dash2", href="#"),
                    # dbc.NavLink("Dash3", href="#"),
                    # dbc.NavLink("Dash4", href="#"),
                ],
                # dbc.NavLink("Home", href="#"),
                # dbc.NavLink("Dash1", href="#"),
                # dbc.NavLink("Dash2", href="#"),
                # dbc.NavLink("Dash3", href="#"),
                # dbc.NavLink("Dash4", href="#"),
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("RWH", href="/dash1")),
                dbc.NavItem(dbc.NavLink("Historical trends", href="/dash2")),
                dbc.NavItem(dbc.NavLink("Predictions", href="/dash3")),
                dbc.NavItem(dbc.NavLink("Storage", href="/dash4")),
                dbc.NavItem(dbc.NavLink("Report", href="/dash5")),
            ],
            )
        ],
        className="mb-0",
        # dark=True

    ),
    html.Iframe(src="https://analytics.zoho.in/open-view/187821000000002277",
                style={"height": "100%", "width": "100%", "overflow": "hidden"})
], style={"height": "657px", "left": "0", "right": "0", "bottom": "0", "top": "0"})

page_1_layout = html.Div(children=[
    dbc.Navbar(
        [
            # Use row and col to control vertical alignment of logo / brand
            html.Img(src="https://freesvg.org/img/1413121417.png", height=30, width=30),
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand(html.B(html.I("PAWA"), style={"color": "DodgerBlue"})), className="ml-2"),
                    # dbc.NavLink("Home", href="#"),
                    # dbc.NavLink("Dash1", href="#"),
                    # dbc.NavLink("Dash2", href="#"),
                    # dbc.NavLink("Dash3", href="#"),
                    # dbc.NavLink("Dash4", href="#"),
                ],
                # dbc.NavLink("Home", href="#"),
                # dbc.NavLink("Dash1", href="#"),
                # dbc.NavLink("Dash2", href="#"),
                # dbc.NavLink("Dash3", href="#"),
                # dbc.NavLink("Dash4", href="#"),
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("RWH", href="/dash1")),
                dbc.NavItem(dbc.NavLink("Historical trends", href="/dash2")),
                dbc.NavItem(dbc.NavLink("Predictions", href="/dash3")),
                dbc.NavItem(dbc.NavLink("Storage", href="/dash4")),
                dbc.NavItem(dbc.NavLink("Report", href="/dash5")),
            ],
            )
        ],
        className="mb-0"

    ),
    dbc.Col([
        html.H3("Historical Trends", style={"align": "center"})
    ], className="container text-center p-3 mb-4 bg-dark text-white", style={"width": "100%"}),

    html.Div(
        [

        ]
    ),
    html.Div(
        [
            dcc.Graph(id='KPI_precipitation', figure=kpi_1())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_vp', figure=kpi_2())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_avgtemp', figure=kpi_3())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_mintemp', figure=kpi_4())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_cc', figure=kpi_5())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_mx', figure=kpi_6())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(children=[
        html.H5("Precipitation"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="states",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states],
                    value=all_states[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="districts")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='line-chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px'
              }),
    html.Div(children=[
        html.H5("Vapour Pressure"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="stats",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_v],
                    value=all_states_v[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="districs")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='vp_line_chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Average Temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="stat",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_a],
                    value=all_states_a[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="distric")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='a_line_chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Minimum temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="sta",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_m],
                    value=all_states_m[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="distri")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='m_line_chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Cloud Cover"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="st",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_c],
                    value=all_states_c[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="distr")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='c-line-chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'margin-bottom': '20px'
              }),
    html.Div(children=[
        html.H5("Maximum Temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="state_mx",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_mx],
                    value=all_states_mx[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="district_mx")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='mx-line-chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'margin-bottom': '20px'
              }),
    html.Div(children=[
        html.H5("Groundwater"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="states_gw",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_gw],
                    value=all_states_gw[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        dcc.Graph(id='gw_line_chart'),
    ], style={'width': '95%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'margin-bottom': '20px'
              }),
])

# prediction layouts
page_2_layout = html.Div(children=[
    dbc.Navbar(
        [
            # Use row and col to control vertical alignment of logo / brand
            html.Img(src="https://freesvg.org/img/1413121417.png", height=30, width=30),
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand(html.B(html.I("PAWA"), style={"color": "DodgerBlue"})), className="ml-2"),
                    # dbc.NavLink("Home", href="#"),
                    # dbc.NavLink("Dash1", href="#"),
                    # dbc.NavLink("Dash2", href="#"),
                    # dbc.NavLink("Dash3", href="#"),
                    # dbc.NavLink("Dash4", href="#"),
                ],
                # dbc.NavLink("Home", href="#"),
                # dbc.NavLink("Dash1", href="#"),
                # dbc.NavLink("Dash2", href="#"),
                # dbc.NavLink("Dash3", href="#"),
                # dbc.NavLink("Dash4", href="#"),
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("RWH", href="/dash1")),
                dbc.NavItem(dbc.NavLink("Historical trends", href="/dash2")),
                dbc.NavItem(dbc.NavLink("Predictions", href="/dash3")),
                dbc.NavItem(dbc.NavLink("Storage", href="/dash4")),
                dbc.NavItem(dbc.NavLink("Report", href="/dash5")),
            ],
            )
        ],
        className="mb-0"

    ),
    dbc.Col([
        html.H3("Predictions", style={"align": "center"})
    ], className="container text-center p-3 mb-4 bg-dark text-white", style={"width": "100%"}),

    html.Div(
        [

        ]
    ),
    html.Div(
        [
            dcc.Graph(id='KPI_rainfall_prediction', figure=kpi_7())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_rainfall_prediction', figure=kpi_8())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(
        [
            dcc.Graph(id='KPI_rainfall_prediction', figure=kpi_9())
        ]
        , style={'width': '32%',
                 'height': '100%',
                 'display': 'inline-block',
                 'margin-right': '10px',
                 'margin-left': '10px',
                 'margin-bottom': '10px'
                 }),
    html.Div(children=[
        html.H5("Top 10 states in amount of Precipitation"),
        html.Div(
            [
                html.H6("Year:"),
                dcc.Dropdown(
                    id="p_year_s",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in year],
                    value=year[0],
                    placeholder="Select a year"),

            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='p_line_chart_top_10_s'),
    ], style={'width': '45%',
              'height': '100%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Top 10 districts in amount of Precipitation"),
        html.Div(
            [
                html.H6("Year:"),
                dcc.Dropdown(
                    id="p_year",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in year],
                    value=year[0],
                    placeholder="Select a State"),

            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='p_line_chart_top_10'),
    ], style={'width': '45%',
              'height': '100%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Precipitation"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_states_p",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states],
                    value=all_states[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_districts_p")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr-line-chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px'
              }),
    html.Div(children=[
        html.H5("Vapour Pressure"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_states_v",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_v],
                    value=all_states_v[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_districts_v")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr_line_chart_vp'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Average Temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_states_a",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_a],
                    value=all_states_a[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_districts_a")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr_line_chart_a'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Minimum temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_states_min",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_m],
                    value=all_states_m[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_districts_min")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr_line_chart_min'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Cloud Cover"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_states_cc",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_c],
                    value=all_states_c[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_districts_cc")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr_line_chart_cc'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'margin-bottom': '20px'
              }),
    html.Div(children=[
        html.H5("Maximum Temperature"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="pr_state_mx",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_mx],
                    value=all_states_mx[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="pr_district_mx")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='pr_line_chart_mx'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '60px',
              'margin-bottom': '20px'
              }),
    html.Div(children=[
        html.H5("Soil Moisture:"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="sm_states",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_sm],
                    value=all_states_sm[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block'}),
        html.Div(
            [
                html.H6("District:"),
                dcc.Dropdown(
                    id="sm_districts")
            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='sm_line_chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Top 10 districts in amount Soil moisture"),
        html.Div(
            [
                html.H6("Year:"),
                dcc.Dropdown(
                    id="sm_year",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in year],
                    value=year[0],
                    placeholder="Select a State"),

            ],
            style={'width': '25%',
                   'display': 'inline-block'}),
        dcc.Graph(id='sm_line_chart_top_10'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '1px',
              'margin-left': '60px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
    html.Div(children=[
        html.H5("Consumption Forecast"),
        dcc.Graph(id='consumption', figure=consumption_forecast()),
    ], style={'width': '95%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '10px',
              'margin-left': '10px',
              'border': '5px',
              'border-filter': 'blur(3px)',
              }),
])

page_3_layout = html.Div(children=[
    dbc.Navbar(
        [
            # Use row and col to control vertical alignment of logo / brand
            html.Img(src="https://freesvg.org/img/1413121417.png", height=30, width=30),
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand(html.B(html.I("PAWA"), style={"color": "DodgerBlue"})), className="ml-2"),
                    # dbc.NavLink("Home", href="#"),
                    # dbc.NavLink("Dash1", href="#"),
                    # dbc.NavLink("Dash2", href="#"),
                    # dbc.NavLink("Dash3", href="#"),
                    # dbc.NavLink("Dash4", href="#"),
                ],
                # dbc.NavLink("Home", href="#"),
                # dbc.NavLink("Dash1", href="#"),
                # dbc.NavLink("Dash2", href="#"),
                # dbc.NavLink("Dash3", href="#"),
                # dbc.NavLink("Dash4", href="#"),
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("RWH", href="/dash1")),
                dbc.NavItem(dbc.NavLink("Historical trends", href="/dash2")),
                dbc.NavItem(dbc.NavLink("Predictions", href="/dash3")),
                dbc.NavItem(dbc.NavLink("Storage", href="/dash4")),
                dbc.NavItem(dbc.NavLink("Report", href="/dash5")),
            ],
            )
        ],
        className="mb-0",
        # dark=True

    ),
    html.Iframe(
        src="https://docs.google.com/spreadsheets/d/e/2PACX-1vT7l0mBESvHup2eT3pShifl0nLzYxnb7C8zfugt1oRq9A8VHPgNUBegeXuQ6w4tWWfrFDTN_DhYZt-n/pubhtml?gid=0&single=true",
        style={"height": "100%", "width": "100%", "overflow": "hidden"}),
    # html.Iframe(
        # src="https://public.tableau.com/views/Performanceassessment_Waterdashboarddefaultfont/STATE??:embed=yes&:tabs=yes&:toolbar=yes",
        # style={"height": "100%", "width": "100%", "overflow": "hidden"})
    html.Div(children=[
        html.H5("Storage reservoir full capacity"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="states_st",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_st],
                    value=all_states_st[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        # html.Div(
        #     [
        #         html.H6("District:"),
        #         dcc.Dropdown(
        #             id="districts_st")
        #     ],
        #     style={'width': '25%',
        #            'display': 'inline-block'}),
        dcc.Graph(id='st_line_chart'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'margin-bottom': '20px'
              }),
    html.Div(children=[
        html.H5("Storage reservoir current level"),
        html.Div(
            [
                html.H6("State:"),
                dcc.Dropdown(
                    id="states_st_cl",
                    options=[{
                        'label': i,
                        'value': i
                    } for i in all_states_st],
                    value=all_states_st[0],
                    placeholder="Select a State"),

            ],
            style={'width': '30%',
                   'display': 'inline-block',
                   }),
        # html.Div(
        #     [
        #         html.H6("District:"),
        #         dcc.Dropdown(
        #             id="districts_st")
        #     ],
        #     style={'width': '25%',
        #            'display': 'inline-block'}),
        dcc.Graph(id='st_line_chart_cl'),
    ], style={'width': '45%',
              'height': '50%',
              'display': 'inline-block',
              'margin-right': '60px',
              'margin-left': '10px',
              'margin-bottom': '20px'
              }),

], style={"height": "657px", "left": "0", "right": "0", "bottom": "0", "top": "0"})


page_4_layout = html.Div(children=[
    dbc.Navbar(
        [
            # Use row and col to control vertical alignment of logo / brand
            html.Img(src="https://freesvg.org/img/1413121417.png", height=30, width=30),
            dbc.Row(
                [
                    dbc.Col(dbc.NavbarBrand(html.B(html.I("PAWA"), style={"color": "DodgerBlue"})), className="ml-2"),
                    # dbc.NavLink("Home", href="#"),
                    # dbc.NavLink("Dash1", href="#"),
                    # dbc.NavLink("Dash2", href="#"),
                    # dbc.NavLink("Dash3", href="#"),
                    # dbc.NavLink("Dash4", href="#"),
                ],
                # dbc.NavLink("Home", href="#"),
                # dbc.NavLink("Dash1", href="#"),
                # dbc.NavLink("Dash2", href="#"),
                # dbc.NavLink("Dash3", href="#"),
                # dbc.NavLink("Dash4", href="#"),
            ),
            dbc.Nav([
                dbc.NavItem(dbc.NavLink("RWH", href="/dash1")),
                dbc.NavItem(dbc.NavLink("Historical trends", href="/dash2")),
                dbc.NavItem(dbc.NavLink("Predictions", href="/dash3")),
                dbc.NavItem(dbc.NavLink("Storage", href="/dash4")),
                dbc.NavItem(dbc.NavLink("Report", href="/dash5")),
            ],
            )
        ],
        className="mb-0",
        # dark=True

    ),
    html.Iframe(
        src="https://drive.google.com/embeddedfolderview?id=184Jfz5uKCp9szIj6mG9YqOvBSNZIgiTL#grid",
        style={"height": "100%", "width": "100%", "overflow": "hidden"}),
], style={"height": "657px", "left": "0", "right": "0", "bottom": "0", "top": "0"})


@app.callback(
    [Output("districts", "options"), Output("districts", "value")],
    [Input("states", "value")])
def update_pr(state):
    temp = df.State.isin([state])
    temp1 = df[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    [Output("districs", "options"), Output("districs", "value")],
    [Input("stats", "value")])
def update_vp(state):
    temp = df1.State.isin([state])
    temp1 = df1[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    [Output("distric", "options"), Output("distric", "value")],
    [Input("stat", "value")])
def update_vp(state):
    temp = df2.State.isin([state])
    temp1 = df2[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    [Output("distri", "options"), Output("distri", "value")],
    [Input("sta", "value")])
def update_vp(state):
    temp = df3.State.isin([state])
    temp1 = df3[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    [Output("distr", "options"), Output("distr", "value")],
    [Input("st", "value")])
def update_vp(state):
    temp = df4.State.isin([state])
    temp1 = df4[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    [Output("district_mx", "options"), Output("district_mx", "value")],
    [Input("state_mx", "value")])
def update_vp(state):
    temp = df5.State.isin([state])
    temp1 = df5[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


# @app.callback(
#     [Output("districts_gw", "options"), Output("districts_gw", "value")],
#     [Input("states_gw", "value")])
# def update_vp(state):
#     temp = gw.STATE.isin([state])
#     temp1 = gw[temp]
#     new_dist = temp1['DISTRICT'].unique()
#     new_dist = list(new_dist)
#     return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


# @app.callback(
#     [Output("districts_st", "options"), Output("districts_st", "value")],
#     [Input("states_st", "value")])
# def update_vp(state):
#     temp = st.State.isin([state])
#     temp1 = st[temp]
#     new_dist = temp1['District'].unique()
#     new_dist = list(new_dist)
#     return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("line-chart", "figure"),
    [Input("districts", "value")])
def update_line_chart(district):
    mask = df.District.isin([district])
    fig = px.area(df[mask], x="Year", y="Sum", color_discrete_map={'German Shephard': 'rgb(255,0,0)'})
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("vp_line_chart", "figure"),
    [Input("districs", "value")])
def update_line_chart(district):
    mask = df1.District.isin([district])
    fig = px.area(df1[mask], x="Year", y="Sum")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("a_line_chart", "figure"),
    [Input("distric", "value")])
def update_line_chart(district):
    mask = df2.District.isin([district])
    fig = px.line(df2[mask], x="Year", y="Sum", color_discrete_sequence=["orange"], line_shape='spline')
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("m_line_chart", "figure"),
    [Input("distri", "value")])
def update_line_chart(district):
    mask = df3.District.isin([district])
    fig = px.line(df3[mask], x="Year", y="Sum", color_discrete_sequence=["green"])
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("c-line-chart", "figure"),
    [Input("distr", "value")])
def update_line_chart(district):
    mask = df4.District.isin([district])
    fig = px.bar(df4[mask], x="Year", y="Sum", color='Sum')
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("mx-line-chart", "figure"),
    [Input("district_mx", "value")])
def update_line_chart(district):
    mask = df5.District.isin([district])
    fig = px.scatter(df5[mask], x="Year", y="Sum")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("gw_line_chart", "figure"),
    [Input("states_gw", "value")])
def update_line_chart(state):
    mask = gw.STATE.isin([state])
    fig = px.area(gw[mask], y=col_gw, x="DISTRICT")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("st_line_chart", "figure"),
    [Input("states_st", "value")])
def update_line_chart(state):
    mask = st.State.isin([state])
    fig = px.bar(st[mask], x="Reservoir Name", y="Full Reservoir Level (m)")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("st_line_chart_cl", "figure"),
    [Input("states_st_cl", "value")])
def update_line_chart(state):
    mask = st.State.isin([state])
    fig = px.bar(st[mask], x="Reservoir Name", y="Current Reservoir Level (m)", color_discrete_sequence=['red'])
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


# prediction callbacks


@app.callback(
    [Output("pr_districts_p", "options"), Output("pr_districts_p", "value")],
    [Input("pr_states_p", "value")])
def update_pr_p(state):
    temp = pf.State.isin([state])
    temp1 = pf[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr-line-chart", "figure"),
    [Input("pr_districts_p", "value")])
def update_line_chart(district):
    mask = pf.District.isin([district])
    fig = px.bar(pf[mask], x="Month", y=['2021', '2022'], color_discrete_map={'German Shephard': 'rgb(255,0,0)'},
                 barmode='group')
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    [Output("pr_districts_v", "options"), Output("pr_districts_v", "value")],
    [Input("pr_states_v", "value")])
def update_pr_v(state):
    temp = pf1.State.isin([state])
    temp1 = pf1[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr_line_chart_vp", "figure"),
    [Input("pr_districts_v", "value")])
def update_line_chart(district):
    mask = pf1.District.isin([district])
    fig = px.bar(pf1[mask], x="Month", y=['2021', '2022'], color_discrete_sequence=['orange', 'blue'],
                 barmode='group')
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    [Output("pr_districts_a", "options"), Output("pr_districts_a", "value")],
    [Input("pr_states_a", "value")])
def update_pr_v(state):
    temp = pf2.State.isin([state])
    temp1 = pf2[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr_line_chart_a", "figure"),
    [Input("pr_districts_a", "value")])
def update_line_chart(district):
    mask = pf2.District.isin([district])
    fig = px.bar(pf2[mask], x="Month", y=['2021', '2022'], color_discrete_sequence=['aqua', 'lime'])
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    [Output("pr_districts_min", "options"), Output("pr_districts_min", "value")],
    [Input("pr_states_min", "value")])
def update_pr_v(state):
    temp = pf3.State.isin([state])
    temp1 = pf3[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr_line_chart_min", "figure"),
    [Input("pr_districts_min", "value")])
def update_line_chart(district):
    mask = pf3.District.isin([district])
    fig = px.area(pf3[mask], x="Month", y=['2021', '2022'], color_discrete_sequence=['purple', 'magenta'])
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    [Output("pr_districts_cc", "options"), Output("pr_districts_cc", "value")],
    [Input("pr_states_cc", "value")])
def update_pr_cc(state):
    temp = pf4.State.isin([state])
    temp1 = pf4[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr_line_chart_cc", "figure"),
    [Input("pr_districts_cc", "value")])
def update_line_chart(district):
    mask = pf4.District.isin([district])
    fig = px.bar(pf4[mask], x=['2021', '2022'], y="Month", color_discrete_sequence=['red', 'yellow'], orientation="h")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    [Output("pr_district_mx", "options"), Output("pr_district_mx", "value")],
    [Input("pr_state_mx", "value")])
def update_pr_cc(state):
    temp = pf5.State.isin([state])
    temp1 = pf5[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("pr_line_chart_mx", "figure"),
    [Input("pr_district_mx", "value")])
def update_line_chart(district):
    mask = pf5.District.isin([district])
    fig = px.area(pf5[mask], x="Month", y=['2021', '2022'], color_discrete_sequence=['red', 'yellow'])
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


# soil moisture callbacks
@app.callback(
    [Output("sm_districts", "options"), Output("sm_districts", "value")],
    [Input("sm_states", "value")])
def update_pr_cc(state):
    temp = soil_df.State.isin([state])
    temp1 = soil_df[temp]
    new_dist = temp1['District'].unique()
    new_dist = list(new_dist)
    return [{'label': i, 'value': i} for i in new_dist], new_dist[0]


@app.callback(
    Output("sm_line_chart", "figure"),
    [Input("sm_districts", "value")])
def update_line_chart(district):
    mask = soil_df.District.isin([district])
    fig = px.bar(soil_df[mask], x="Season", y="Pasm", color="Year")
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("sm_line_chart_top_10", "figure"),
    [Input("sm_year", "value")])
def update_line_chart(year1):
    mask = soil_df.loc[soil_df['Year'] == year1]
    new = mask.groupby("District", as_index=False).agg({'Pasm': ['sum']})
    new.columns = new.columns.droplevel(1)
    new = new.sort_values(by=['Pasm'], ascending=False)
    new = new[:10]
    fig = px.pie(new, values='Pasm', names='District', hole=.3)
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10)
    )
    return fig


@app.callback(
    Output("p_line_chart_top_10", "figure"),
    [Input("p_year", "value")])
def update_line_chart(year1):
    mask = pf[['District', str(year1)]]
    new = mask.groupby("District", as_index=False).agg({str(year1): ['sum']})
    new.columns = new.columns.droplevel(1)
    new = new.sort_values(by=[str(year1)], ascending=False)
    new = new[:10]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=new['District'], y=new[str(year1)], mode='lines+markers'))
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10),
        height=450
    )
    return fig


@app.callback(
    Output("p_line_chart_top_10_s", "figure"),
    [Input("p_year_s", "value")])
def update_line_chart(year1):
    mask = pf[['State', str(year1)]]
    new = mask.groupby("State", as_index=False).agg({str(year1): ['sum']})
    new.columns = new.columns.droplevel(1)
    new = new.sort_values(by=[str(year1)], ascending=False)
    new = new[:10]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=new['State'], y=new[str(year1)], mode='lines+markers', fill='tozeroy',
                             fillcolor='rgba(255,0,0,0.5)', line_color='#ff0000'))
    fig.update_xaxes(visible=True, fixedrange=True)
    fig.update_yaxes(visible=True, fixedrange=True)
    fig.update_layout(
        showlegend=True,
        plot_bgcolor="white",
        margin=dict(t=10, l=10, b=10, r=10),
        height=450
    )
    return fig


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dash1':
        return page_0_layout
    elif pathname == '/dash2':
        return page_1_layout
    elif pathname == '/dash3':
        return page_2_layout
    elif pathname == '/dash4':
        return page_3_layout
    elif pathname == '/dash5':
        return page_4_layout
    else:
        return page_0_layout
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(debug=False)
