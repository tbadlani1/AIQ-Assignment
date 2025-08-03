import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering

# === Copy input data ===
df_copy = input_df.copy()
data_array = df_copy.values  # Convert to NumPy array

# === Apply KMeans clustering ===
kmeans_model = KMeans(
    n_clusters=n_clusters,
    init=init,
    n_init=n_init,
    max_iter=max_iter,
    tol=tol,
    random_state=random_state
)
df_copy['KMeans_Label'] = kmeans_model.fit_predict(data_array)

# === Apply Agglomerative (Hierarchical) clustering ===
hierarchical_model = AgglomerativeClustering(
    n_clusters=n_clusters,
    linkage='ward'  # You can change to 'average', 'complete', etc.
)
df_copy['Hierarchical_Label'] = hierarchical_model.fit_predict(data_array)

# === Output DataFrame with both clustering labels ===
clustered_df = df_copy
