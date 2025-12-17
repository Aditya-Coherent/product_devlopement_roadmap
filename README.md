# Rituva Development Roadmap

A beautiful serverless web application built with Next.js to visualize and filter development roadmap data from Excel files. Deployable on Vercel.

## Features

- 📊 **Automatic Data Loading** - Excel data is automatically converted to JSON and loaded on page load
- 🎯 **Team Filter** - Filter by team (Website, AI, Market Research, Digital Marketing)
- 📅 **Month Filter** - Filter by specific months or view all months
- 📈 **Statistics** - View total tasks and unique elements
- 🎨 **Beautiful UI** - Modern, responsive design with white and mint green professional theme
- 🖼️ **Logo Display** - Company logo in top-left corner

## Getting Started

### Prerequisites

- Node.js 18+ installed
- npm or yarn package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Aditya-Coherent/product_devlopement_roadmap.git
cd product_devlopement_roadmap
```

2. Install dependencies:
```bash
npm install
```

3. Convert Excel files to JSON (if you have Excel files):
```bash
npm run convert-excel
```

4. Run the development server:
```bash
npm run dev
```

5. Open [http://localhost:3000](http://localhost:3000) in your browser

## Deployment on Vercel

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. Push your code to GitHub (already done)
2. Go to [vercel.com](https://vercel.com)
3. Click "New Project"
4. Import your GitHub repository: `Aditya-Coherent/product_devlopement_roadmap`
5. Vercel will automatically detect Next.js and configure the project
6. Click "Deploy"

### Option 2: Deploy via Vercel CLI

1. Install Vercel CLI:
```bash
npm i -g vercel
```

2. Deploy:
```bash
vercel
```

### Important Notes for Vercel Deployment

- The JSON data files in the `public/` directory will be automatically included in the deployment
- Make sure all Excel files are converted to JSON before deploying
- The app uses static JSON files, so no database is required
- All team data (Website, AI, Market Research, Digital Marketing) is included

## Project Structure

```
.
├── app/
│   ├── layout.js              # Root layout component
│   ├── page.js                # Main page component
│   ├── globals.css            # Global styles with Tailwind
│   └── error-boundary.js      # Error boundary component
├── public/
│   ├── logo.png               # Company logo
│   ├── website-data.json      # Website team data
│   ├── digital-marketing-data.json
│   ├── market-research-data.json
│   └── artificial-intelligence-data.json
├── data/                      # Data files (backup)
├── scripts/
│   └── convert-excel-to-json.js  # Excel to JSON converter
├── package.json
├── next.config.js
├── tailwind.config.js
└── vercel.json                # Vercel configuration
```

## Usage

1. The Excel files are automatically converted to JSON using the conversion script
2. Run `npm run convert-excel` if you update the Excel files to regenerate the JSON
3. The app automatically loads the data when you visit the page
4. Use the Team filter to select a team (Website, AI, Market Research, Digital Marketing)
5. Use the Month filter to view specific months or all months
6. Data is automatically grouped by month, then by element, with tasks listed under each element

## Technologies Used

- **Next.js 14** - React framework with App Router
- **React 18** - UI library
- **Tailwind CSS 3** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **Lucide React** - Icon library
- **XLSX** - Excel file parsing (for conversion script)

## Development

### Converting Excel Files

If you have Excel files to convert:

1. Place Excel files in the root directory:
   - `12_Month_Website_Timeline.xlsx`
   - `Digital Marketing.xlsx`
   - `Research Team.xlsx`
   - `Ai Team.xlsx`

2. Run the conversion script:
```bash
npm run convert-excel
```

3. The script will:
   - Process all Excel files
   - Create JSON files in `data/`, `app/`, and `public/` directories
   - Generate separate files for each team

## License

MIT

## Author

Aditya-Coherent
