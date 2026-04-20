import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset

def check_drift(reference_path, current_data):

    reference = pd.read_csv(reference_path)
    current = pd.DataFrame([current_data])

    report = Report(metrics=[DataDriftPreset()])
    report.run(reference_data=reference, current_data=current)

    result = report.as_dict()

    drift_detected = result["metrics"][0]["result"]["dataset_drift"]

    return drift_detected
