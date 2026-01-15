import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for remaining Dec to Feb occurrences in January/February
jan_remaining = 0
feb_remaining = 0

for entry in data:
    if entry.get('month') == 'January':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'Dec to Feb' in entry[key]:
                jan_remaining += 1
                print(f'✗ [JANUARY] {key}: {entry[key][:80]}')
    elif entry.get('month') == 'February':
        for key in ['task', 'element', 'subElement', 'monthlyTask']:
            if key in entry and 'Dec to Feb' in entry[key]:
                feb_remaining += 1
                print(f'✗ [FEBRUARY] {key}: {entry[key][:80]}')

print("\n" + "="*70)
print("✅ VERIFICATION RESULTS")
print("="*70)
print(f"Remaining 'Dec to Feb' in January: {jan_remaining}")
print(f"Remaining 'Dec to Feb' in February: {feb_remaining}")
if jan_remaining == 0 and feb_remaining == 0:
    print("\n✅ ALL 'Dec to Feb' SUCCESSFULLY REMOVED!")
else:
    print("\n✗ Some occurrences still remain")
print("="*70)



