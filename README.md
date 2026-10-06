# 🛒 Superstore Sales & Profit Analysis — From Raw Data to Interactive Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?logo=pandas&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Visualization-3F4F75?logo=plotly&logoColor=white)
![Dash](https://img.shields.io/badge/Dash-Interactive%20Dashboard-008DE4)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-F37626?logo=jupyter&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen)

> An end-to-end retail analytics project: cleaning a transactional dataset, exploring it to answer concrete business questions, and delivering the findings through an interactive Plotly Dash dashboard with filters and CSV export.

---

## 📑 Table of Contents

1. [Project Overview](#-project-overview)
2. [Project Files](#-project-files)
3. [Dataset](#-dataset)
4. [Workflow](#-workflow)
5. [Data Cleaning & Feature Engineering](#-data-cleaning--feature-engineering)
6. [Exploratory Data Analysis](#-exploratory-data-analysis)
7. [Key Insights](#-key-insights)
8. [Business Recommendations](#-business-recommendations)
9. [Interactive Dashboard](#-interactive-dashboard)
10. [How to Run](#-how-to-run)
11. [Challenges & Lessons Learned](#-challenges--lessons-learned)
12. [Tech Stack](#-tech-stack)
13. [Repository Structure](#-repository-structure)
14. [Future Improvements](#-future-improvements)
15. [Author](#-author)

---

## 🎯 Project Overview

A retail business needs to know **what drives revenue, where profit is being lost, and when demand peaks**. This project answers those questions using the well-known Superstore dataset (9,994 order lines, 2014–2017).

**Objectives**

- Clean, validate and transform raw transactional data with Python and pandas.
- Perform exploratory data analysis (EDA) to uncover trends, patterns, relationships and data-quality issues.
- Build clear visualizations that answer specific business questions.
- Deliver an interactive sales and profitability dashboard with Dash.
- Translate findings into actionable business recommendations.

**Headline numbers (cleaned data)**

| Metric | Value |
|---|---|
| Total Sales | **$2,294,629** |
| Total Profit | **$285,738** |
| Overall Profit Margin | **≈ 12.5%** |
| Average Sales per Order Line | **$229.78** |
| Orders / Customers / Products | 5,009 / 793 / 1,862 |
| Period Covered | 3 Jan 2014 – 30 Dec 2017 |

---

## 📂 Project Files

| # | File | Description |
|---|---|---|
| 1 | [`1_Superstore_Dataset.csv`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/1.Superstore_Dataset.csv) | Raw dataset (9,994 rows × 21 columns), sourced from Kaggle |
| 2 | [`2_Superstore_DataCleaning.ipynb`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/2.Superstore_DataCleaning.ipynb) | Data cleaning, validation and feature-engineering notebook |
| 3 | [`3_Cleaned_Superstore_Dataset.csv`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/3.Cleaned_Superstore_Dataset.csv) | Analysis-ready dataset (9,986 rows × 27 columns) |
| 4 | [`4_EDA_Visualization_Superstore.ipynb`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/4.EDA_Visualization_Superstore.ipynb) | Exploratory analysis and 10 business questions with visualizations |
| 5 | [`5_Superstore_Dashboard.py`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/1.Superstore_Dataset.csv5.Superstore_Dashboard.py) | Interactive Plotly Dash dashboard (filters, KPIs, 8 charts, CSV export) |
| 6 | [`Superstore_Data_Analytics_Project_Report.docx`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/Superstore_Data_Analytics_Project_Report.docx) | Written project report: methodology, insights, challenges |

> 💡 **Tip:** GitHub renders `.ipynb` files directly in the browser, so you can read both notebooks (including charts) without installing anything.

---

## 📊 Dataset

- **Source:** [Superstore Dataset on Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final?resource=download) by Vivek Chowdhury
- **Granularity:** One row per product line within an order
- **Raw size:** 9,994 rows × 21 columns
- **Cleaned size:** 9,986 rows × 27 columns

<details>
<summary><b>Data dictionary (click to expand)</b></summary>

| Column | Description |
|---|---|
| Row ID | Unique ID for each row |
| Order ID | Unique order identifier |
| Order Date / Ship Date | Date the order was placed / shipped |
| Ship Mode | Shipping method (Standard, Second Class, First Class, Same Day) |
| Customer ID / Customer Name | Customer identifier and name |
| Segment | Consumer, Corporate or Home Office |
| Country / State / City / Postal Code | Customer location |
| Region | East, West, Central, South |
| Product ID / Product Name | Product identifier and name |
| Category / Sub-Category | Product hierarchy (3 categories, 17 sub-categories) |
| Sales | Revenue from the line item ($) |
| Quantity | Units sold |
| Discount | Discount rate applied (0–1) |
| Profit | Profit or loss on the line item ($) |

**Engineered columns (added during cleaning)**

| Column | Logic |
|---|---|
| Year, Month, Day | Extracted from `Order Date` |
| Month_Year | Year-month period (e.g. `2016-11`) for time-series analysis |
| Profit_Margin | `Profit / Sales` (0 when Sales = 0) |
| Ship Days | `Ship Date − Order Date` in days |

</details>

---

## 🔄 Workflow

```
Business Understanding → Data Collection → Cleaning & Validation → Feature Engineering
        → EDA & Visualization → Interactive Dashboard → Insights & Recommendations
```

---

## 🧹 Data Cleaning & Feature Engineering

Notebook: [`2_Superstore_DataCleaning.ipynb`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/2.Superstore_DataCleaning.ipynb)

| Step | Action | Outcome |
|---|---|---|
| Loading | Looped through multiple encodings (`utf-8`, `latin1`, `cp1252`, …) | File loaded despite non-UTF-8 characters |
| Missing values | Checked every column with `isnull().sum()` | No missing values found |
| Data types | Converted `Order Date` and `Ship Date` to `datetime`; cast text columns to `string` and trimmed whitespace | Consistent, validated types |
| Exact duplicates | `drop_duplicates()` | None found |
| Duplicate Order ID + Product ID pairs | Averaged `Sales`, `Quantity` and `Profit` across the repeated lines, then kept one row | 8 redundant rows removed (9,994 → 9,986) |
| Product ID ↔ Product Name conflicts | Found 32 Product IDs mapped to two names; standardized each to its most frequent name | One name per Product ID (validated with `nunique() == 1`) |
| Feature engineering | Added `Year`, `Month`, `Day`, `Month_Year`, `Profit_Margin`, `Ship Days` | 6 new analytical columns |
| Export | Saved UTF-8 CSV | [`3_Cleaned_Superstore_Dataset.csv`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/3.Cleaned_Superstore_Dataset.csv) |

---

## 🔍 Exploratory Data Analysis

Notebook: [`4_EDA_Visualization_Superstore.ipynb`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/4.EDA_Visualization_Superstore.ipynb)

The EDA is organized around **10 business questions**, each paired with a purpose-chosen chart:

| # | Business Question | Visualization |
|---|---|---|
| 1 | Which categories generate the most revenue? | Bar chart |
| 2 | How do sales change over time, and which months peak? | Line chart (monthly trend) |
| 3 | Which regions contribute most to sales and profit? | Pie / donut chart |
| 4 | How much variability and outlier risk exists in order values? | Box plot (log scale) |
| 5 | Is there a relationship between discount and profit? | Scatter plot |
| 6 | Which sub-categories drive profit vs. losses? | Horizontal bar chart |
| 7 | How does segment mix vary by region? | Stacked bar chart |
| 8 | Which numeric factors correlate with profit and sales? | Correlation heatmap |
| 9 | What is the category → sub-category sales mix? | Sunburst / treemap-style breakdown |
| 10 | Is shipping efficient, and does ship mode matter? | Grouped bar chart + summary table |

It also includes group analyses of the **top 5 most profitable** and **top 5 loss-making products per category**.

---

## 💡 Key Insights

### 1. Technology leads revenue; Furniture leads on volume but not on profit
| Category | Sales | Profit | Margin |
|---|---:|---:|---:|
| Technology | $835,714 | $145,377 | 17.4% |
| Furniture | $741,289 | $18,339 | **2.5%** |
| Office Supplies | $717,626 | $122,022 | 17.0% |

Furniture generates over $740K in sales yet delivers only ~$18K in profit — the weakest margin by far.

### 2. The West region outperforms; Central under-delivers
| Region | Sales | Profit | Margin |
|---|---:|---:|---:|
| West | $725,368 | $108,406 | 14.9% |
| East | $677,374 | $91,202 | 13.5% |
| Central | $501,240 | $39,706 | **7.9%** |
| South | $390,647 | $46,423 | 11.9% |

Central captures about 22% of sales but returns the lowest profit and margin.

### 3. Strong seasonality, with a holiday peak
- **November** ($351K), **December** ($325K) and **September** ($308K) are the three strongest months.
- **February** ($60K) and **January** ($95K) are the weakest.
- Year-over-year sales grew from **$484K (2014)** to **$732K (2017)**, and profit nearly doubled from **$49.6K to $93.1K**.

### 4. Discounting is the biggest profit leak
| Discount Level | Order Lines | Total Profit | Avg. Margin |
|---|---:|---:|---:|
| No discount | 4,793 | +$320,394 | 34% |
| Up to 20% | 3,801 | +$100,707 | 17% |
| 21–40% | 459 | **−$35,805** | −17% |
| Over 40% | 933 | **−$99,559** | −109% |

Every discount above 20% is destroying value. Discount has a negative correlation with profit (−0.22), while Sales and Profit are positively correlated (0.48).

### 5. Three sub-categories lose money
**Tables (−$17.7K)**, **Bookcases (−$3.5K)** and **Supplies (−$1.2K)** are loss-making. **Copiers ($55.6K)**, **Phones ($44.5K)** and **Accessories ($41.9K)** are the top profit drivers.

### 6. Extreme outliers and concentrated risk
- Average order-line value is ≈ **$230**, yet a single line reached **$22,638**.
- The largest loss was **−$6,600** on a 3D printer sold at a **70% discount**.

### 7. Shipping performance
| Ship Mode | Avg. Ship Days | Sales | Profit |
|---|---:|---:|---:|
| Same Day | 0.04 | $128K | $15.9K |
| First Class | 2.2 | $351K | $49.0K |
| Second Class | 3.2 | $458K | $57.0K |
| Standard Class | 5.0 | $1,357K | $163.9K |

Standard Class carries ~59% of sales; ship mode has no material effect on profitability.

> 📌 Figures above were recomputed from [`3_Cleaned_Superstore_Dataset.csv`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/3.Cleaned_Superstore_Dataset.csv) and match the EDA notebook.

---

## ✅ Business Recommendations

1. **Cap discounts at ~20%.** Discounts beyond that threshold generated roughly **$135K in combined losses**. Introduce approval rules for deep discounts.
2. **Review Furniture pricing and cost structure,** especially Tables and Bookcases, which are loss-making at the sub-category level.
3. **Investigate Central region operations** (pricing, discount practice, product mix, logistics) to lift its 7.9% margin toward the West's 14.9%.
4. **Plan inventory and marketing around Q4 and September,** and run targeted promotions in the weak January–February period.
5. **Double down on Technology and Office Supplies,** which deliver ~17% margins and 94% of total profit.
6. **Add guardrails on high-value orders** to limit exposure to large single-transaction losses.

---

## 📈 Interactive Dashboard

File: [`5_Superstore_Dashboard.py`](https://github.com/Joemy2392/Superstore_Data_Analytics_Project/blob/main/5.Superstore_Dashboard.py) — built with **Plotly Dash**.

**Features**

- **Four dynamic filters:** Year, Category, Region, Segment
- **KPI cards:** Total Sales, Total Profit, Average Order Value
- **Eight interactive charts**, all linked to the filters:
  1. Sales trend over time (line)
  2. Total sales by category (bar)
  3. Sales distribution by region (donut)
  4. Spread of sales by category (box plot, log scale)
  5. Top 10 most profitable products (bar)
  6. Top 10 loss-making products (bar)
  7. Total profit by sub-category (profit/loss colour-coded)
  8. Sales breakdown: category → sub-category (sunburst)
- **Export button:** downloads the currently filtered data as CSV

<!-- Add your screenshots here after running the dashboard:
![Dashboard Overview](./images/dashboard_overview.png)
-->

---

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install dependencies
```bash
pip install pandas numpy matplotlib plotly dash jupyter
```

### 3. Explore the notebooks
```bash
jupyter notebook
```
Open `2_Superstore_DataCleaning.ipynb`, then `4_EDA_Visualization_Superstore.ipynb`.

### 4. Launch the dashboard
The dashboard reads the cleaned CSV from a file path defined near the top of the script. Update it to a relative path before running:

```python
# In 5_Superstore_Dashboard.py
file_path = "3_Cleaned_Superstore_Dataset.csv"
```

Then run:
```bash
python 5_Superstore_Dashboard.py
```
Open **http://127.0.0.1:2392/** in your browser.

> ⚠️ The notebooks also contain local file paths for loading and saving data. Update them to relative paths (e.g. `"1_Superstore_Dataset.csv"`) when running on your own machine.

---

## 🧠 Challenges & Lessons Learned

**Challenges**
- **Data types and encoding:** the raw file required trying several encodings, and dates/numerics needed careful validation.
- **Inconsistent keys:** repeated Order ID + Product ID pairs and Product IDs with multiple names had to be reconciled without distorting totals.
- **Extreme variance:** sales ranged from $0.44 to over $22,000, making standard box plots unreadable. A **log scale** solved this.
- **Dashboard design:** callbacks had to update every chart and KPI consistently whenever any filter changed.

**What I learned**
- Handling the full data lifecycle: ingestion, validation, feature engineering, analysis, and deployment.
- Turning raw numbers into actionable business intelligence rather than just descriptive charts.
- Designing multi-input Dash callbacks and a filtered export workflow.

---

## 🛠 Tech Stack

| Area | Tools |
|---|---|
| Language | Python |
| Data wrangling | pandas, NumPy |
| Visualization | Plotly Express, Matplotlib |
| Dashboard | Dash (Plotly) |
| Environment | Jupyter Notebook |

---

## 🗂 Repository Structure

```
superstore-analytics/
├── 1_Superstore_Dataset.csv
├── 2_Superstore_DataCleaning.ipynb
├── 3_Cleaned_Superstore_Dataset.csv
├── 4_EDA_Visualization_Superstore.ipynb
├── 5_Superstore_Dashboard.py
├── Superstore_Data_Analytics_Project_Report.pdf
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

- Deploy the dashboard publicly (Render, Railway or Hugging Face Spaces).
- Add customer-level analysis: RFM segmentation and retention.
- Build a sales forecasting model (e.g. Prophet / SARIMA).
- Add a profit-prediction model to flag at-risk discounted orders.
- Add state-level geographic maps.
- Add unit tests and data-validation checks to the cleaning pipeline.

---

## 👤 Author

**Emmanuel JOseph** — Data Analyst

- GitHub: [@your-username](https://github.com/joemy2392)
- LinkedIn: [your-linkedin](https://www.linkedin.com/in/emman-joseph)
- Email: ejoseph2392@gmail.com

⭐ If you found this project useful, please consider giving it a star!

---

*Dataset credit: Vivek Chowdhury via [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final). This project is for educational and portfolio purposes.*
