import os
import json

from config.setting import DIRECTORY_DATA

def ensure_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def convert_to_json2(final_df, stock):
    directory = f'{DIRECTORY_DATA}/{stock}'  
    print('direc', directory)
    ensure_directory(directory) 

    output_file = os.path.join(directory, f'{stock}_ten_years.json')
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(final_df, f, ensure_ascii=False, indent=4)
