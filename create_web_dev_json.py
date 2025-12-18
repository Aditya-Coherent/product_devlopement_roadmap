import json
import csv

json_data = []

# Element grouping - mapping tasks to their element categories
element_map = {
    'UI/UX design required Pages aligned with wellness aesthetics': 'Website Design and Development',
    'Payment gateway & shipping integration': 'Website Design and Development',
    'SEO-friendly structure & content setup': 'Website Design and Development',
    'Reviews, ratings & UGC integration': 'Website Design and Development',
    'Email automation + remarketing setup': 'Website Design and Development',
    'Intergration of Google Analtics and Hotjar': 'Website Traffic & User Behavior: Analytics Tracking',
    'WooCommerce Conversion Tracking': 'Conversion Tracking & eCommerce: Wocommerce Plugin',
    'Addition of UTM Parameters': 'Conversion Tracking & eCommerce: Wocommerce Plugin',
    'Integrate CRM tools': 'Customer Acquisition/Retention : CRM Integration & Cohort Analysis',
    'Zoho CRM Integration and configurations': 'Customer Acquisition/Retention : CRM Integration & Cohort Analysis',
    'Zoho CRM Features activations': 'Customer Acquisition/Retention : CRM Integration & Cohort Analysis',
    'Integrate inventory management systems Using WooCommerce': 'Inventory Management Integration',
    'WP Widget Integration and Live chat integration': 'Customer Experience: Survey Widgets & Support Integration',
    'Follow-up email for Product review and Rating': 'Customer Experience: Survey Widgets & Support Integration',
    'Site Caching Improve Page Load time': 'Website Speed Optimization',
    'Images Optimization': 'Website Speed Optimization',
    'CDN Monitoring and Required configurations ': 'Website Speed Optimization',
    'Check GSC For Issues': 'Search Console',
    'Fix mobile related issues': 'Search Console',
    'Redirections Handling': 'Search Console',
    'Fix crawl Errors': 'Search Console',
    'Product Schema Markup': 'Search Console',
    'Core Web Vitals Fixing – Mobile': 'Search Console',
    'Core Web Vitals Fixing – Desktop': 'Search Console',
    'Improve Product Link Structure': 'Search Console',
    'Google Page Speed Insights recommended optimizations and resolve the issues': 'Google PageSpeed Insights',
    'Technical Audit fixing Errors, Warnings and Notices': 'Gtmetrix and Ahref',
    'Hotjar Tracking implementations': 'Performance Analytics and Monitoring',
    'Errors Log Fixing': 'Error Monitoring',
    'Broken Links Fixing': 'Error Monitoring',
    'Mobile Friendly Issues Fixing ': 'Mobile Optimization',
    'Monitor Server Health': 'Server and Hosting Monitoring',
    'Hosting Performance Management': 'Server and Hosting Monitoring',
    'Database cleaning and Optimization': 'Database Optimization',
    'Database Indexing For Performance': 'Database Optimization',
    'Monitor Shopping Cart Load ': 'Load Testing',
    'Server AutoScale Based on Traffic Spikes': 'Load Testing',
    'Page Loading Management': 'Content Delivery and Optimization',
    'Minification and Concatenation': 'Content Delivery and Optimization',
    'Security Monitoring ': 'Security and Performance',
    'Themes and Plugins Updates to Latest Version': 'Themes and Plugins Updates',
}

# Month mapping
month_map = {
    'Jan': 'January', 'Feb': 'February', 'Mar': 'March', 'Apr': 'April',
    'May': 'May', 'Jun': 'June', 'Jul': 'July', 'Aug': 'August',
    'Sep': 'September', 'Oct': 'October', 'Nov': 'November', 'Dec': 'December'
}

# Read CSV with proper CSV parsing
with open('public/web development.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    header = next(reader)  # Skip header
    
    for row in reader:
        if len(row) < 5:
            continue
        
        task = row[1].strip() if len(row) > 1 else ''
        quantifiable = row[2].strip() if len(row) > 2 else ''
        monthly_task = row[3].strip() if len(row) > 3 else ''
        month_str = row[4].strip() if len(row) > 4 else ''
        
        # Skip empty tasks
        if not task:
            continue
        
        # Get element from mapping
        element = element_map.get(task, 'Website Development')
        
        # Determine months
        months = []
        if 'Jan -  Dec' in month_str or 'Jan - Dec' in month_str:
            months = ['January', 'February', 'March', 'April', 'May', 'June',
                     'July', 'August', 'September', 'October', 'November', 'December']
        elif month_str:
            # Handle single months
            for abbr, full in month_map.items():
                if abbr in month_str:
                    months.append(full)
                    break
            if not months:
                months = ['January']
        else:
            months = ['January']
        
        # Create entries for each month
        for month in months:
            entry = {
                'month': month,
                'category': 'Web Development',
                'element': element,
                'task': task,
                'monthlyTask': monthly_task if monthly_task else '',
                'monthlyQuantifiable': quantifiable if quantifiable else '',
                'team': 'website'
            }
            json_data.append(entry)

# Write to JSON file
with open('public/website-development-data.json', 'w', encoding='utf-8') as f:
    json.dump(json_data, f, indent=2, ensure_ascii=False)

print('✅ Successfully updated website-development-data.json!')
print(f'Total entries: {len(json_data)}')
print(f'Data imported from web development.csv with proper element grouping')

