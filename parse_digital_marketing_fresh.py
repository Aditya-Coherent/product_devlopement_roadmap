import csv
import json

# Read the CSV file using proper CSV reader
data = []
months_list = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

current_category = None
current_element = None

with open('public/7am.csv', 'r', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f, fieldnames=['Team', 'Elements', 'SubElements', 'Task', 'MonthlyTask', 'Month'])
    
    for row in reader:
        # Skip empty rows
        if not row or all(v == '' or v is None for v in row.values()):
            continue
        
        team = row['Team'].strip() if row['Team'] else ''
        csv_elements = row['Elements'].strip() if row['Elements'] else ''  # A. Page Metadata, etc.
        csv_subelements = row['SubElements'].strip() if row['SubElements'] else ''  # i. Page Title, etc.
        csv_task = row['Task'].strip() if row['Task'] else ''  # The description
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
            continue
        
        # Skip lines with just "Elements" header
        if csv_elements == 'Elements' and csv_subelements == 'Sub-elements':
            continue
        
        # Skip if no task
        if not csv_task or csv_task == 'Task':
            continue
        
        # Update current element if provided (this is the grouping like "A. Page Metadata")
        if csv_elements and csv_elements not in ['Elements', 'NA', '']:
            current_element = csv_elements
        
        # Determine months
        if month_str in ['Jan -  Dec', 'Jan - Dec']:
            months_to_add = months_list
        elif month_str == 'Jan':
            months_to_add = ['January']
        else:
            months_to_add = ['January']
        
        category = current_category if current_category else 'Digital Marketing'
        
        # SWAPPED: 
        # subElement = the grouping (A. Page Metadata, B. HTML Structure, etc.)
        # element = the specific item (i. Page Title Optimization, etc.)
        subelement = current_element if current_element else 'Other'
        element = csv_subelements if csv_subelements else 'Other'
        
        # Clean up task - remove leading bullet points
        task_clean = csv_task
        if task_clean.startswith('·'):
            task_clean = task_clean.replace('·', '', 1).strip()
        
        # Clean up monthly_task - remove leading bullet points
        monthly_task_clean = monthly_task
        if monthly_task_clean.startswith('·'):
            monthly_task_clean = monthly_task_clean.replace('·', '', 1).strip()
        
        # Add entry for each month
        for month in months_to_add:
            entry = {
                'month': month,
                'category': category,
                'element': element,           # i. Page Title Optimization
                'subElement': subelement,     # A. Page Metadata
                'task': task_clean,           # Create and Optimize title tags
                'monthlyTask': monthly_task_clean,
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

print("\n✓ SWAPPED STRUCTURE:")
print("\nOn-Page SEO January sample:")
on_page_jan = [e for e in data if e['category'] == 'On-Page SEO' and e['month'] == 'January'][:3]
for entry in on_page_jan:
    print(f"\n  SubElement: {entry['subElement']}")
    print(f"  Element: {entry['element']}")
    print(f"  Task: {entry['task']}")
    print(f"  Monthly Task: {entry['monthlyTask']}")

print("\n\nOff-Page SEO January sample:")
off_page_jan = [e for e in data if e['category'] == 'Off-Page SEO' and e['month'] == 'January'][:2]
for entry in off_page_jan:
    print(f"\n  SubElement: {entry['subElement']}")
    print(f"  Element: {entry['element']}")
    print(f"  Task: {entry['task']}")
    print(f"  Monthly Task: {entry['monthlyTask']}")
