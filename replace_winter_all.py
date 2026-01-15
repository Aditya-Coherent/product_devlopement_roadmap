import json
import re

# Read the JSON file
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Counter for replacements
january_replacements = 0
february_replacements = 0

# Process each entry
for entry in data:
    # Process January entries
    if entry.get('month') == 'January':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry:
                original = entry[key]
                # Replace Winter -> Summer (preserve case)
                entry[key] = re.sub(r'Winter', 'Summer', entry[key])
                entry[key] = re.sub(r'winter', 'summer', entry[key])
                
                # Count replacements
                if original != entry[key]:
                    january_replacements += 1
    
    # Process February entries
    elif entry.get('month') == 'February':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry:
                original = entry[key]
                # Replace Winter -> Summer
                entry[key] = re.sub(r'Winter', 'Summer', entry[key])
                entry[key] = re.sub(r'winter', 'summer', entry[key])
                
                # Count replacements
                if original != entry[key]:
                    february_replacements += 1

# Write the updated JSON back
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("="*70)
print("✅ REPLACEMENTS COMPLETED")
print("="*70)
print(f"✓ January replacements: {january_replacements}")
print(f"✓ February replacements: {february_replacements}")
print(f"✓ Total replacements: {january_replacements + february_replacements}")
print("="*70)
print("✅ File updated successfully!")



