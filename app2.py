import streamlit as st
import ee
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Initialize Google Earth Engine
ee.Initialize()

def get_land_area(region):
    # Define the region of interest
    if region == "West Africa":
        geometry = ee.Geometry.Polygon([[-18.0, 4.0], [-18.0, 20.0], [24.0, 20.0], [24.0, 4.0]])
    elif region == "East Africa":
        geometry = ee.Geometry.Polygon([[24.0, -12.0], [52.0, -12.0], [52.0, 5.0], [24.0, 5.0]])
    elif region == "Southern Africa":
        geometry = ee.Geometry.Polygon([[10.0, -35.0], [40.0, -35.0], [40.0, -10.0], [10.0, -10.0]])

    # Load the land cover dataset
    landcover = ee.ImageCollection("COPERNICUS/Landcover/100m/Proba-V-C3/Global").filterBounds(geometry)

    # Calculate the land area over time
    land_area = []
    for year in range(2015, 2024):
        image = landcover.filter(ee.Filter.calendarRange(year, year, 'year')).first()
        area = image.select('discrete_classification').multiply(10000).reduceRegion(
            reducer=ee.Reducer.sum(), geometry=geometry, scale=100).get('discrete_classification')
        land_area.append(area.getInfo())

    # Create a pandas DataFrame
    df = pd.DataFrame({'Year': range(2015, 2024), 'Land Area (km^2)': land_area})
    return df

def get_emissions(region):
    # Define the region of interest
    if region == "West Africa":
        geometry = ee.Geometry.Polygon([[-18.0, 4.0], [-18.0, 20.0], [24.0, 20.0], [24.0, 4.0]])
    elif region == "East Africa":
        geometry = ee.Geometry.Polygon([[24.0, -12.0], [52.0, -12.0], [52.0, 5.0], [24.0, 5.0]])
    elif region == "Southern Africa":
        geometry = ee.Geometry.Polygon([[10.0, -35.0], [40.0, -35.0], [40.0, -10.0], [10.0, -10.0]])

    # Load the greenhouse gas emissions dataset
    emissions = ee.ImageCollection("CAMS/GHG/V2/CO2_CONSTANT_GRID").filterBounds(geometry)

    # Calculate the total emissions over time
    total_emissions = []
    for year in range(2015, 2024):
        image = emissions.filter(ee.Filter.calendarRange(year, year, 'year')).first()
        emission = image.select('CO2').reduceRegion(
            reducer=ee.Reducer.sum(), geometry=geometry, scale=10000).get('CO2')
        total_emissions.append(emission.getInfo())

    # Create a pandas DataFrame
    df = pd.DataFrame({'Year': range(2015, 2024), 'Total Emissions (tons)': total_emissions})
    return df

def get_precipitation(region):
    # Define the region of interest
    if region == "West Africa":
        geometry = ee.Geometry.Polygon([[-18.0, 4.0], [-18.0, 20.0], [24.0, 20.0], [24.0, 4.0]])
    elif region == "East Africa":
        geometry = ee.Geometry.Polygon([[24.0, -12.0], [52.0, -12.0], [52.0, 5.0], [24.0, 5.0]])
    elif region == "Southern Africa":
        geometry = ee.Geometry.Polygon([[10.0, -35.0], [40.0, -35.0], [40.0, -10.0], [10.0, -10.0]])

    # Load the precipitation dataset
    precipitation = ee.ImageCollection("ECMWF/ERA5/MONTHLY").filterBounds(geometry)

    # Calculate the total precipitation over time
    total_precipitation = []
    for year in range(2015, 2024):
        for month in range(1, 13):
            image = precipitation.filter(ee.Filter.calendarRange(year, year, 'year'))
            image = image.filter(ee.Filter.calendarRange(month, month, 'month')).first()
            precip = image.select('total_precipitation').reduceRegion(
                reducer=ee.Reducer.sum(), geometry=geometry, scale=10000).get('total_precipitation')
            total_precipitation.append(precip.getInfo())

    # Create a pandas DataFrame
    df = pd.DataFrame({'Year': np.repeat(range(2015, 2024), 12), 'Month': np.tile(range(1, 13), 9), 'Total Precipitation (mm)': total_precipitation})
    return df

def get_pollution(region):
    # Define the region of interest
    if region == "West Africa":
        geometry = ee.Geometry.Polygon([[-18.0, 4.0], [-18.0, 20.0], [24.0, 20.0], [24.0, 4.0]])
    elif region == "East Africa":
        geometry = ee.Geometry.Polygon([[24.0, -12.0], [52.0, -12.0], [52.0, 5.0], [24.0, 5.0]])
    elif region == "Southern Africa":
        geometry = ee.Geometry.Polygon([[10.0, -35.0], [40.0, -35.0], [40.0, -10.0], [10.0, -10.0]])

    # Load the air quality and pollution dataset
    pollution = ee.ImageCollection("COPERNICUS/S5P/OFFL/L3_NO2").filterBounds(geometry)

    # Calculate the average pollution levels over time
    pollution_levels = []
    for year in range(2015, 2024):
        image = pollution.filter(ee.Filter.calendarRange(year, year, 'year')).mean()
        level = image.select('tropospheric_NO2_column_number_density').reduceRegion(
            reducer=ee.Reducer.mean(), geometry=geometry, scale=5000).get('tropospheric_NO2_column_number_density')
        pollution_levels.append(level.getInfo())

    # Create a pandas DataFrame
    df = pd.DataFrame({'Year': range(2015, 2024), 'Pollution Levels (mol/m^2)': pollution_levels})
    return df

def get_temperature(region):
    # Define the region of interest
    if region == "West Africa":
        geometry = ee.Geometry.Polygon([[-18.0, 4.0], [-18.0, 20.0], [24.0, 20.0], [24.0, 4.0]])
    elif region == "East Africa":
        geometry = ee.Geometry.Polygon([[24.0, -12.0], [52.0, -12.0], [52.0, 5.0], [24.0, 5.0]])
    elif region == "Southern Africa":
        geometry = ee.Geometry.Polygon([[10.0, -35.0], [40.0, -35.0], [40.0, -10.0], [10.0, -10.0]])

    # Load the land surface temperature dataset
    temperature = ee.ImageCollection("MODIS/006/MOD11A2").filterBounds(geometry)

    # Calculate the average surface temperature over time
    surface_temperature = []
    for year in range(2015, 2024):
        image = temperature.filter(ee.Filter.calendarRange(year, year, 'year')).mean()
        temp = image.select('LST_Day_1km').reduceRegion(
            reducer=ee.Reducer.mean(), geometry=geometry, scale=1000).get('LST_Day_1km')
        surface_temperature.append(temp.getInfo())

    # Create a pandas DataFrame
    df = pd.DataFrame({'Year': range(2015, 2024), 'Surface Temperature (°C)': surface_temperature})
    return df

def display_correlations(region):
    # Retrieve the data for the selected region
    land_area = get_land_area(region)
    emissions = get_emissions(region)
    precipitation = get_precipitation(region)
    pollution = get_pollution(region)
    temperature = get_temperature(region)

    # Create a figure with multiple subplots
    fig = make_subplots(rows=3, cols=2, subplot_titles=("Land Area Changes", "Greenhouse Gas Emissions",
                                                       "Precipitation", "Air Pollution",
                                                       "Surface Temperature", "Correlations"))

    # Plot the land area changes
    fig.add_trace(go.Scatter(x=land_area['Year'], y=land_area['Land Area (km^2)'], mode='lines'), row=1, col=1)

    # Plot the emissions
    fig.add_trace(go.Scatter(x=emissions['Year'], y=emissions['Total Emissions (tons)'], mode='lines'), row=1, col=2)

    # Plot the precipitation
    fig.add_trace(go.Scatter(x=precipitation['Year'], y=precipitation['Total Precipitation (mm)'], mode='lines'), row=2, col=1)

    # Plot the pollution
    fig.add_trace(go.Scatter(x=pollution['Year'], y=pollution['Pollution Levels (mol/m^2)'], mode='lines'), row=2, col=2)

    # Plot the surface temperature
    fig.add_trace(go.Scatter(x=temperature['Year'], y=temperature['Surface Temperature (°C)'], mode='lines'), row=3, col=1)

    # Calculate the correlations
    correlations = pd.DataFrame({
        'Metric': ['Land Area', 'Emissions', 'Precipitation', 'Pollution', 'Temperature'],
        'Land Area': [1.0, land_area.corr(emissions), land_area.corr(precipitation), land_area.corr(pollution), land_area.corr(temperature)],
        'Emissions': [land_area.corr(emissions), 1.0, emissions.corr(precipitation), emissions.corr(pollution), emissions.corr(temperature)],
        'Precipitation': [land_area.corr(precipitation), emissions.corr(precipitation), 1.0, precipitation.corr(pollution), precipitation.corr(temperature)],
        'Pollution': [land_area.corr(pollution), emissions.corr(pollution), precipitation.corr(pollution), 1.0, pollution.corr(temperature)],
        'Temperature': [land_area.corr(temperature), emissions.corr(temperature), precipitation.corr(temperature), pollution.corr(temperature), 1.0]
    })

    # Plot the correlations
    fig.add_trace(go.Heatmap(x=correlations.columns, y=correlations['Metric'], z=correlations.values, colorscale='Viridis'), row=3, col=2)

    # Customize the layout
    fig.update_layout(height=800, width=1200, title_text=f"{region} - Environmental Metrics Correlations")
    st.plotly_chart(fig, use_container_width=True)

# Streamlit app
st.set_page_config(layout="wide")

# Sidebar for region selection
st.sidebar.title("Select Region")
region = st.sidebar.selectbox("", ["West Africa", "East Africa", "Southern Africa"])

# Display the correlations
display_correlations(region)