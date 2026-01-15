import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Check for any remaining entries that should have been removed
remaining_patterns = [
    "Preparation for Upcoming Rituva Summer Kit",
    "Off-Page SEO for Upcoming Rituva Kit",
    "Performance Marketing Strategy for Upcoming Rituva Kit",
    "Preparation for Upcoming Season Rituva Kit",
]

february_entries_count = 0
found_unwanted = 0

for entry in data:
    if entry.get('month') == 'February':
        february_entries_count += 1
        for pattern in remaining_patterns:
            if pattern in entry.get('element', '') or pattern in entry.get('task', ''):
                found_unwanted += 1
                print(f'✗ STILL PRESENT: {entry.get("element")} - {entry.get("task")[:80]}')

print("\n" + "="*70)
print("✅ VERIFICATION RESULTS")
print("="*70)
print(f"Total February entries: {february_entries_count}")
print(f"Unwanted entries still present: {found_unwanted}")
if found_unwanted == 0:
    print("\n✅ ALL SPECIFIED ENTRIES SUCCESSFULLY REMOVED FROM FEBRUARY!")
else:
    print(f"\n✗ {found_unwanted} unwanted entries still remain")
print("="*70)



