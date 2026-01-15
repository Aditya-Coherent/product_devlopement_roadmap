import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Show sample entries with weekly tasks
print("="*70)
print("✅ SAMPLE ENTRIES WITH WEEKLY TASKS INTEGRATED")
print("="*70)

sample_count = 0
for entry in data:
    if entry.get('month') in ['January', 'February'] and 'weeklyTask' in entry:
        sample_count += 1
        print(f"\n[{entry['month']}] {entry['category']}")
        print(f"  Element: {entry['element']}")
        print(f"  Sub-element: {entry['subElement']}")
        print(f"  Task: {entry['task'][:80]}")
        print(f"  Monthly: {entry['monthlyTask'][:80]}")
        print(f"  Weekly: {entry['weeklyTask'][:100]}...")
        
        if sample_count >= 5:
            break

# Count total entries with weekly tasks
total_with_weekly = sum(1 for entry in data if 'weeklyTask' in entry)
total_jan_feb = sum(1 for entry in data if entry.get('month') in ['January', 'February'])

print("\n" + "="*70)
print("INTEGRATION STATISTICS")
print("="*70)
print(f"Total January + February entries: {total_jan_feb}")
print(f"Entries with weekly tasks added: {total_with_weekly}")
print("="*70)

