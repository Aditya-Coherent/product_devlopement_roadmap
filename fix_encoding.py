import json
import re

# Read the file with UTF-8 encoding
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Clean all string values
for item in data:
    for key in item:
        if isinstance(item[key], str):
            value = item[key]
            
            # Replace various dash/hyphen characters
            value = value.replace('–', '-')   # en-dash
            value = value.replace('—', '-')   # em-dash
            value = value.replace('−', '-')   # minus
            value = value.replace('‐', '-')   # hyphen
            value = value.replace('‑', '-')   # non-breaking hyphen
            value = value.replace('â€"', '-')  # encoded en-dash variant 1
            value = value.replace('â€"', '-')  # encoded en-dash variant 2
            
            # Replace smart quotes
            value = value.replace('"', '"')   # left double quote
            value = value.replace('"', '"')   # right double quote
            value = value.replace(''', "'")   # left single quote
            value = value.replace(''', "'")   # right single quote
            value = value.replace('â€œ', '"')  # encoded left quote
            value = value.replace('â€™', "'")  # encoded right quote
            
            item[key] = value

# Write back with ASCII-safe format
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=True)

print('✅ Fixed all special character encoding issues!')
print('All dashes and quotes have been normalized to ASCII equivalents')

