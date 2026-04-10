
# SkillCraft Internship - Task 02: Customer Segmentation with K-Means

## 📌 Project Overview
This project is part of the SkillCraft Internship program. The objective is to apply **K-Means clustering** on the Mall Customer dataset to group customers based on their purchase behavior. The clustering helps identify distinct customer segments, which can be useful for targeted marketing strategies.

---

## 📂 Dataset
- **Mall_Customers.csv** → Contains customer details:
  - `CustomerID`
  - `Gender`
  - `Age`
  - `Annual Income (k$)`
  - `Spending Score (1-100)`

---

## 🔑 Features Used
For clustering, the following features were selected:
- `Age` – Customer’s age  
- `Annual Income (k$)` – Customer’s annual income  
- `Spending Score (1-100)` – Score assigned based on spending behavior  

The `Gender` column was encoded into numeric form but not directly used in clustering visualization.

---

## ⚙️ Methodology
1. **Data Loading**: Import dataset using Pandas.  
2. **Preprocessing**: Encode categorical variables (`Gender`) and scale numeric features using `StandardScaler`.  
3. **Elbow Method**: Determine the optimal number of clusters by plotting Within-Cluster Sum of Squares (WCSS).  
4. **K-Means Clustering**: Apply K-Means with the chosen number of clusters (e.g., 5).  
5. **Visualization**: Plot clusters using Annual Income vs Spending Score.  
6. **Output**: Save cluster assignments to `customer_segments.csv`.

---

## 📊 Visualizations
- **Elbow Method Plot** → Helps decide the optimal number of clusters.  
- **Cluster Scatter Plot** → Shows customer groups based on income and spending score.  

---

## 🚀 How to Run
1. Install required libraries:
   ```bash
   pip install pandas numpy matplotlib scikit-learn
   ```
2. Place `Mall_Customers.csv` inside the `Task2` folder.  
3. Run the notebook/script:
   ```bash
   python customer_segmentation.py
   ```
4. The output file `customer_segments.csv` will be generated.

---

## 📈 Results
- Customers grouped into distinct clusters (e.g., high income–high spending, low income–low spending, etc.).  
- Cluster assignments saved for further analysis.  
- Visualizations provide clear insights into customer segmentation.  

---

