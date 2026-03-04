<div align="center">

# 📊 DataGouv Dashboard Builder

**Transform French Open Data into Beautiful Dashboards — No Code Required**

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![Pandas](https://img.shields.io/badge/Pandas-2.0+-150458?logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-5.18+-3F4F75?logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

[🚀 Live Demo](#) · [📖 Documentation](#documentation) · [🐛 Report Bug](../../issues)

![Dashboard Preview](assets/demo-screenshot.png)

</div>

---

## ✨ Key Features

| Feature | Description |
|---------|-------------|
| 🔍 **Smart Search** | Browse 35,000+ datasets from data.gouv.fr with instant search |
| 🤖 **Auto-Visualization** | AI-powered chart recommendations based on data types |
| 🔎 **SQL Transparency** | View the exact SQL queries powering every visualization |
| 📐 **Grid Editor** | Drag-and-drop dashboard builder with flexible layouts |
| 📊 **Multiple Chart Types** | Bar charts, line graphs, pie charts, and KPI metrics |
| ⚡ **Real-time Preview** | See changes instantly as you configure |
| 🎨 **Modern UI** | Clean, professional SaaS design with Slate/Indigo palette |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- pip package manager

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/datagouv-dashboard-builder.git
cd datagouv-dashboard-builder

# 2. Create virtual environment (recommended)
python -m venv venv

# Activate on macOS/Linux:
source venv/bin/activate

# Activate on Windows:
venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

Open your browser at **`http://localhost:8501`** 🎉

---

## 📁 Project Structure

```
datagouv-dashboard-builder/
├── 📄 app.py                 # Main Streamlit application
├── 📁 src/
│   ├── 📄 database.py        # DataGouv API client & SQL builder
│   └── 📄 ui_components.py   # Reusable UI components & charts
├── 📁 data/                  # Local data storage (gitignored)
├── 📁 assets/                # Images and static files
├── 📄 requirements.txt       # Python dependencies
├── 📄 .gitignore            # Git ignore rules
└── 📄 README.md             # This file
```

---

## 🎯 How It Works

### 1. Search & Connect
Browse thousands of datasets from the French government's open data platform. Search by keywords like "economy", "environment", or "transport".

### 2. Select & Load
Choose a dataset and load it instantly. Our system automatically detects column types (numeric, categorical, date) for optimal visualization.

### 3. Configure Visualizations
Build your dashboard with:
- **KPI Cards** — Track key metrics with customizable aggregations
- **Bar Charts** — Compare categories with horizontal/vertical bars
- **Line Charts** — Track trends over time
- **Pie Charts** — Show proportional distributions

### 4. Transparent SQL
Every visualization shows the exact SQL query used, ensuring full transparency and reproducibility.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.9+** | Core language |
| **Streamlit** | Web application framework |
| **Pandas** | Data manipulation & analysis |
| **Plotly** | Interactive visualizations |
| **Requests** | HTTP client for API calls |

---

## 📊 Example Dashboards

### Economic Indicators Dashboard
```python
# Auto-generated dashboard for French economic data
KPIs: [
  "SUM(GDP) → €2.8T",
  "AVG(Unemployment) → 7.3%",
  "COUNT(Regions) → 18"
]
Charts: [
  "GDP by Region (Bar Chart)",
  "Unemployment Trend (Line Chart)",
  "Sector Distribution (Pie Chart)"
]
```

### Environmental Data Dashboard
```python
# Air quality monitoring dashboard
KPIs: [
  "AVG(PM2.5) → 12.4 µg/m³",
  "MAX(CO2) → 450 ppm",
  "COUNT(Stations) → 156"
]
Charts: [
  "Pollution by City (Bar Chart)",
  "Monthly Trends (Line Chart)"
]
```

---

## 🎨 Customization

### Color Palette

The app uses a modern **Slate/Indigo** color scheme:

| Color | Hex | Usage |
|-------|-----|-------|
| Primary | `#4F46E5` | Buttons, charts, highlights |
| Primary Dark | `#3730A3` | Hover states |
| Background | `#F8FAFC` | Page background |
| Surface | `#FFFFFF` | Cards, containers |
| Text | `#1E293B` | Headings, body text |
| Muted | `#64748B` | Secondary text |

### Adding Custom Charts

```python
from src.ui_components import create_bar_chart
import plotly.graph_objects as go

# Create custom visualization
fig = create_bar_chart(
    df=your_dataframe,
    x_column="category",
    y_column="value",
    title="My Custom Chart"
)
st.plotly_chart(fig, use_container_width=True)
```

---

## 🧪 Development

### Running Tests

```bash
# Install dev dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/
```

### Code Quality

```bash
# Format code
black src/ app.py

# Lint
flake8 src/ app.py

# Type check
mypy src/
```

---

## 🚢 Deployment

### Streamlit Cloud (Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your repository
4. Deploy!

### Docker

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

```bash
docker build -t datagouv-dashboard .
docker run -p 8501:8501 datagouv-dashboard
```

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please read our [Contributing Guide](CONTRIBUTING.md) for details.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- **Data Source**: [data.gouv.fr](https://www.data.gouv.fr) — French government's open data platform
- **UI Components**: Built with [Streamlit](https://streamlit.io) and [Plotly](https://plotly.com)
- **Icons**: [Emoji](https://emoji.supply/kitchen/)

---

## 📬 Contact

Have questions or suggestions?

- Open an [issue](../../issues)
- Connect on [LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

<div align="center">

**⭐ Star this repo if you find it useful!**

Made with ❤️ and ☕ in France

</div>
