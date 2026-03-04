# DataGouv Dashboard Builder - GitHub Setup Guide

This guide will help you create a GitHub repository for the DataGouv Dashboard Builder app and run it locally.

## Project Overview

**DataGouv Dashboard Builder** is a no-code dashboard builder for French open data from [data.gouv.fr](https://www.data.gouv.fr).

### Features
- Search & Connect - Browse thousands of datasets
- Auto-Generate Dashboards - AI-powered visualizations
- Transparent SQL - Full query transparency

### Tech Stack
- React 18 + TypeScript
- Vite (build tool)
- Tailwind CSS
- shadcn/ui components

---

## Option 1: Quick Setup with GitHub CLI (Recommended)

### Prerequisites
- [Git](https://git-scm.com/downloads) installed
- [GitHub CLI](https://cli.github.com/) installed
- [Node.js 20+](https://nodejs.org/) installed

### Steps

1. **Navigate to the project folder:**
   ```bash
   cd /path/to/app
   ```

2. **Run the setup script:**
   ```bash
   bash setup-github.sh
   ```

3. **Follow the prompts** to create your repository.

---

## Option 2: Manual Setup

### Step 1: Initialize Git Repository

```bash
cd /path/to/app
git init
git branch -m main
```

### Step 2: Create GitHub Repository

1. Go to [https://github.com/new](https://github.com/new)
2. Enter **Repository name**: `datagouv-dashboard-builder`
3. Choose **Public** or **Private**
4. **DO NOT** check "Add a README file" (we already have one)
5. Click **Create repository**

### Step 3: Push Code to GitHub

```bash
# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: DataGouv Dashboard Builder"

# Add remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/datagouv-dashboard-builder.git

# Push to GitHub
git push -u origin main
```

---

## Running the App Locally

### Step 1: Install Dependencies

```bash
cd /path/to/app
npm install
```

### Step 2: Start Development Server

```bash
npm run dev
```

### Step 3: Open in Browser

Navigate to [http://localhost:5173](http://localhost:5173)

---

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |
| `npm run lint` | Run ESLint |

---

## Project Structure

```
datagouv-dashboard-builder/
├── src/
│   ├── components/
│   │   └── ui/          # 40+ shadcn/ui components
│   ├── hooks/           # Custom React hooks
│   ├── lib/             # Utility functions
│   ├── App.tsx          # Main app component
│   ├── index.css        # Global styles
│   └── main.tsx         # Entry point
├── index.html           # HTML template
├── tailwind.config.js   # Tailwind CSS config
├── vite.config.ts       # Vite config
├── package.json         # Dependencies
└── README.md            # Project documentation
```

---

## Troubleshooting

### Port 5173 is already in use
```bash
npm run dev -- --port 3000
```

### Node version issues
Make sure you have Node.js 20+:
```bash
node --version
```

### Permission errors on Windows
Run PowerShell/Command Prompt as Administrator.

---

## Next Steps

After setting up your repository:

1. **Customize the app** - Edit `src/App.tsx` to add your own features
2. **Add more components** - Use shadcn/ui components from `src/components/ui/`
3. **Deploy** - Use Vercel, Netlify, or GitHub Pages for free hosting

---

## Resources

- [React Documentation](https://react.dev/)
- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [shadcn/ui Documentation](https://ui.shadcn.com/)
- [data.gouv.fr API](https://www.data.gouv.fr/fr/apidoc/)

---

## License

MIT License - feel free to use and modify!
