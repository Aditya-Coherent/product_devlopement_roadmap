import csv
import json

# Read the CSV file using proper CSV reader
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None
current_element = None
current_subelement = None
current_monthly_task = None  # Carry forward monthly task within element groups

def clean_bullet(text):
    """Remove bullet points and extra whitespace"""
    if not text:
        return ''
    text = text.strip()
    if text.startswith('·'):
        text = text.replace('·', '', 1).strip()
    # Remove multiple spaces
    while '  ' in text:
        text = text.replace('  ', ' ')
    return text

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, fieldnames=['Team', 'Elements', 'SubElements', 'Task', 'MonthlyTask', 'Month'])
    
    for row in reader:
        # Skip empty rows
        if not row or all(v == '' or v is None for v in row.values()):
            continue
        
        team = row['Team'].strip() if row['Team'] else ''
        elements = row['Elements'].strip() if row['Elements'] else ''
        subelements = row['SubElements'].strip() if row['SubElements'] else ''
        task = row['Task'].strip() if row['Task'] else ''
        monthly_task = row['MonthlyTask'].strip() if row['MonthlyTask'] else ''
        month_str = row['Month'].strip() if row['Month'] else ''
        
        # Skip header row
        if team == 'Team':
            continue
        
        # Check if this is a category header (main section)
        if team in ['Digital Marketing', 'On-Page SEO', 'Off-Page SEO', 'Technical SEO',
                   'Performance Marketing', 'Paid PR Submission & Distribution Services (B2C Focus)',
                   'Brand Positioning & Thought Leadership', 'Content Marketing & Strategy']:
            current_category = team
            current_element = None
            current_subelement = None
            current_monthly_task = None
            continue
        
        # Skip lines with just "Elements" header
        if elements == 'Elements' and subelements == 'Sub-elements':
            continue
        
        # Skip if there's no task AND no monthly task (completely empty data row)
        if not task and not monthly_task:
            continue
        
        # Skip if task is just "Task" header
        if task == 'Task':
            continue
        
        # Update current element if provided
        if elements and elements not in ['Elements', 'NA', '']:
            current_element = elements
            current_monthly_task = None  # Reset monthly task when element changes
        
        # Update current subelement if provided
        if subelements and subelements not in ['Sub-elements', 'NA', '']:
            current_subelement = subelements
        
        # Update current monthly task if provided
        if monthly_task:
            current_monthly_task = clean_bullet(monthly_task)
        
        # Use current values for grouping
        element = current_element if current_element else 'Other'
        subelement = current_subelement if current_subelement else subelements if subelements else 'Other'
        
        # Determine months
        if month_str in ['Jan -  Dec', 'Jan - Dec']:
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        elif month_str:
            months_to_add = ['January']
        else:
            months_to_add = ['January']
        
        category = current_category if current_category else 'Digital Marketing'
        
        # Clean up task
        task_clean = clean_bullet(task)
        
        # Get monthly task - use current row's or carry forward
        monthly_task_clean = clean_bullet(monthly_task) if monthly_task else current_monthly_task
        
        # If task is empty but monthly_task has data, use monthly_task as task
        if not task_clean and monthly_task_clean:
            task_clean = monthly_task_clean
            monthly_task_clean = current_monthly_task if current_monthly_task else ''
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,
                'subElement': subelement,
                'task': task_clean,
                'monthlyTask': monthly_task_clean if monthly_task_clean else '',
                'team': 'digital-marketing'
            }
            data.append(entry)

# Write to JSON file
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Successfully created digital-marketing-data.json with {len(data)} entries")
print("\nBreakdown by category:")
categories = {}
for entry in data:
    cat = entry['category']
    if cat not in categories:
        categories[cat] = 0
    categories[cat] += 1

for cat in sorted(categories.keys()):
    print(f"  {cat}: {categories[cat]}")

# Show Technical SEO sample to verify monthly tasks
print("\nTechnical SEO January sample (checking monthly tasks):")
tech_seo_jan = [e for e in data if e['category'] == 'Technical SEO' and e['month'] == 'January']
for i, entry in enumerate(tech_seo_jan):
    print(f"\n{i+1}. Element: {entry['element']}")
    print(f"   SubElement: {entry['subElement']}")
    print(f"   Task: {entry['task']}")
    print(f"   Monthly Task: {entry['monthlyTask'] if entry['monthlyTask'] else '(empty)'}")

# Count empty monthly tasks
empty_monthly = sum(1 for e in data if not e['monthlyTask'])
print(f"\n\nTotal entries with empty monthly tasks: {empty_monthly} out of {len(data)}")
