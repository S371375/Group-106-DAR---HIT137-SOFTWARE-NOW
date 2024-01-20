import os
import pandas as pd
from zipfile import ZipFile

# Specify the path to the zipped folder
zipped_folder_path = 'Assignment 2.zip'
extracted_folder_path = 'extracted_files'

# Extract the contents of the zipped folder
with ZipFile(zipped_folder_path, 'r') as zip_ref:
    zip_ref.extractall(extracted_folder_path)

# List all CSV files in the extracted folder
csv_files = [file for file in os.listdir(extracted_folder_path) if file.endswith('.csv')]

# Create an empty list to store text from all CSV files
all_texts = []

# Iterate through each CSV file
for csv_file in csv_files:
    # Read the CSV file
    df = pd.read_csv(os.path.join(extracted_folder_path, csv_file))
    
    # Try 'TEXT' column, if not present, try 'SHORT-TEXT' column
    text_column_name = 'TEXT' if 'TEXT' in df.columns else 'SHORT-TEXT'
    
    # Concatenate text from the specified column
    all_texts.extend(df[text_column_name].astype(str).tolist())

# Combine all texts into a single string
combined_text = '\n'.join(all_texts)

# Write the combined text to a single .txt file
output_txt_path = 'Qtask1_output.txt'
with open(output_txt_path, 'w', encoding='utf-8') as txt_file:
    txt_file.write(combined_text)

# Optionally, print a message indicating success
print(f"Text extracted from {len(csv_files)} CSV files and saved to {output_txt_path}.")
