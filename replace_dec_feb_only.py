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
                # Replace Dec–Feb only with seasonal focus only (using en-dash)
                entry[key] = re.sub(r'Dec[–-]Feb\s+only', 'seasonal focus only', entry[key])
                
                # Count replacements
                if original != entry[key]:
                    january_replacements += 1
                    print(f"✓ [JANUARY] {key}: {original[:70]}...")
    
    # Process February entries
    elif entry.get('month') == 'February':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry:
                original = entry[key]
                # Replace Dec–Feb only with seasonal focus only
                entry[key] = re.sub(r'Dec[–-]Feb\s+only', 'seasonal focus only', entry[key])
                
                # Count replacements
                if original != entry[key]:
                    february_replacements += 1
                    print(f"✓ [FEBRUARY] {key}: {original[:70]}...")

# Write the updated JSON back
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n" + "="*70)
print("✅ REPLACEMENTS COMPLETED - 'Dec–Feb only' → 'seasonal focus only'")
print("="*70)
print(f"✓ January replacements: {january_replacements}")
print(f"✓ February replacements: {february_replacements}")
print(f"✓ Total replacements: {january_replacements + february_replacements}")
print("="*70)
print("✅ File updated successfully!")



