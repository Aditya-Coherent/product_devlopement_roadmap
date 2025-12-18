import csv
import json

# Read the CSV file
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

# Month mapping for "Jan - Dec" format
month_expansion = {
    'Jan -  Dec': months_list,
    'January': ['January'],
    'February': ['February'],
    'March': ['March'],
    'April': ['April'],
    'May': ['May'],
    'June': ['June'],
    'July': ['July'],
    'August': ['August'],
    'September': ['September'],
    'October': ['October'],
    'November': ['November'],
    'December': ['December']
}

current_element = None
current_category = 'Web Development'

with open('public/web team.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Get the element - if it's empty, use the current element
        if row['Elements'].strip():
            current_element = row['Elements'].strip()
        
        element = current_element if current_element else 'Other'
        
        task = row['Task'].strip() if row['Task'] else ''
        
        # Skip rows with empty tasks
        if not task:
            continue
        
        monthly_quantifiable = row['Monthly quantifiable or not (to measure outcome)'].strip() if row['Monthly quantifiable or not (to measure outcome)'] else ''
        monthly_task = row['Monthly Task'].strip() if row['Monthly Task'] else ''
        
        # Get the month or months
        month_str = row['Month'].strip() if row['Month'] else 'January'
        
        # Expand months
        if month_str in month_expansion:
            months_to_add = month_expansion[month_str]
        else:
            months_to_add = ['January']
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': current_category,
                'element': element,
                'task': task,
                'monthlyTask': monthly_task,
                'monthlyQuantifiable': monthly_quantifiable,
                'team': 'website'
            }
            data.append(entry)

# Write to JSON file
with open('public/website-development-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created website-development-data.json with {len(data)} entries")

