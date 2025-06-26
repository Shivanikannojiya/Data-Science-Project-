import os
os.getcwd() 
os.chdir("C:\BIA") 


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# 1. Read CSV with safe encoding

e_comme = pd.read_excel("E_Commerce.xlsx")



# 2. Drop ID column if exists
e_comme = e_comme.drop(columns=["ID"], errors="ignore")

# 3. Encode categorical columns
le = LabelEncoder()
categorical_cols = ['Warehouse_block', 'Mode_of_Shipment', 'Product_importance', 'Gender']

for col in categorical_cols:
    e_comme[col] = le.fit_transform(e_comme[col])

# 4. Split features and target
X = e_comme.drop(columns=["Reached.on.Time_Y.N"])
y = e_comme["Reached.on.Time_Y.N"]

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train KNN 
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

# 7. Save model
joblib.dump(knn, "bia.joblib")
print("✅ Model trained and saved as bia.joblib")




