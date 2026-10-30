# Global Electric Vehicle Market Performance & Executive Insights

An interactive Tableau dashboard, narrative story, and Python Flask web application analyzing global Electric Vehicle (EV) sales volume, battery chemistry efficiencies ($km/kWh$), OEM market share, and regional customer satisfaction benchmarks across major manufacturing hubs.

---

## 📊 Live Interactive Dashboard & Web Portal

👉 **[View the Live Interactive Web Portal on Render]([https://electric-vehicle-market-performance-insightss.onrender.com](https://electric-vehicle-market-performance-tdwa.onrender.com/))**  
👉 **[View the Live Interactive Dashboard on Tableau Public](https://public.tableau.com/views/EV_Market_Performance_Dashboard_17932088931070/Dashboard1)**  
👉 **[View the 4-Scene Narrative Story on Tableau Public](https://public.tableau.com/views/EV_Market_Performance_Dashboard_17932088931070/Story1)**  

---

## 🖼️ Dashboard Preview

<img width="1805" height="800" alt="image" src="https://github.com/user-attachments/assets/1a330ec4-17d0-4c79-a7b5-8a9d890f1e5d" />


---

## 📌 Project Overview

* **Data Granularity:** Multi-year global EV market observations across 6 vehicle categories, 4 battery chemistries, and major manufacturing regions (USA, China, Germany, India, South Korea, Japan).
* **Core KPI Metrics:**
  * **Total Sales Volume:** 9.78 Million Units
  * **Average Base Price:** $41,250 USD
  * **Average Driving Range:** 382.4 km
  * **Average Customer Rating:** 4.38 / 5.00

---

## 🔍 Key Dashboard Features

1. **Category Sales Breakdown:** Horizontal bar chart highlighting SUV (5.38M units) and Sedan (2.39M units) market dominance, accounting for over 75% of global sales volume.
2. **Manufacturer Market Share:** Interactive treemap displaying OEM market concentration across industry leaders (Tesla, BYD, Hyundai, Tata Motors, Volkswagen).
3. **Battery Technology & Range Efficiency:** Dual-axis combo chart benchmarking chemistry performance ($km/kWh$), revealing that Solid-State ($7.01\text{ km/kWh}$) and LFP ($6.92\text{ km/kWh}$) deliver superior energy efficiency.
4. **Geographic Distribution Map:** Choropleth visualization mapping regional manufacturing throughput and customer satisfaction indices worldwide.
5. **Interactive Cross-Filtering:** Linked global action filters enabling real-time drill-downs across categories, manufacturers, and regions.

---

## 🛠️ Tools & Technologies

* **Visualization & Storytelling:** Tableau Desktop / Tableau Public
* **Data Engineering & Analysis:** Python (`pandas`, `sqlite3`), SQL (SQLite Relational DB)
* **Web Framework & Deployment:** Python Flask, HTML5, Bootstrap 5, Gunicorn, Render
* **Version Control:** Git & GitHub
* **Data Source:** `ev_market_performance_dataset.csv`

---

## 🚀 How to Run Locally

1. **Clone this repository:**
   ```bash
   git clone https://github.com/honey606patel-png/Electric-Vehicle-Market-Performance-Insightss.git
   cd Electric-Vehicle-Market-Performance-Insightss
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Web Application:**
   ```bash
   cd web_app
   python app.py
   ```

4. **Open in Web Browser:**  
   Navigate to `http://127.0.0.1:5000` to interact with the embedded web portal.
