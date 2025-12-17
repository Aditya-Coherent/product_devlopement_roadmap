import './globals.css'

export const metadata = {
  title: 'Rituva Development Roadmap',
  description: 'Track your team\'s progress and milestones',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en" className="scroll-smooth">
      <body className="antialiased">
        {children}
      </body>
    </html>
  )
}

