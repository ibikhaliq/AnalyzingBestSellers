# AnalyzingBestSellers
This project analyzes a dataset of best-selling books using Python's pandas, matplotlib, and seaborn libraries. It performs data cleaning, statistical summary, and visual analysis, with all graphs exported to a PDF report.
# 📚 Bestsellers Data Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green?logo=pandas)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualizations-orange?logo=matplotlib)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical_Graphics-blueviolet?logo=seaborn)](https://seaborn.pydata.org/)

Analyze and visualize insights from a dataset of best-selling books using Python libraries: `pandas`, `matplotlib`, and `seaborn`.

---

## 📁 Dataset

**`bestsellers.csv`**  
Includes:
- `Name` (Book Title)
- `Author`
- `User Rating`
- `Reviews`
- `Price`
- `Genre`
- `Year`

---

## ✨ Features

### 🔍 Data Exploration
- View first 5 rows of the dataset
- Output dataset shape and column names
- Show summary statistics for numeric columns

### 🧹 Data Cleaning
- Remove duplicate rows
- Rename columns for easier access:
  - `Name` → `Title`
  - `Year` → `Publication Year`
  - `User Rating` → `Rating`
- Convert `Price` to float

### 📊 Data Analysis
- Count number of times each author appears
- Calculate average rating per genre

---

## 📤 Exported Files

| File Name                 | Description                           |
|--------------------------|---------------------------------------|
| `top_authors.csv`        | Top 10 most frequent authors          |
| `avg_rating_by_genre.csv`| Mean user rating per book genre       |
| `analyzingbestsellers.pdf` | 📄 PDF report with all visualizations |

---

## 📈 Visualizations (Saved to PDF)

All graphs are exported using `PdfPages` from Matplotlib.

### ✅ 1. Bar Chart – Top 10 Authors
Displays the most published authors by count.

### ✅ 2. Pie Chart – Genre Distribution
Shows how genres are distributed (Fiction vs Non Fiction).

### ✅ 3. Box Plot – Rating by Genre
Visualizes rating variation within each genre using Seaborn.

### ✅ 4. Line Chart – Average Rating Over the Years
Tracks rating trends over different publication years.

---

## 💻 How to Run

1. Clone the repo or copy the script.
2. Ensure `bestsellers.csv` is in the same directory.
3. Run the script:

```bash
python main.py
