import json

# Read the raw CSV content and manually create the proper entries with all details

json_data = []

entries = [
    {
        'month': 'January',
        'element': 'Monthly Pack (M1)',
        'task': 'Base Month\n• Competitor SKU & launch tracker (continuous): Advertising & campaign activity snapshot, Festive offers. Recent developments, Other key trends\n• Pricing baseline / Snapshot: Pricing Snapshot (Top Changes / Movements across companies)\n• Sales Channel-wise performance pulse (D2C / marketplace / Q-commerce / offline)',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'February',
        'element': 'Monthly Pack (M2)',
        'task': 'Consumer & Ingredient Focus (while all baseline tracking continues):\n• Ingredient & format signal tracker (rising/declining)\n• Consumer demand & sentiment cues\n• Competitor strategic moves (portfolio, funding, pricing resets)',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': ['January', 'February', 'March'],
        'element': 'Quarterly + Monthly (Q1)',
        'task': 'Deliver Q1 datasets: market size & sales dataset cuts (Product/Ingredient/Format), Global vs India benchmarks, Sales Channel dashboards, Competitor Pricing & Promotions + macro shifts / sentiment / Ayurveda×clinical narrative / ingredient megatrends.',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'April',
        'element': 'Monthly Pack (M4)',
        'task': '• Sales Channel Dashboard Snapshot (key changes only)\n• Recent Developments Across Competitors\n• Price Trends / Changes (top SKUs/brands)\n• New ingredient/claim callouts captured in market',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'May',
        'element': 'Monthly Pack (M5)',
        'task': 'Monthly Refresh:\n• Ingredient preference signals / Insights Dashboard\n• Claims Language Shifts, "mainstream vs rising" update\n• Shortlist of "watch" ingredients/formats\n• New product/format additions (kits/bundles/minis)',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': ['April', 'May', 'June'],
        'element': 'Quarterly + Monthly (Q2)',
        'task': 'Deliver Q2 datasets: market size & sales dataset cuts (Product/Ingredient/Format), Global vs India benchmarks, Sales Channel dashboards / Pricing Dashboards, Competitor Pricing & Promotions + macro shifts / sentiment / Ayurveda×clinical narrative / ingredient megatrends.',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'July',
        'element': 'Monthly Pack (M7)',
        'task': 'Mid-Year Reset:\n• Post-Q2 change log (what accelerated / slowed)\n• Ingredient adoption momentum Check Insights\n• Sales Channel performance Insights: Winners/Laggards',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'August',
        'element': 'Monthly Pack (M8)',
        'task': 'Consumer & Spend Pulse:\n• Consumer concerns & spend cues (pre-festive)\n• SKU-level pricing / promos movements\n• Ingredient & format tracker refresh',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': ['July', 'August', 'September'],
        'element': 'Quarterly + Monthly (Q3)',
        'task': '• Deliver Q3 full pack: updated datasets + dashboards as in Q2\n• Pricing/promos trends in last quarter\n• Quarterly trend storylines (what\'s now "default" vs "next-wave")\n• Festive build-up pricing & promo strategies',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'October',
        'element': 'Monthly Pack (M10)',
        'task': 'Festive Intelligence Month:\n• Sales & pricing Datasets\n• Festive pricing, offers & bundles\n• Kit / gifting strategy deep dive\n• Ingredient & claim themes in festive campaigns',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': 'November',
        'element': 'Monthly Pack (M11)',
        'task': 'Deep-Dive Month (one agreed theme):\n• Ingredients OR formats OR channel economics\n• Performance comparison vs prior quarters\n• Implications drawn from year-to-date data\n• Narrative: Ingredients, Formats, or Channel economics/pricing',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    },
    {
        'month': ['October', 'November', 'December'],
        'element': 'Quarterly + Annual Wrap (Q4)',
        'task': '• Q4 + Annual Consolidation:\n• Q4 datasets & dashboards\n• Year-end pricing & promo summary\n• Ingredient & format shifts across the year\n• Winners/losers + next-year watchlist',
        'quantifiable': 'NA',
        'monthly_task': 'NA'
    }
]

# Create JSON entries
for entry in entries:
    months = entry['month'] if isinstance(entry['month'], list) else [entry['month']]
    
    for month in months:
        json_entry = {
            'month': month,
            'category': 'Research',
            'element': entry['element'],
            'task': entry['task'],
            'monthlyTask': entry['monthly_task'] if entry['monthly_task'] != 'NA' else '',
            'monthlyQuantifiable': entry['quantifiable'] if entry['quantifiable'] != 'NA' else '',
            'team': 'market-research'
        }
        json_data.append(json_entry)

# Write to JSON file
with open('public/market-research-data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print('✅ Successfully updated market-research-data.json!')
print(f'Total entries: {len(json_data)}')
print(f'Included all opening lines and bullet points from CSV')
