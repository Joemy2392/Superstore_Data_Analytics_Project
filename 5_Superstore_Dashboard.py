#-------------------------------------------------------------
# Superstore Analysis - Interactive Dashboard
#-------------------------------------------------------------

# 1. Import required libraries
#-------------------------------------------------------------
import pandas as pd
import numpy as np
import plotly.express as px
import dash
from dash import dcc, html, Input, Output, State
import os


# 2. Load cleaned Superstore Dataset
#--------------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "3_Cleaned_Superstore_Dataset.csv")
df = pd.read_csv(file_path)


# 3. Create a dash application
#-----------------------------------------------------------------------------
app = dash.Dash(__name__)
app.title = "Superstore Sales Dashboard"
server = app.server   # Exposed to gunicorn for rendering


# 4. Define/Build Dash App Layout
#-----------------------------------------------------------------------------
app.layout = html.Div(style={'fontFamily': 'Arial, sans-serif', 'padding': '20px', 'backgroundColor': '#f4f6f9'}, children=[

    # Header & Export Button
    html.Div([
        html.H1("Superstore Performance Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),
        html.Button("Export Filtered Data", id="btn-export", style={
            'padding': '10px 20px', 'backgroundColor': '#27ae60', 'color': 'white',
            'border': 'none', 'borderRadius': '5px', 'cursor': 'pointer', 'float': 'right'
        }),
        dcc.Download(id="download-dataframe-csv")
    ], style={'paddingBottom': '40px'}),

    # Filters
    html.Div([
        # Year Filter
        html.Div([
            html.Label("Select Year:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='year-filter',
                options=[{'label': 'All Years', 'value': 'All'}] + [{'label': str(y), 'value': y} for y in sorted(df['Year'].dropna().unique())],
                value='All',
                clearable=False,
                style={'width': '240px'}
            )
        ], style={'flex': '0 0 auto'}),

        # Category Filter
        html.Div([
            html.Label("Select Category:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='category-filter',
                options=[{'label': category, 'value': category} for category in sorted(df['Category'].dropna().unique())],
                value=df['Category'].dropna().unique().tolist(),
                multi=True,
                style={'width': '240px'}
            )
        ], style={'flex': '0 0 auto'}),

        # Region Filter
        html.Div([
            html.Label("Select Region:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='region-filter',
                options=[{'label': region, 'value': region} for region in sorted(df['Region'].dropna().unique())],
                value=df['Region'].dropna().unique().tolist(),
                multi=True,
                style={'width': '240px'}
            )
        ], style={'flex': '0 0 auto'}),

        # Segment Filter
        html.Div([
            html.Label("Select Segment:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='segment-filter',
                options=[{'label': segment, 'value': segment} for segment in sorted(df['Segment'].dropna().unique())],
                value=df['Segment'].dropna().unique().tolist(),
                multi=True,
                style={'width': '240px'}
            )
        ], style={'flex': '0 0 auto'}),

    ],style={'display': 'flex', 'flexDirection': 'row', 'alignItems': 'center', 'gap': '20px', 'marginBottom': '20px'}),


    # KPI Cards Row
    html.Div(id='kpi-cards', style={'display': 'flex', 'justifyContent': 'space-around', 'marginBottom': '20px'}),

    # Visualizations Grid
    html.Div([
        # Row 1: Line Chart & Bar Chart
        html.Div([
            dcc.Graph(id='line-chart', style={'flex': '1', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'}),
            dcc.Graph(id='bar-chart', style={'flex': '1', 'marginLeft': '10px', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'})
        ], style={'display': 'flex', 'flexDirection': 'row', 'marginBottom': '20px'}),

        # Row 2: Pie Chart & Box Plot
        html.Div([
            dcc.Graph(id='pie-chart', style={'flex': '1', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'}),
            dcc.Graph(id='box-plot', style={'flex': '1', 'marginLeft': '10px', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'})
        ], style={'display': 'flex', 'flexDirection': 'row', 'marginBottom': '20px'}),

        # Row 3: Top profitable products - Bar Chart
        html.Div([
            dcc.Graph(id='top-product-chart', style={'flex': '1', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'}),
            dcc.Graph(id='least-profit-chart', style={'flex': '1', 'marginLeft': '10px', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'})
        ],  style={'display': 'flex', 'flexDirection': 'row', 'marginBottom': '20px'}),

        # Row 4: Bar Chart -
        html.Div([
            dcc.Graph(id='profit-chart', style={'flex': '1', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'}),
            dcc.Graph(id='sunburst-chart', style={'flex': '1', 'marginLeft': '10px', 'marginRight': '10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'})
        ],  style={'display': 'flex', 'flexDirection': 'row', 'marginBottom': '20px'}),
    ])
])



# 5. Callbacks for Interactivity
#-------------------------------------------------------------------------------
@app.callback(
    [Output('kpi-cards', 'children'),
     Output('line-chart', 'figure'),
     Output('bar-chart', 'figure'),
     Output('pie-chart', 'figure'),
     Output('box-plot', 'figure'),
     Output('top-product-chart', 'figure'),
     Output('least-profit-chart', 'figure'),
     Output('profit-chart', 'figure'),
     Output('sunburst-chart', 'figure'),],
    [Input('year-filter', 'value'),
     Input('category-filter', 'value'),
     Input('region-filter', 'value'),
     Input('segment-filter', 'value'),
     ],
)

def update_dashboard(selected_year, selected_category, selected_region, selected_segment):
    # Complete dataset
    filtered_df = df.copy()

    # Apply year filter
    if selected_year != 'All':
        filtered_df = filtered_df[filtered_df['Year'] == selected_year]

    # Apply category filter
    if selected_category:
        filtered_df = filtered_df[filtered_df['Category'].isin(selected_category)]

    # Apply region filter
    if selected_region:
        filtered_df = filtered_df[filtered_df['Region'].isin(selected_region)]

    # Apply segment filter
    if selected_segment:
        filtered_df = filtered_df[filtered_df['Segment'].isin(selected_segment)]


    # --- KPI Calculations ---
    total_sales = filtered_df['Sales'].sum()
    total_profit = filtered_df['Profit'].sum()
    avg_order = filtered_df['Sales'].mean()

    # Create KPI UI elements
    card_style = {'backgroundColor': 'white', 'padding': '20px', 'borderRadius': '10px', 'textAlign': 'center', 'flex': '1', 'margin': '0 10px', 'boxShadow': '0 4px 8px 0 rgba(0,0,0,0.1)'}
    kpis = [
        html.Div([html.H3("Total Sales", style={'color': '#7f8c8d'}), html.H2(f"${total_sales:,.2f}", style={'color': '#2980b9'})], style=card_style),
        html.Div([html.H3("Total Profit", style={'color': '#7f8c8d'}), html.H2(f"${total_profit:,.2f}", style={'color': '#27ae60'})], style=card_style),
        html.Div([html.H3("Avg Order Value", style={'color': '#7f8c8d'}), html.H2(f"${avg_order:,.2f}", style={'color': '#8e44ad'})], style=card_style)
    ]

    # --- Visualizations ---
    # Plot 1. Line Chart: Trend over time
    monthly_sales = filtered_df.groupby('Month_Year')['Sales'].sum().reset_index().sort_values('Month_Year')
    fig_line = px.line(monthly_sales, x='Month_Year', y='Sales', title="Sales Trend Over Time", markers=True)
    fig_line.update_layout(xaxis_title="Month-Year", yaxis_title="Total Sales ($)")

    # Plot 2. Bar Chart: Category vs Sales
    cat_sales = filtered_df.groupby('Category')['Sales'].sum().reset_index()
    fig_bar = px.bar(cat_sales, x='Category', y='Sales', title="Total Sales by Category", color='Category')

    # Plot 3. Pie Chart: Distribution by Region
    fig_pie = px.pie(filtered_df, names='Region', values='Sales', title="Sales Distribution by Region", hole=0.3)

    # Plot 4. Box Plot: Spread of Sales by Category
    # Capping extremely high outliers for better visualization readability, or using log scale
    fig_box = px.box(filtered_df, x='Category', y='Sales', title="Spread of Sales by Category (Log Scale)", color='Category')
    fig_box.update_layout(yaxis_type="log")


    # Plot 5. Top 10 Most Profitable Products
    top_product = filtered_df.groupby(['Product ID'])['Profit'].sum().reset_index().sort_values('Profit', ascending= False).head(10)
    fig_top_prod = px.bar(top_product, x='Product ID', y='Profit', color_discrete_sequence=['green'],
        title='Top 10 Most Profitable Products', labels={'Profit': 'Total Profit ($)', 'Product ID':'Product ID'})
    fig_top_prod.update_layout(xaxis_tickangle=-45)


    # Plot 6. Top 10 Loss-Making Products
    least_product = filtered_df.groupby(['Product ID'])['Profit'].sum().reset_index().sort_values('Profit').head(10)
    fig_least_prod = px.bar(least_product, x='Profit', y='Product ID', color_discrete_sequence=['red'], title='Top 10 Loss-Making Products')
    fig_least_prod.update_layout(xaxis_tickangle=-45, xaxis_title="Total Profit ($)", yaxis_title="Product ID", yaxis={'autorange': 'reversed'})

    # Plot 7. Bar Chart
    subcat_profit = filtered_df.groupby('Sub-Category')['Profit'].sum().sort_values().reset_index()
    subcat_profit['Color'] = np.where(subcat_profit['Profit'] < 0, 'Loss', 'Profit')

    fig_profit = px.bar(subcat_profit, x='Profit', y='Sub-Category', orientation='h',
        color='Color', color_discrete_map={'Profit': 'green', 'Loss': 'red'},
        title='Total Profit by Sub-Category', labels={'Profit': 'Profit ($)'})


    # Plot 8. Sunburst Chart: Category to Sub-Category Breakdown
    fig_sunburst = px.sunburst(filtered_df, path=['Category', 'Sub-Category'], values='Sales', title="Sales Breakdown: Category to Sub-Category")

    return kpis, fig_line, fig_bar, fig_pie, fig_box, fig_top_prod, fig_least_prod, fig_profit, fig_sunburst





# 6. Export Data Callback
#----------------------------------------------------------------

@app.callback(
    Output("download-dataframe-csv", "data"),
    Input("btn-export", "n_clicks"),
    State('year-filter', 'value'),
    State('category-filter', 'value'),
    State('region-filter', 'value'),
    State('segment-filter', 'value'),
    prevent_initial_call=True
)
def export_data(n_clicks, selected_year, selected_category, selected_region, selected_segment):

    # Complete dataset
    export_df  = df.copy()

    # Apply year filter
    if selected_year != 'All':
        export_df = export_df[export_df['Year'] == selected_year]

    # Apply category filter
    if selected_category:
        export_df = export_df[export_df['Category'].isin(selected_category)]

    # Apply region filter
    if selected_region:
        export_df = export_df[export_df['Region'].isin(selected_region)]

    # Apply segment filter
    if selected_segment:
        export_df = export_df[export_df['Segment'].isin(selected_segment)]

    # Export filtered data
    return dcc.send_data_frame(export_df.to_csv, f"Superstore_Data_{selected_region}_{selected_segment}_{selected_category}_{selected_year}.csv", index=False)



# 7. Run the application
#----------------------------------------------------------------------------
if __name__ == '__main__':
    # Runs on http://127.0.0.1:8050/ by default
    app.run(debug=True, port=2392)

