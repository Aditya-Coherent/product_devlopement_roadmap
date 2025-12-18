import json
import csv

# Read the HR CSV file with proper CSV parsing to handle multi-line entries
json_data = []
current_month = None

# Month mapping
month_map = {
    'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
    'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
    'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
}

# Use CSV reader to properly handle quoted fields with newlines
with open('public/Book5.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    
    current_element = None
    
    for row in reader:
        if len(row) < 3:
            continue
        
        month_str = row[0].strip()
        element = row[1].strip()
        task = row[2].strip()
        
        # Skip empty rows
        if not task:
            continue
        
        # Update month if provided
        if month_str:
            month_abbr = month_str.split('-')[0]
            if month_abbr in month_map:
                current_month = month_map[month_abbr]
        
        # Update element if provided
        if element:
            current_element = element
        
        # Create entry with preserved newlines
        if current_month and current_element:
            # Preserve multi-line content as-is
            entry = {
                'month': current_month,
                'category': 'Human Resources',
                'element': current_element,
                'task': task,  # This will preserve newlines from CSV
                'monthlyTask': '',
                'monthlyQuantifiable': '',
                'team': 'human-resources'
            }
            json_data.append(entry)

# Write to JSON file
with open('public/Human-Resource-data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print('✅ Successfully updated Human-Resource-data.json!')
print(f'Total entries: {len(json_data)}')
print(f'Preserved all multi-line task entries from CSV')
