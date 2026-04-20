import pandas as pd
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
import joblib

print("Retraining using data_store.csv...")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data_store.csv")

# -----------------------------
# CREATE TARGET
# -----------------------------
if "diagnosed_diabetes" not in df.columns:
    df["diagnosed_diabetes"] = df["diabetes_risk_score"].apply(lambda x: 1 if x > 50 else 0)

# -----------------------------
# TARGETS
# -----------------------------
y_risk = df["diabetes_risk_score"]
y_class = df["diagnosed_diabetes"]
y_stage = df["diabetes_stage"]

# -----------------------------
# FEATURES
# -----------------------------
X = df.drop(columns=["diabetes_risk_score", "diagnosed_diabetes", "diabetes_stage"])

categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numeric_cols = X.select_dtypes(exclude=["object"]).columns.tolist()

# -----------------------------
# PREPROCESSOR
# -----------------------------
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numeric_cols)
    ]
)

# -----------------------------
# MODELS
# -----------------------------
risk_model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor())
])

class_model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier())
])

stage_model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestClassifier())
])

print("Training models...")

risk_model.fit(X, y_risk)
class_model.fit(X, y_class)
stage_model.fit(X, y_stage)

# -----------------------------
# SAVE MODELS
# -----------------------------
joblib.dump(risk_model, "risk_model.pkl")
joblib.dump(class_model, "classification_model.pkl")
joblib.dump(stage_model, "stage_model.pkl")

print("Retraining completed successfully!")