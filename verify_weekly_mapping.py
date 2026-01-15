import json

with open('public/digital-marketing-data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print("="*90)
print("VERIFICATION - Comparing January vs February Weekly Tasks")
print("="*90)

# Test cases - same tasks that should have DIFFERENT weekly tasks per month
test_cases = [
    "i. Page Title Optimization",
    "i. Header Tags",
    "i. Monthly Backlink Building",
    "Search Engine Marketing",
    "Rituva Summer Kits"
]

for test_sub in test_cases:
    print(f"\n{'='*90}")
    print(f"Task: {test_sub}")
    print("="*90)
    
    # Find January entry
    jan_entry = None
    feb_entry = None
    
    for entry in data:
        if entry.get('subElement') == test_sub or entry.get('element') == test_sub:
            if entry.get('month') == 'January' and not jan_entry:
                jan_entry = entry
            elif entry.get('month') == 'February' and not feb_entry:
                feb_entry = entry
    
    if jan_entry:
        weekly = jan_entry.get('weeklyTask', 'NO WEEKLY TASK')
        print(f"\n[JANUARY]:")
        print(f"  Task: {jan_entry.get('task', 'N/A')[:60]}...")
        print(f"  Weekly: {weekly[:100]}...")
    else:
        print("\n[JANUARY]: No entry found")
    
    if feb_entry:
        weekly = feb_entry.get('weeklyTask', 'NO WEEKLY TASK')
        print(f"\n[FEBRUARY]:")
        print(f"  Task: {feb_entry.get('task', 'N/A')[:60]}...")
        print(f"  Weekly: {weekly[:100]}...")
    else:
        print("\n[FEBRUARY]: No entry found")

# Now verify there are NO Feb dates in January and NO Jan dates in February
print("\n\n" + "="*90)
print("CROSS-CONTAMINATION CHECK")
print("="*90)

jan_contaminated = 0
feb_contaminated = 0

for entry in data:
    if entry.get('month') == 'January' and 'weeklyTask' in entry:
        weekly = entry['weeklyTask'].lower()
        if 'feb' in weekly:
            jan_contaminated += 1
            print(f"⚠ JAN with FEB: {entry.get('subElement')} -> {entry['weeklyTask'][:60]}...")
    
    if entry.get('month') == 'February' and 'weeklyTask' in entry:
        weekly = entry['weeklyTask'].lower()
        if 'jan' in weekly:
            feb_contaminated += 1
            print(f"⚠ FEB with JAN: {entry.get('subElement')} -> {entry['weeklyTask'][:60]}...")

print(f"\nResults:")
print(f"✓ January entries with Feb dates: {jan_contaminated}")
print(f"✓ February entries with Jan dates: {feb_contaminated}")

if jan_contaminated == 0 and feb_contaminated == 0:
    print("\n✅ NO CROSS-CONTAMINATION FOUND!")
else:
    print("\n❌ CROSS-CONTAMINATION DETECTED!")

# Final count
jan_with_weekly = sum(1 for e in data if e.get('month') == 'January' and 'weeklyTask' in e)
feb_with_weekly = sum(1 for e in data if e.get('month') == 'February' and 'weeklyTask' in e)

print("\n" + "="*90)
print("FINAL STATISTICS")
print("="*90)
print(f"January entries with weekly tasks: {jan_with_weekly}")
print(f"February entries with weekly tasks: {feb_with_weekly}")

