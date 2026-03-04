# DataGouv Dashboard Builder

A no-code dashboard builder for French open data from [data.gouv.fr](https://www.data.gouv.fr).

![DataGouv Dashboard Builder](https://img.shields.io/badge/DataGouv-Dashboard%20Builder-blue)
![React](https://img.shields.io/badge/React-18-61DAFB?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-3178C6?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind%20CSS-3.4-06B6D4?logo=tailwindcss)
![shadcn/ui](https://img.shields.io/badge/shadcn%2Fui-latest-000000)

## Features

- **Search & Connect** - Browse thousands of datasets from data.gouv.fr. Find data on economy, environment, transport, and more.
- **Auto-Generate Dashboards** - AI analyzes your data and creates relevant visualizations automatically. Bar charts, line graphs, pie charts, and stats.
- **Transparent SQL** - See exactly what queries are run to generate each visualization. Full transparency into how your data is processed.

## How It Works

1. **Search** - Find datasets on data.gouv.fr
2. **Select** - Choose a data resource
3. **Analyze** - We auto-detect data types
4. **Visualize** - Dashboard generates instantly

## Tech Stack

- [React](https://react.dev/) - UI library
- [TypeScript](https://www.typescriptlang.org/) - Type safety
- [Vite](https://vitejs.dev/) - Build tool
- [Tailwind CSS](https://tailwindcss.com/) - Styling
- [shadcn/ui](https://ui.shadcn.com/) - UI components

## Getting Started

### Prerequisites

- Node.js 20+ 
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/datagouv-dashboard-builder.git
cd datagouv-dashboard-builder
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open [http://localhost:5173](http://localhost:5173) in your browser.

### Build for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## Project Structure

```
├── src/
│   ├── components/     # React components
│   │   └── ui/         # shadcn/ui components
│   ├── hooks/          # Custom React hooks
│   ├── lib/            # Utility functions
│   ├── types/          # TypeScript types
│   ├── App.tsx         # Main app component
│   ├── index.css       # Global styles
│   └── main.tsx        # Entry point
├── public/             # Static assets
├── index.html          # HTML template
├── tailwind.config.js  # Tailwind CSS config
├── vite.config.ts      # Vite config
└── package.json        # Dependencies
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License - see LICENSE file for details.

## Acknowledgments

- Powered by [data.gouv.fr](https://www.data.gouv.fr) - French government's open data platform
- Built with [shadcn/ui](https://ui.shadcn.com/) components
