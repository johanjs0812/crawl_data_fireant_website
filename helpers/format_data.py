import re
from unidecode import unidecode

def convert_to_safe_name(column_name):
    safe_name = column_name.replace(' ', '_')
    return safe_name

def clean_first_value(value):
    value = unidecode(value) 
    value = re.sub(r'[^\w\s]', '', value)
    value = re.sub(r'\s+', '_', value) 
    value = value.lower()
    return value