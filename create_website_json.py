import json

# Read the CSV file line by line to properly handle the structure
csv_lines = []
with open('public/web team.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    # Skip header
    for line in lines[1:]:
        if line.strip():
            csv_lines.append(line.strip())

json_data = []
current_category = None
current_element = None

# Process line by line
for line in csv_lines:
    parts = [part.strip() for part in line.split(',', 6)]  # Split into 7 parts max
    
    # Extract values
    team = parts[0] if len(parts) > 0 else ''
    elements = parts[1] if len(parts) > 1 else ''
    sub_elements = parts[2] if len(parts) > 2 else ''
    task = parts[3] if len(parts) > 3 else ''
    quantifiable = parts[4] if len(parts) > 4 else ''
    monthly_task = parts[5] if len(parts) > 5 else ''
    month = parts[6] if len(parts) > 6 else 'January'
    
    # Skip if no task
    if not task:
        continue
    
    # Update category if provided
    if team:
        current_category = team
    
    # Update element if provided and not Na
    if elements and elements.lower() != 'na':
        current_element = elements
    
    # Determine months
    is_january_only = False
    if 'January' in month and 'Dec' not in month:
        is_january_only = True
        months = ['January']
    elif 'Jan' in month and 'Dec' in month:
        months = ['January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December']
    else:
        months = ['January']
    
    # Create entries for each month
    for m in months:
        entry = {
            'month': m,
            'category': current_category or 'Web Development',
            'element': current_element or 'Website Design and Development',
            'task': task,
            'monthlyTask': monthly_task if monthly_task else '',
            'monthlyQuantifiable': quantifiable if quantifiable else '',
            'team': 'website'
        }
        json_data.append(entry)

# Write to JSON file
with open('public/website-development-data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

# Fix encoding issues
with open('public/website-development-data.json', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace problematic Unicode sequences and dashes
content = content.replace('\u00e2\u20ac\u201c', '-')
content = content.replace('\u00e2\u20ac\u201d', '-')
content = content.replace('–', '-')
content = content.replace('—', '-')

# Write back
with open('public/website-development-data.json', 'w', encoding='utf-8') as f:
    f.write(content)

print('✅ Successfully updated website-development-data.json!')
print(f'Total entries: {len(json_data)}')
print(f'Properly mapped quantifiable values and monthly tasks')
