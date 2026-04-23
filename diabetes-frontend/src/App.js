import React, { useState } from "react";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    pregnancies: "",
    glucose: "",
    blood_pressure: "",
    skin_thickness: "",
    insulin: "",
    bmi: "",
    diabetes_pedigree_function: "",
    age: "",
    glucose_postprandial: "",
    hba1c: "",
    insulin_level: "",
    diabetes_risk_score: "",
    waist_to_hip_ratio: "",
    heart_rate: "",
    triglycerides: "",
    diet_score: "",
    cardiovascular_history: "",
    alcohol_consumption_per_week: "",
    physical_activity_minutes_per_week: "",
    screen_time: "",
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch(
        "https://diabetes-ml-api-production-156e.up.railway.app/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(
            Object.fromEntries(
              Object.entries(formData).map(([k, v]) => [k, parseFloat(v)])
            )
          ),
        }
      );

      const data = await response.json();

      if (data.prediction !== undefined) {
        setResult("Prediction: " + data.prediction);
      } else {
        setResult("Error: " + JSON.stringify(data));
      }
    } catch (error) {
      console.error(error);
      setResult("Error connecting to backend");
    }
  };

  return (
    <div
      style={{
        minHeight: "100vh",
        background:
          "linear-gradient(135deg, #5f5fc4, #8f6ed5, #c77dd8)",
        display: "flex",
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <div
        style={{
          background: "rgba(255,255,255,0.15)",
          backdropFilter: "blur(15px)",
          padding: "30px",
          borderRadius: "20px",
          width: "400px",
          boxShadow: "0 8px 32px rgba(0,0,0,0.2)",
        }}
      >
        <h1 style={{ textAlign: "center", color: "#fff" }}>
          Diabetes Predictor
        </h1>

        {Object.keys(formData).map((key) => (
          <input
            key={key}
            name={key}
            placeholder={key}
            value={formData[key]}
            onChange={handleChange}
            style={{
              width: "100%",
              margin: "8px 0",
              padding: "10px",
              borderRadius: "10px",
              border: "none",
            }}
          />
        ))}

        <button
          onClick={handleSubmit}
          style={{
            width: "100%",
            padding: "12px",
            marginTop: "10px",
            borderRadius: "10px",
            border: "none",
            background: "#ff4b5c",
            color: "#fff",
            fontWeight: "bold",
            cursor: "pointer",
          }}
        >
          🚀 Predict
        </button>

        <p style={{ marginTop: "15px", color: "#fff", textAlign: "center" }}>
          {result}
        </p>
      </div>
    </div>
  );
}

export default App;