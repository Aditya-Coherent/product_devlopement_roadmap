import json

# Read the JSON file
with open('public/website-development-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Find the January "Gtmetrix and Ahref" entry to get the correct values
january_gtmetrix = None
for item in data:
    if item['month'] == 'January' and item['element'] == 'Gtmetrix and Ahref':
        january_gtmetrix = item
        break

if january_gtmetrix:
    print(f"Found January Gtmetrix entry:")
    print(f"  Task: {january_gtmetrix['task']}")
    print(f"  Monthly Task: {january_gtmetrix['monthlyTask']}")
    print(f"  Quantifiable: {january_gtmetrix['monthlyQuantifiable']}")
    
    # Update all other months' Gtmetrix entries with the same values
    updated_count = 0
    for item in data:
        if item['element'] == 'Gtmetrix and Ahref' and item['month'] != 'January':
            item['task'] = january_gtmetrix['task']
            item['monthlyTask'] = january_gtmetrix['monthlyTask']
            item['monthlyQuantifiable'] = january_gtmetrix['monthlyQuantifiable']
            updated_count += 1
    
    print(f"\nUpdated {updated_count} entries across other months")
    
    # Write back to file
    with open('public/website-development-data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print("✅ Successfully updated all Gtmetrix and Ahref entries!")
else:
    print("❌ Could not find January Gtmetrix entry")

