import json
from datetime import datetime

# Read the existing January data
with open('public/digital-marketing-data.json', 'r') as f:
    january_data = json.load(f)

# List of all months
months = ['January', 'February', 'March', 'April', 'May', 'June', 
          'July', 'August', 'September', 'October', 'November', 'December']

# Items to exclude from non-January months
exclude_elements = [
    'F. Schema Markup',  # On-Page SEO
    'Structure Data and Schema Mark-up'  # Technical SEO
]

all_data = []

for month in months:
    for item in january_data:
        # Skip schema markup items for non-January months
        if month != 'January' and item.get('element') in exclude_elements:
            continue
        
        # Create a copy of the item with the new month
        new_item = item.copy()
        new_item['month'] = month
        all_data.append(new_item)

# Write the updated data back to the JSON file
with open('public/digital-marketing-data.json', 'w') as f:
    json.dump(all_data, f, indent=2)

print(f"✅ Successfully replicated data for all 12 months!")
print(f"Total items: {len(all_data)}")
print(f"Schema Markup items kept only in January")

