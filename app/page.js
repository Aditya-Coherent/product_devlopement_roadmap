'use client'

import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import Image from 'next/image'
import { 
  Calendar, 
  Users, 
  CheckCircle2, 
  Filter,
  ChevronRight,
  Target,
  Zap,
  Sparkles
} from 'lucide-react'

const monthNames = {
  '1': 'January',
  '2': 'February',
  '3': 'March',
  '4': 'April',
  '5': 'May',
  '6': 'June',
  '7': 'July',
  '8': 'August',
  '9': 'September',
  '10': 'October',
  '11': 'November',
  '12': 'December'
}

const monthColors = [
  'from-emerald-400 to-teal-500',
  'from-teal-400 to-cyan-500',
  'from-cyan-400 to-blue-500',
  'from-blue-400 to-indigo-500',
  'from-indigo-400 to-purple-500',
  'from-purple-400 to-pink-500',
  'from-pink-400 to-rose-500',
  'from-rose-400 to-red-500',
  'from-red-400 to-orange-500',
  'from-orange-400 to-amber-500',
  'from-amber-400 to-yellow-500',
  'from-yellow-400 to-lime-500',
]

export default function Home() {
  const [excelData, setExcelData] = useState([])
  const [filteredData, setFilteredData] = useState([])
  const [teamFilter, setTeamFilter] = useState('website')
  const [monthFilter, setMonthFilter] = useState('all')
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState(null)

  // Load data based on team selection
  useEffect(() => {
    const loadData = async () => {
      setIsLoading(true)
      setError(null)
      try {
        let data = []
        let fileName = null
        
        if (teamFilter === 'website') {
          fileName = '/website-development-data.json'
        } else if (teamFilter === 'digital-marketing') {
          fileName = '/digital-marketing-data.json'
        } else if (teamFilter === 'market-research') {
          fileName = '/market-research-data.json'
        } else if (teamFilter === 'artificial-intelligence') {
          fileName = '/artificial-intelligence-data.json'
        } else if (teamFilter === 'human-resources') {
          fileName = '/Human-Resource-data.json'
        }

        if (fileName) {
          console.log(`🔄 Fetching data from: ${fileName}`)
          const response = await fetch(fileName)
          console.log(`📡 Response status: ${response.status}`)
          
          if (response.ok) {
            data = await response.json()
            console.log(`✅ Loaded data for team: ${teamFilter}`, data.length, 'items')
          } else {
            const errorMsg = `Failed to fetch data: ${response.status} ${response.statusText}`
            console.error(errorMsg)
            setError(errorMsg)
          }
        }
        
        if (Array.isArray(data) && data.length > 0) {
          setExcelData(data)
          setFilteredData(data)
          setError(null)
        } else if (fileName) {
          console.warn('No data found for team:', teamFilter)
          setExcelData([])
          setFilteredData([])
        }
      } catch (error) {
        const errorMsg = `Error loading roadmap data: ${error.message}`
        console.error(errorMsg, error)
        setError(errorMsg)
        setExcelData([])
        setFilteredData([])
      } finally {
        setIsLoading(false)
      }
    }

    loadData()
  }, [teamFilter])

  const normalizeMonth = (monthString) => {
    if (!monthString) return ''
    
    let normalized = String(monthString).trim().toLowerCase()
    normalized = normalized.replace(/\s+/g, ' ')
    
    const monthNum = parseInt(normalized)
    if (!isNaN(monthNum) && monthNum >= 1 && monthNum <= 12) {
      return monthNames[monthNum.toString()]
    }
    
    const monthAbbr = {
      'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
      'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
      'sep': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'
    }
    
    if (monthAbbr[normalized.substring(0, 3)]) {
      return monthAbbr[normalized.substring(0, 3)]
    }
    
    for (const [num, name] of Object.entries(monthNames)) {
      const nameLower = name.toLowerCase()
      if (normalized === nameLower || 
          normalized.includes(nameLower) || 
          nameLower.includes(normalized)) {
        return name
      }
    }
    
    const date = new Date(monthString)
    if (!isNaN(date.getTime())) {
      const monthIndex = date.getMonth() + 1
      return monthNames[monthIndex.toString()]
    }
    
    return String(monthString).trim()
  }

  const applyFilters = () => {
    let filtered = [...excelData]

    if (monthFilter !== 'all') {
      const selectedMonth = monthNames[monthFilter]
      filtered = filtered.filter(item => {
        const itemMonth = normalizeMonth(item.month)
        return itemMonth === selectedMonth || 
               itemMonth.includes(selectedMonth) || 
               selectedMonth.includes(itemMonth)
      })
    }

    setFilteredData(filtered)
  }

  useEffect(() => {
    if (excelData.length > 0) {
      applyFilters()
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [monthFilter, excelData])

  const groupedData = () => {
    const grouped = {}
    
    filteredData.forEach(item => {
      const month = normalizeMonth(item.month)
      if (!grouped[month]) {
        grouped[month] = {}
      }
      
      const category = item.category || 'Other'
      if (!grouped[month][category]) {
        grouped[month][category] = {}
      }
      
      // For digital marketing, group by element; for others, group by element
      const groupKey = item.element || 'Other'
      if (!grouped[month][category][groupKey]) {
        grouped[month][category][groupKey] = []
      }
      
      grouped[month][category][groupKey].push({
        element: item.element || '',
        subElement: item.subElement || '',
        task: item.task || '',
        monthlyTask: item.monthlyTask || '',
        monthlyQuantifiable: item.monthlyQuantifiable || ''
      })
    })

    return grouped
  }

  const sortedMonths = () => {
    const grouped = groupedData()
    const monthOrder = Object.values(monthNames)
    return Object.keys(grouped).sort((a, b) => {
      return monthOrder.indexOf(a) - monthOrder.indexOf(b)
    })
  }

  const totalTasks = () => {
    let count = 0
    filteredData.forEach(item => {
      count += 1
    })
    return count
  }
  
  const uniqueElements = new Set(filteredData.map(item => item.element)).size

  const getMonthColor = (month) => {
    const monthIndex = Object.values(monthNames).indexOf(month)
    return monthColors[monthIndex % monthColors.length]
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-emerald-50 to-teal-50">
      {/* Logo in top left corner - scrolls with page */}
      <div className="absolute top-6 left-6 z-10">
        <Image
          src="/logo.png"
          alt="Rituva Logo"
          width={120}
          height={48}
          className="h-12 w-auto object-contain drop-shadow-md"
          priority
        />
      </div>

      {/* Subtle background pattern */}
      <div className="fixed inset-0 overflow-hidden pointer-events-none opacity-5">
        <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(circle_at_50%_50%,rgba(16,185,129,0.1),transparent_50%)]"></div>
      </div>

      <div className="relative z-10 container mx-auto px-4 py-8 max-w-7xl">
        {/* Error Message */}
        {error && (
          <div className="mb-6 p-4 bg-red-50 border border-red-200 rounded-lg">
            <p className="text-red-800 font-medium">Error: {error}</p>
            <p className="text-red-600 text-sm mt-1">Please check the browser console for more details.</p>
          </div>
        )}

        {/* Header */}
        <motion.header
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
          className="text-center mb-12 pt-16"
        >
          <motion.div
            initial={{ scale: 0.9 }}
            animate={{ scale: 1 }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="inline-flex items-center justify-center w-20 h-20 rounded-full bg-gradient-to-r from-emerald-500 to-teal-500 mb-6 shadow-lg"
          >
            <Sparkles className="w-10 h-10 text-white" />
          </motion.div>
          <h1 className="text-5xl md:text-6xl font-bold text-gray-800 mb-4">
            Rituva Execution Roadmap
          </h1>
          <p className="text-xl text-gray-600 font-light">
            Track progress and milestones
          </p>
        </motion.header>

        {/* Filters - Always show */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="mb-8"
        >
          <div className="bg-white rounded-2xl p-6 shadow-lg border border-emerald-100">
            <div className="flex items-center gap-2 mb-4">
              <Filter className="w-5 h-5 text-emerald-600" />
              <h3 className="text-lg font-semibold text-gray-800">Filters</h3>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div>
                <label htmlFor="team-filter" className="block text-sm font-medium text-gray-700 mb-2">
                  <Users className="w-4 h-4 inline mr-2" />
                  Team
                </label>
                <select
                  id="team-filter"
                  value={teamFilter}
                  onChange={(e) => setTeamFilter(e.target.value)}
                  className="w-full px-4 py-3 bg-white border-2 border-emerald-200 rounded-xl text-gray-800 font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all cursor-pointer hover:border-emerald-300"
                >
                  <option value="website">Website Development</option>
                  <option value="artificial-intelligence">Artificial Intelligence</option>
                  <option value="market-research">Market Research</option>
                  <option value="digital-marketing">Digital Marketing</option>
                  <option value="human-resources">Human Resources</option>
                </select>
              </div>

              <div>
                <label htmlFor="month-filter" className="block text-sm font-medium text-gray-700 mb-2">
                  <Calendar className="w-4 h-4 inline mr-2" />
                  Month
                </label>
                <select
                  id="month-filter"
                  value={monthFilter}
                  onChange={(e) => setMonthFilter(e.target.value)}
                  className="w-full px-4 py-3 bg-white border-2 border-emerald-200 rounded-xl text-gray-800 font-medium focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all cursor-pointer hover:border-emerald-300"
                >
                  <option value="all">All Months</option>
                  {Object.entries(monthNames).map(([num, name]) => (
                    <option key={num} value={num}>{name}</option>
                  ))}
                </select>
              </div>
            </div>
          </div>
        </motion.div>

        {/* Stats */}
        {!isLoading && excelData.length > 0 && (
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.4 }}
            className="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8"
          >
            <motion.div
              whileHover={{ scale: 1.02 }}
              className="bg-gradient-to-r from-emerald-500 to-teal-500 rounded-2xl p-6 shadow-lg border border-emerald-400"
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-emerald-50 text-sm font-medium mb-1">Total Tasks</p>
                  <p className="text-4xl font-bold text-white">{totalTasks()}</p>
                </div>
                <div className="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-sm">
                  <CheckCircle2 className="w-8 h-8 text-white" />
                </div>
              </div>
            </motion.div>

            <motion.div
              whileHover={{ scale: 1.02 }}
              className="bg-gradient-to-r from-teal-500 to-cyan-500 rounded-2xl p-6 shadow-lg border border-teal-400"
            >
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-teal-50 text-sm font-medium mb-1">Elements</p>
                  <p className="text-4xl font-bold text-white">{uniqueElements}</p>
                </div>
                <div className="w-16 h-16 rounded-full bg-white/20 flex items-center justify-center backdrop-blur-sm">
                  <Target className="w-8 h-8 text-white" />
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}

        {/* Data Display */}
        {!isLoading && excelData.length > 0 && (
          <div className="space-y-6">
            <AnimatePresence mode="wait">
              {filteredData.length === 0 ? (
                <motion.div
                  key="empty"
                  initial={{ opacity: 0 }}
                  animate={{ opacity: 1 }}
                  exit={{ opacity: 0 }}
                  className="text-center py-20 bg-white rounded-2xl border border-emerald-100"
                >
                  <p className="text-gray-600 text-lg">No data found for the selected filters.</p>
                </motion.div>
              ) : (
                sortedMonths().map((month, monthIndex) => {
                  const grouped = groupedData()
                  const categories = Object.keys(grouped[month])
                  
                  return (
                    <motion.div
                      key={month}
                      initial={{ opacity: 0, y: 30 }}
                      animate={{ opacity: 1, y: 0 }}
                      transition={{ duration: 0.5, delay: monthIndex * 0.1 }}
                      className="bg-white rounded-2xl p-6 md:p-8 shadow-lg border border-emerald-100 overflow-hidden"
                    >
                      {/* Month Header */}
                      <div className={`bg-gradient-to-r ${getMonthColor(month)} rounded-xl p-6 mb-6 shadow-md`}>
                        <div className="flex items-center justify-between flex-wrap gap-4">
                          <div className="flex items-center gap-4">
                            <div className="w-12 h-12 rounded-full bg-white/30 flex items-center justify-center backdrop-blur-sm">
                              <Calendar className="w-6 h-6 text-white" />
                            </div>
                            <div>
                              <h2 className="text-3xl font-bold text-white">{month}</h2>
                              <p className="text-white/90 text-sm mt-1">{categories.length} Categories</p>
                            </div>
                          </div>
                          <div className="flex items-center gap-2 px-4 py-2 bg-white/30 rounded-full backdrop-blur-sm">
                            <Zap className="w-4 h-4 text-white" />
                            <span className="text-white font-semibold">{categories.length}</span>
                          </div>
                        </div>
                      </div>

                      {/* Table for each Category */}
                      <div className="space-y-8">
                        {categories.map((category, categoryIndex) => (
                          <motion.div
                            key={category}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ duration: 0.4, delay: categoryIndex * 0.1 }}
                          >
                            {/* Category Header */}
                            <h3 className="text-lg font-bold text-white bg-emerald-600 px-4 py-3 rounded-t-lg mb-0">{category}</h3>
                            
                            {/* Table */}
                            <div className="overflow-x-auto border border-emerald-200 rounded-b-lg">
                              <table className="w-full border-collapse">
                                <thead>
                                  <tr className="bg-emerald-100 border-b border-emerald-200">
                                    <th className="border border-emerald-200 px-4 py-3 text-left font-semibold text-gray-800 text-sm">
                                      {teamFilter === 'digital-marketing' ? 'Element' : 'Element'}
                                    </th>
                                    {teamFilter === 'digital-marketing' && (
                                      <th className="border border-emerald-200 px-4 py-3 text-left font-semibold text-gray-800 text-sm">Sub-element</th>
                                    )}
                                    <th className="border border-emerald-200 px-4 py-3 text-left font-semibold text-gray-800 text-sm">Task</th>
                                    {teamFilter !== 'human-resources' && teamFilter !== 'market-research' && (
                                      <th className="border border-emerald-200 px-4 py-3 text-left font-semibold text-gray-800 text-sm">Monthly Task</th>
                                    )}
                                  </tr>
                                </thead>
                                <tbody>
                                  {Object.keys(grouped[month][category]).map((groupKey, elementIndex) => {
                                    const items = grouped[month][category][groupKey]
                                    
                                    // Check if all sub-elements are "Other" - if so, hide the column
                                    const hasSubElements = teamFilter === 'digital-marketing' && items.some(item => item.subElement !== 'Other')
                                    
                                    // Calculate row spans for monthly tasks (merge cells)
                                    const monthlyTaskSpans = {}
                                    let currentMonthly = null
                                    let spanStart = 0
                                    
                                    items.forEach((item, idx) => {
                                      if (item.monthlyTask !== currentMonthly) {
                                        if (currentMonthly !== null) {
                                          monthlyTaskSpans[spanStart] = idx - spanStart
                                        }
                                        currentMonthly = item.monthlyTask
                                        spanStart = idx
                                      }
                                    })
                                    if (currentMonthly !== null) {
                                      monthlyTaskSpans[spanStart] = items.length - spanStart
                                    }
                                    
                                    // Calculate row spans for sub-elements (merge cells)
                                    const subElementSpans = {}
                                    let currentSubElement = null
                                    let subSpanStart = 0
                                    
                                    items.forEach((item, idx) => {
                                      if (item.subElement !== currentSubElement) {
                                        if (currentSubElement !== null) {
                                          subElementSpans[subSpanStart] = idx - subSpanStart
                                        }
                                        currentSubElement = item.subElement
                                        subSpanStart = idx
                                      }
                                    })
                                    if (currentSubElement !== null) {
                                      subElementSpans[subSpanStart] = items.length - subSpanStart
                                    }
                                    
                                    return items.map((item, itemIndex) => (
                                      <tr 
                                        key={`${groupKey}-${itemIndex}`}
                                        className={`border-b border-emerald-100 hover:bg-emerald-50 transition-colors ${itemIndex % 2 === 0 ? 'bg-white' : 'bg-emerald-50/30'}`}
                                      >
                                        <td className="border border-emerald-200 px-4 py-3 text-sm text-gray-700 font-medium">
                                          {itemIndex === 0 ? groupKey : ''}
                                        </td>
                                        {teamFilter === 'digital-marketing' && hasSubElements && subElementSpans[itemIndex] && (
                                          <td 
                                            className="border border-emerald-200 px-4 py-3 text-sm text-gray-700 whitespace-pre-wrap"
                                            rowSpan={subElementSpans[itemIndex]}
                                          >
                                            {item.subElement !== 'Other' ? item.subElement : ''}
                                          </td>
                                        )}
                                        <td className="border border-emerald-200 px-4 py-3 text-sm text-gray-700 whitespace-pre-wrap">
                                          {item.task}
                                        </td>
                                        {teamFilter !== 'human-resources' && teamFilter !== 'market-research' && monthlyTaskSpans[itemIndex] && (
                                          <td 
                                            className="border border-emerald-200 px-4 py-3 text-sm text-gray-600 italic whitespace-pre-wrap"
                                            rowSpan={monthlyTaskSpans[itemIndex]}
                                          >
                                            {item.monthlyTask || 'NA'}
                                          </td>
                                        )}
                                      </tr>
                                    ))
                                  })}
                                </tbody>
                              </table>
                            </div>
                          </motion.div>
                        ))}
                      </div>
                    </motion.div>
                  )
                })
              )}
            </AnimatePresence>
          </div>
        )}

        {/* Loading State */}
        {isLoading && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-20 bg-white rounded-2xl border border-emerald-100 shadow-sm"
          >
            <motion.div
              animate={{ rotate: 360 }}
              transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
              className="inline-block mb-4"
            >
              <Sparkles className="w-12 h-12 text-emerald-500" />
            </motion.div>
            <h2 className="text-2xl font-semibold text-gray-800 mb-2">Loading roadmap data...</h2>
            <p className="text-gray-600">Please wait while we load your development roadmap</p>
          </motion.div>
        )}

        {/* Empty State */}
        {!isLoading && excelData.length === 0 && !error && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="text-center py-20 bg-white rounded-2xl border border-emerald-100 shadow-sm"
          >
            <h2 className="text-2xl font-semibold text-gray-800 mb-2">No data available</h2>
            <p className="text-gray-600">Please select a different team or check the data files</p>
          </motion.div>
        )}
      </div>
    </div>
  )
}
