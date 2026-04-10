# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# Load dataset
customers = pd.read_csv("Mall_Customers.csv")

# Encode categorical variable 'Gender' into numeric form
customers['Gender'] = customers['Gender'].map({'Female': 0, 'Male': 1})

# Select features for clustering (Age, Income, Spending Score)
X = customers[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# Standardize features for better clustering performance
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method to determine optimal number of clusters
wcss = []
for clusters in range(1, 11):
    km = KMeans(n_clusters=clusters, init="k-means++", n_init=10, random_state=42)
    km.fit(X_scaled)
    wcss.append(km.inertia_)

plt.figure(figsize=(8,6))
plt.plot(range(1, 11), wcss, marker='o')
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("WCSS")
plt.show()

# Fit KMeans with chosen number of clusters (e.g., 5)
optimal_k = 5
kmeans = KMeans(n_clusters=optimal_k, init="k-means++", n_init=10, random_state=42)
customers['Cluster'] = kmeans.fit_predict(X_scaled)

# Preview clustered data
print(customers.head())

# Visualize clusters using Income vs Spending Score
plt.figure(figsize=(10,6))
plt.scatter(customers['Annual Income (k$)'], customers['Spending Score (1-100)'],
            c=customers['Cluster'], cmap='viridis', s=60)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation by Income and Spending")
plt.colorbar(label="Cluster")
plt.show()

# Save cluster assignments
output = customers[['CustomerID', 'Cluster']]
output.to_csv("customer_segments.csv", index=False)
print("\nCluster results saved to customer_segments.csv")
