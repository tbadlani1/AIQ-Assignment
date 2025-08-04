import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# === Load the data ===
df = dataset


print("Preview of dataset:")
print(df.head())

# === Define input and target columns ===
input_features = ['Population', 'Median_Household_Income', 'Temperature', 'Humidity', 'COVID_Cases']
target_column = 'Case_Rate'
meta_columns = ['State', 'Year']

X = df[input_features]
y = df[target_column]
meta = df[meta_columns]

# === Split the data ===
X_train, X_test, y_train, y_test, meta_train, meta_test = train_test_split(
    X, y, meta, test_size=0.2, random_state=42
)

# === Initialize individual models ===
model_rf = RandomForestRegressor(n_estimators=100, random_state=42)
model_gb = GradientBoostingRegressor(n_estimators=100, random_state=42)
model_lr = LinearRegression()

# === Train models ===
model_rf.fit(X_train, y_train)
model_gb.fit(X_train, y_train)
model_lr.fit(X_train, y_train)

# === Predictions from individual models ===
pred_rf = model_rf.predict(X_test)
pred_gb = model_gb.predict(X_test)
pred_lr = model_lr.predict(X_test)

# === Ensemble model using Voting Regressor ===
ensemble = VotingRegressor(estimators=[
    ('rf', model_rf),
    ('gb', model_gb),
    ('lr', model_lr)
])
ensemble.fit(X_train, y_train)
pred_ensemble = ensemble.predict(X_test)

# === Evaluate and compare models ===
print("\nModel Performance Comparison:")
for name, preds in zip(
    ['Random Forest', 'Gradient Boosting', 'Linear Regression', 'Ensemble'],
    [pred_rf, pred_gb, pred_lr, pred_ensemble]
):
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    print(f"{name}: MSE = {mse:.2f}, R² = {r2:.2f}")

# === Create results DataFrame ===
results_df = X_test.copy()
results_df['State'] = meta_test['State'].values
results_df['Year'] = meta_test['Year'].values
results_df['Actual Case Rate'] = y_test.values
results_df['RF Prediction'] = pred_rf
results_df['GB Prediction'] = pred_gb
results_df['LR Prediction'] = pred_lr
results_df['Ensemble Prediction'] = pred_ensemble

# === Feature Importance (RF and GB) ===
importance_rf = pd.DataFrame({
    'Feature': input_features,
    'Importance': model_rf.feature_importances_,
    'Model': 'Random Forest'
})

importance_gb = pd.DataFrame({
    'Feature': input_features,
    'Importance': model_gb.feature_importances_,
    'Model': 'Gradient Boosting'
})

feature_importance_df = pd.concat([importance_rf, importance_gb])
