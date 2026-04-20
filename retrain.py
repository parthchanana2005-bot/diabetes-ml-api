import subprocess
import pandas as pd
import sys

def retrain_model():

    try:
        df = pd.read_csv("data_store.csv")

        # 🔥 THRESHOLD CHECK
        if len(df) < 10:
            return f"Not enough data for retraining (current: {len(df)})"

        # 🔥 USE SAME PYTHON (VERY IMPORTANT FIX)
        result = subprocess.run(
            [sys.executable, "train_models.py"],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            return "Model retrained successfully ✅"
        else:
            return f"Retraining failed ❌: {result.stderr}"

    except Exception as e:
        return f"Retraining error ❌: {str(e)}"