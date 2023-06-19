# import pandas as pd
# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime
# import re
# import geopandas as gpd
import tensorflow as tf

model = tf.keras.models.load_model("cnn_model_3.h5")
# Display the model summary
model.summary()



# Load the CSV data
# data = pd.read_csv('data.csv')

# data.drop(["year","month","First Appearance_1","formatted_date"], inplace=True, axis = 1)

# # Function to scrape webpage and extract citizenship
# def get_citizenship(url):
#     response = requests.get(url)
#     if response.status_code == 200:
#         soup = BeautifulSoup(response.content, 'html.parser')
#         citizenship_info = soup.find('div', {'data-source': 'Citizenship'})
#         if citizenship_info is not None:
#             citizenship_value = citizenship_info.find('div', {'class': 'pi-data-value'}).text.strip()
#         else:
#             citizenship_value = 'N/A'
#     else:
#         citizenship_value = 'N/A'
#     return citizenship_value

# # Add 'citizenship' column to the original DataFrame
# data['citizenship'] = data['link'].apply(get_citizenship)

# # Save the updated DataFrame back to the CSV file
# data.to_csv('data_with_citizenship.csv', index=False)

# Convert the 'date' column to strings
# data['date'] = data['date'].astype(str)

# # Extract the month and year values
# data['month'] = data['date'].str.split('-', expand=True)[1]
# data['year'] = data['date'].str.split('-', expand=True)[0]

# # Replace missing or invalid values with defaults
# data['month'].fillna('01', inplace=True)
# data['year'].fillna('1900', inplace=True)

# # Create the formatted date column
# data['formatted_date'] = data['month'] + '/' + data['year']

# # # Save the updated dataset back to the same file
# data.to_csv("data.csv", index=False)

# import geopandas as gpd

# # Read the shapefile using geopandas
# shapefile_path = 'shapefile/SA2_2021_AUST_GDA2020.shp'
# gdf = gpd.read_file(shapefile_path)

# # Filter the GeoDataFrame based on the value of STE_NAME21
# filtered_gdf = gdf[gdf['STE_NAME21'] == 'Victoria']

# # Select only the desired columns
# selected_columns = ['SA2_NAME21', 'STE_NAME21', 'geometry']
# df = filtered_gdf[selected_columns]

# # Save the DataFrame to a CSV file
# csv_path = 'geo.csv'
# df.to_csv(csv_path, index=False)
