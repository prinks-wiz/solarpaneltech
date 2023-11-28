#Converting all the json file data into a single csv file for further analysis. 

import os
import json
import pandas as pd
import numpy as np
# Directory containing JSON files
directory_path = '/Users/prinks/Desktop/Sem 5/DAV LAB/Project/JSON DATA'

# List all files in the directory
all_files = os.listdir(directory_path)

# Filter out only JSON files
json_files = [file for file in all_files if file.endswith('.json')]

# Initialize an empty list to store DataFrames for each JSON file
data_frames = []

# Iterate over each JSON file
for json_file in json_files:
    # Construct the full path to the JSON file
    json_file_path = os.path.join(directory_path, json_file)

    # Load JSON data from the file
    with open(json_file_path, 'r') as file:
        json_data = file.read()

    # Parse JSON data
    data = json.loads(json_data)

    # Extract input data
    input_data = data['inputs']
    input_data_flattened = {'latitude': input_data['location']['latitude'],
                            'longitude': input_data['location']['longitude'],
                            'elevation': input_data['location']['elevation'],
                            'radiation_db': input_data['meteo_data']['radiation_db'],
                            'meteo_db': input_data['meteo_data']['meteo_db'],
                            'year_min': input_data['meteo_data']['year_min'],
                            'year_max': input_data['meteo_data']['year_max'],
                            'use_horizon': input_data['meteo_data']['use_horizon'],
                            'horizon_db': input_data['meteo_data']['horizon_db'],
                            'slope_value': input_data['mounting_system']['fixed']['slope']['value'],
                            'slope_optimal': input_data['mounting_system']['fixed']['slope']['optimal'],
                            'azimuth_value': input_data['mounting_system']['fixed']['azimuth']['value'],
                            'azimuth_optimal': input_data['mounting_system']['fixed']['azimuth']['optimal'],
                            'type': input_data['mounting_system']['fixed']['type'],
                            'technology': input_data['pv_module']['technology'],
                            'peak_power': input_data['pv_module']['peak_power'],
                            'system_loss': input_data['pv_module']['system_loss'],
                            'system_cost': input_data['economic_data']['system_cost'],
                            'interest': input_data['economic_data']['interest'],
                            'lifetime': input_data['economic_data']['lifetime']}

    # Create a DataFrame for input data
    input_df = pd.DataFrame([input_data_flattened])

    # Extract monthly output data
    monthly_data = data['outputs']['monthly']['fixed']

    # Create a DataFrame for monthly output data
    output_df = pd.DataFrame(monthly_data)

    # Merge input and output DataFrames
    result_df = pd.concat([input_df] * len(output_df), ignore_index=True)
    result_df = pd.concat([result_df, output_df], axis=1)

    # Append the resulting DataFrame to the list
    data_frames.append(result_df)

# Concatenate all DataFrames in the list
final_df = pd.concat(data_frames, ignore_index=True)

# Save the final DataFrame to a single CSV file
destination_path = '/Users/prinks/Desktop/Sem 5/DAV LAB/Project'
csv_output_path = os.path.join(destination_path, 'merged_output.csv')
final_df.to_csv(csv_output_path, index=False)

print(f"All DataFrames successfully merged and saved to '{csv_output_path}'.")

df = pd.read_csv('merged_output.csv')
fields_with_errors = {'latitude':[11.79,0.9],'longitude':[78.89,1.36],'slope_value':[45.58,11.4], 'azimuth_value':[12.64,68.19], 'peak_power':[6.72,1.35], 'system_loss':[11.17,2.11], 'system_cost':[38.12,3.62],'interest':[9.22,1.04],'lifetime':[17.74,5.5]}

# Introduce Gaussian errors to selected fields
for field in fields_with_errors:
    # Set the seed for reproducibility
    np.random.seed(42)
    
    # Generate random errors from a normal distribution
    print(fields_with_errors[field][0])
    errors = np.random.normal(loc=1, scale=0.5, size=len(df))
    
    # Add errors to the selected field

    df[field] += errors

df.to_csv('merged_output.csv')
print('fin')