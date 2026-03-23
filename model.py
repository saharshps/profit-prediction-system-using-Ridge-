import pandas as pd
import joblib

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

df = pd.read_csv(r"C:\Users\sahar\OneDrive\Desktop\bank profit model\banking_dataset.csv")

X = df.drop("bank_profit", axis=1)
y = df["bank_profit"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', Ridge())
])

param_grid = {
    'model__alpha': [0.001, 0.01, 0.1, 1, 100]
}

grid_search = GridSearchCV(pipeline, param_grid, cv=5)

grid_search.fit(X_train, y_train)

best_model = grid_search.best_estimator_

y_pred = best_model.predict(X_test)

print("R2 Score:", r2_score(y_test, y_pred))
print("Best Params:", grid_search.best_params_)
print("Best CV Score:", grid_search.best_score_)

joblib.dump(best_model, "ridge_pipeline.joblib")

input_data = pd.DataFrame([[
57.0, 57916.07, 483217.45, 193244.72, 26.0, 0.0, 0.57, 24469.63,
0.0, 1.0, 158.0, 252.72, 0.82, 657.68, 173255.1, 14528.9,
160413.17, 1.0, 3.95, 9604.55, 4691185.95, 167783.82,
13.25, 0.69, 1.66, 7.0, 24.0, 11.1, 2.29, 0.9
]], columns=X.columns)

prediction = best_model.predict(input_data)

print("Prediction:", prediction[0])
