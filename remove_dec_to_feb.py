import json
import re

# Read the JSON file
with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Counter for replacements
january_removals = 0
february_removals = 0

# Process each entry
for entry in data:
    # Process January entries
    if entry.get('month') == 'January':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry:
                original = entry[key]
                # Remove Dec to Feb (with various spacing and dash variations)
                entry[key] = re.sub(r'\s*Dec\s+to\s+Feb', '', entry[key], flags=re.IGNORECASE)
                entry[key] = re.sub(r'\s*Dec\s*–\s*to\s*Feb', '', entry[key], flags=re.IGNORECASE)
                entry[key] = re.sub(r'\s*Dec–to Feb', '', entry[key])
                # Clean up any double spaces
                entry[key] = re.sub(r'\s+', ' ', entry[key]).strip()
                
                # Count removals
                if original != entry[key]:
                    january_removals += 1
                    print(f"✓ [JANUARY] {key}:")
                    print(f"  Before: {original[:80]}")
                    print(f"  After:  {entry[key][:80]}")
    
    # Process February entries
    elif entry.get('month') == 'February':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry:
                original = entry[key]
                # Remove Dec to Feb (with various spacing and dash variations)
                entry[key] = re.sub(r'\s*Dec\s+to\s+Feb', '', entry[key], flags=re.IGNORECASE)
                entry[key] = re.sub(r'\s*Dec\s*–\s*to\s*Feb', '', entry[key], flags=re.IGNORECASE)
                entry[key] = re.sub(r'\s*Dec–to Feb', '', entry[key])
                # Clean up any double spaces
                entry[key] = re.sub(r'\s+', ' ', entry[key]).strip()
                
                # Count removals
                if original != entry[key]:
                    february_removals += 1
                    print(f"✓ [FEBRUARY] {key}:")
                    print(f"  Before: {original[:80]}")
                    print(f"  After:  {entry[key][:80]}")

# Write the updated JSON back
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("\n" + "="*70)
print("✅ REMOVAL COMPLETED - 'Dec to Feb' REMOVED")
print("="*70)
print(f"✓ January removals: {january_removals}")
print(f"✓ February removals: {february_removals}")
print(f"✓ Total removals: {january_removals + february_removals}")
print("="*70)
print("✅ File updated successfully!")



