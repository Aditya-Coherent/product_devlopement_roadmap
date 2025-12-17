const XLSX = require('xlsx');
const fs = require('fs');
const path = require('path');

// Define Excel files and their corresponding team names
const excelFiles = [
  { file: '12_Month_Website_Timeline.xlsx', team: 'website' },
  { file: 'Digital Marketing.xlsx', team: 'digital-marketing' },
  { file: 'Research Team.xlsx', team: 'market-research' },
  { file: 'Ai Team.xlsx', team: 'artificial-intelligence' }
];

// Function to process a single Excel file
function processExcelFile(fileName, teamName) {
  const excelFilePath = path.join(__dirname, '..', fileName);
  
  if (!fs.existsSync(excelFilePath)) {
    console.log(`⚠️  File not found: ${fileName}, skipping...`);
    return null;
  }

  const workbook = XLSX.readFile(excelFilePath);
  const firstSheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[firstSheetName];
  
  const jsonData = XLSX.utils.sheet_to_json(worksheet, { 
    header: 1,
    defval: ''
  });

  const processedData = [];
  
  for (let i = 1; i < jsonData.length; i++) {
    const row = jsonData[i];
    
    if (row.length === 0 || (!row[0] && !row[1] && !row[2])) {
      continue;
    }

    const month = String(row[0] || '').trim();
    const element = String(row[1] || '').trim();
    const task = String(row[2] || '').trim();

    if (month && element && task) {
      processedData.push({
        month: month,
        element: element,
        task: task,
        team: teamName
      });
    }
  }

  return processedData;
}

// Process all Excel files
const allData = {};

excelFiles.forEach(({ file, team }) => {
  const data = processExcelFile(file, team);
  if (data) {
    allData[team] = data;
    console.log(`✅ Processed ${file}: ${data.length} rows for team "${team}"`);
  }
});

// Create data directory if it doesn't exist
const dataDir = path.join(__dirname, '..', 'data');
if (!fs.existsSync(dataDir)) {
  fs.mkdirSync(dataDir, { recursive: true });
}

// Create public directory if it doesn't exist
const publicDir = path.join(__dirname, '..', 'public');
if (!fs.existsSync(publicDir)) {
  fs.mkdirSync(publicDir, { recursive: true });
}

// Save individual team files
Object.keys(allData).forEach(team => {
  const outputPath = path.join(dataDir, `${team}-data.json`);
  fs.writeFileSync(outputPath, JSON.stringify(allData[team], null, 2));
  console.log(`📁 Saved: ${outputPath}`);
  
  // Also copy to app directory
  const appOutputPath = path.join(__dirname, '..', 'app', `${team}-data.json`);
  fs.writeFileSync(appOutputPath, JSON.stringify(allData[team], null, 2));
  console.log(`📁 Also copied to: ${appOutputPath}`);
  
  // Also copy to public directory for fetch
  const publicOutputPath = path.join(publicDir, `${team}-data.json`);
  fs.writeFileSync(publicOutputPath, JSON.stringify(allData[team], null, 2));
  console.log(`📁 Also copied to: ${publicOutputPath}`);
});

// Save combined data file (for backward compatibility)
const combinedData = Object.values(allData).flat();
const combinedOutputPath = path.join(dataDir, 'roadmap-data.json');
fs.writeFileSync(combinedOutputPath, JSON.stringify(combinedData, null, 2));
console.log(`📁 Combined data saved: ${combinedOutputPath} (${combinedData.length} total rows)`);

// Also copy combined to app directory
const appCombinedPath = path.join(__dirname, '..', 'app', 'roadmap-data.json');
fs.writeFileSync(appCombinedPath, JSON.stringify(combinedData, null, 2));

console.log('\n✨ Conversion complete!');
