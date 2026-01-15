import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('='*80)
print('REMOVING NEAR-DUPLICATES (different dash characters)')
print('='*80)

def normalize_dashes(text):
    """Normalize all types of dashes to regular hyphen"""
    if text is None:
        return ""
    return str(text).replace('–', '-').replace('—', '-').strip()

# Find and track near-duplicates
seen = {}  # normalized key -> first index
duplicates_to_remove = []

for i, entry in enumerate(data):
    month = entry.get('month')
    category = entry.get('category')
    element = normalize_dashes(entry.get('element', ''))
    task = normalize_dashes(entry.get('task', ''))
    
    key = (month, category, element, task)
    
    if key in seen:
        duplicates_to_remove.append(i)
        print(f'NEAR-DUPLICATE at index {i}: {month} | {task[:40]}')
    else:
        seen[key] = i

print(f'\nTotal near-duplicates to remove: {len(duplicates_to_remove)}')

# Remove duplicates (from end to start to preserve indices)
duplicates_to_remove.sort(reverse=True)
for idx in duplicates_to_remove:
    removed = data[idx]
    del data[idx]
    print(f'Removed: {removed.get("task", "")[:50]}')

# Save
with open('public/digital-marketing-data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f'\n✅ Removed {len(duplicates_to_remove)} near-duplicate entries')
print(f'New total entries: {len(data)}')

