from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
import numpy as np

app = Dash(__name__, external_stylesheets=[dbc.themes.LITERA])
app.title = 'MF Data Analysis'

#---------------------------------------------------------------------
# Import files
#---------------------------------------------------------------------

monthly_df = pd.read_csv('monthly_df.csv',index_col= 0)
qstates_df = pd.read_csv('qstates_df.csv',index_col= 0)
qnation_df = pd.read_csv('qnation_df.csv',index_col= 0)
state_codes = pd.read_excel('StateGOVcodes.xlsx')

# Dropdown 
states_lst = []
for state in list(state_codes['StateName'].unique()):
    states_lst += [{'label': state , 'value': state}]

#---------------------------------------------------------------------
# Plots
#---------------------------------------------------------------------

# Tab 3 plot
plot3 = px.line(qnation_df, x='DATE', y='HIGHWAY_GALLONS', color='MF_num',
        labels = {
            'DATE': 'Date',
            'HIGHWAY_GALLONS' : 'Gallons',
            'MF_num': 'MF Codes'
        },
        title="<b>Motor Fuels: Highway Consumption<b>",
        color_discrete_sequence=["blue", "red", "#00CC96"]) #change later

plot3.update_layout(
    plot_bgcolor = "#FFFFFF",
    font_family= "Helvetica Neue",
    font_color="black",
    title_font_color="black",
    title_font_size= 25,
    legend_title_font_color="black")

plot3.update_xaxes(showline = True, linewidth=2, linecolor='black',
                showgrid=True, gridwidth=1, gridcolor='lightgrey')
plot3.update_yaxes(showline = True, linewidth=2, linecolor='black',
                showgrid=True, gridwidth=1, gridcolor='lightgrey')

#---------------------------------------------------------------------
# App layout
#---------------------------------------------------------------------
app.layout = html.Div([
    
    html.H1('Motor Fuels: Highway Consumption Analysis'),
    dcc.Tabs([
        dcc.Tab(value = 'tab1',
                label = 'Monthly by state',
                children = [
                    html.H5("Select state"),
                    dcc.Dropdown(id= 'sel_state1', options = states_lst,
                                 multi = False, value = 'Alabama',  style = {'width': '40%'}),
                    dcc.Graph( id = 'plot1')]
                ),
        dcc.Tab(value = 'tab2',
                label = 'Quarterly by state', 
                children = [
                    html.H5("Select state"),
                    dcc.Dropdown(id= 'sel_state2', options = states_lst,
                                multi = False, value = 'Alabama', style = {'width': '40%'}),
                    dcc.Graph(id = 'plot2')]
                    ),
         dcc.Tab(value = 'tab3',
                 label = 'Quarterly nationwide', 
                children = [
                    # html.H5("Select state"),
                    # dcc.Dropdown(id= 'sel_state3', options = states_lst,
                    #             multi = False, value = 'Alabama', style = {'width': '40%'}),
                    dcc.Graph(id = 'plot3', figure = plot3)]
                    )
    ])
])

#---------------------------------------------------------------------
#  Connect Plotly graphs with Dash Components
#---------------------------------------------------------------------

# Tab 1
@app.callback(
    Output('plot1', 'figure'),
    Input('sel_state1', 'value'),
)

def update_plot1(sel_state1):
    df = monthly_df[(monthly_df['STATE'] == sel_state1)]

    fig = px.line(df, x='DATE', y='HIGHWAY_GALLONS', color='MF_num',
            labels = {
                'DATE': 'Date',
                'HIGHWAY_GALLONS' : 'Gallons',
                'MF_num': 'MF Codes'
            },
            title="<b>Motor Fuels: Highway Consumption for {}<b>".format(sel_state1),
            color_discrete_sequence=["blue", "red", "#00CC96"]) #change later

    fig.update_layout(
        plot_bgcolor = "#FFFFFF",
        font_family= "Helvetica Neue",
        font_color="black",
        title_font_color="black",
        title_font_size= 25,
        legend_title_font_color="black")

    fig.update_xaxes(showline = True, linewidth=2, linecolor='black',
                    showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_yaxes(showline = True, linewidth=2, linecolor='black',
                    showgrid=True, gridwidth=1, gridcolor='lightgrey')
    return fig

# Tab 2
@app.callback(
    Output('plot2', 'figure'),
    Input('sel_state2', 'value'),
)

def update_plot2(sel_state2):
    df = qstates_df[(qstates_df['STATE'] == sel_state2)]

    fig = px.line(df, x='DATE', y='HIGHWAY_GALLONS', color='MF_num',
            labels = {
                'DATE': 'Date',
                'HIGHWAY_GALLONS' : 'Gallons',
                'MF_num': 'MF Codes'
            },
            title="<b>Motor Fuels: Highway Consumption for {}<b>".format(sel_state2),
            color_discrete_sequence=["blue", "red", "#00CC96"]) #change later

    fig.update_layout(
        plot_bgcolor = "#FFFFFF",
        font_family= "Helvetica Neue",
        font_color="black",
        title_font_color="black",
        title_font_size= 25,
        legend_title_font_color="black")

    fig.update_xaxes(showline = True, linewidth=2, linecolor='black',
                    showgrid=True, gridwidth=1, gridcolor='lightgrey')
    fig.update_yaxes(showline = True, linewidth=2, linecolor='black',
                    showgrid=True, gridwidth=1, gridcolor='lightgrey')
    return fig

# # Tab 3 plot
# plot3 = px.line(qnation_df, x='DATE', y='HIGHWAY_GALLONS', color='MF_num',
#         labels = {
#             'DATE': 'Date',
#             'HIGHWAY_GALLONS' : 'Gallons',
#             'MF_num': 'MF Codes'
#         },
#         title="<b>Motor Fuels: Highway Consumption<b>",
#         color_discrete_sequence=["blue", "red", "#00CC96"]) #change later

# plot3.update_layout(
#     plot_bgcolor = "#FFFFFF",
#     font_family= "Helvetica Neue",
#     font_color="black",
#     title_font_color="black",
#     title_font_size= 25,
#     legend_title_font_color="black")

# plot3.update_xaxes(showline = True, linewidth=2, linecolor='black',
#                 showgrid=True, gridwidth=1, gridcolor='lightgrey')
# plot3.update_yaxes(showline = True, linewidth=2, linecolor='black',
#                 showgrid=True, gridwidth=1, gridcolor='lightgrey')
    



if __name__ == '__main__':
    app.run_server(debug=True)