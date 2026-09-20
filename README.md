# Project 2 — Restaurant Growth Analysis

## SkyCity Auckland Restaurants & Bars

A Business Analyst project focused on identifying restaurant growth opportunities, analyzing profitability, evaluating sales channels, and classifying restaurants by growth potential.

---

## 📌 Project Overview

This project analyzes restaurant-level operational and financial data to understand:

- Restaurant profitability
- Sales-channel performance
- Segment and cuisine performance
- Geographic growth opportunities
- Restaurant growth potential
- Opportunities for improving revenue and margins

The analysis is supported by an interactive Streamlit dashboard.

---

## 📊 Dataset

The dataset contains **1,696 restaurant records** and **30 source fields** covering:

- Restaurant name and ID
- Cuisine type
- Restaurant segment
- Auckland subregion
- Average Order Value (AOV)
- Monthly orders
- Growth factor
- Delivery radius
- Delivery costs
- Revenue by sales channel
- Operating costs
- Channel-level net profit

### Sales Channels

- In-store
- Uber Eats
- DoorDash
- Self-delivery

---

## 🔎 Key Findings

- Total revenue across the dataset is approximately **$77.74M**.
- Total net profit is approximately **$7.87M**.
- Overall portfolio net margin is approximately **10.1%**.
- In-store and self-delivery demonstrate stronger profitability than third-party delivery channels.
- Full-service restaurants are loss-making in aggregate and require further operational investigation.
- South Auckland has the highest average growth factor in the dataset.
- Cafe and QSR formats contribute significant aggregate profit.
- Third-party delivery channels show substantially lower aggregate margins due to commission and delivery-related costs.

---

## 🚀 Growth Potential Index

A transparent **Growth Potential Index (GPI)** was developed to prioritize restaurants for potential growth initiatives.

### Model Weights

| Factor | Weight |
|---|---:|
| Growth Factor | 30% |
| Profit Margin | 35% |
| Monthly Orders | 20% |
| Average Order Value (AOV) | 15% |

Each factor is normalized using min-max scaling before applying the weights.

Restaurants are classified into:

- **High Growth Potential**
- **Medium Growth Potential**
- **Low Growth Potential**

The GPI is a prioritization framework based on the available dataset and should not be interpreted as a guaranteed forecast of future performance.

---

## 💡 Business Recommendations

1. Strengthen profitable in-store and self-delivery channels.
2. Review pricing, commissions, bundles and minimum-order strategies for third-party delivery.
3. Prioritize high-potential restaurants in stronger geographic growth areas.
4. Investigate the cost structure and operating model of full-service restaurants.
5. Use restaurant-level growth classification to target specific interventions instead of applying one strategy across the entire portfolio.

---

## 🖥️ Streamlit Dashboard

The interactive dashboard provides:

- Revenue KPIs
- Net profit KPIs
- Profit margin
- Restaurant count
- Segment analysis
- Subregion analysis
- Channel economics
- Restaurant-level growth classification
- Filters for subregion, segment, cuisine and growth class

---

## 📁 Project Files

| File | Description |
|---|---|
| `app.py` | Streamlit dashboard application |
| `requirements.txt` | Python dependencies |
| `Project_2_Restaurant_Growth_Analysis.csv` | Enriched analysis dataset |
| `Project_2_Restaurant_Growth_Documentation.pdf` | Project documentation |
| `Project_2_Restaurant_Growth_PPT.pptx` | Project presentation |
| `README.md` | Project overview and documentation |

---

## ▶️ Run the Dashboard Locally

Install the required packages:

```bash
pip install -r requirements.txt
