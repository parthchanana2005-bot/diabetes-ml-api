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
    screen_time: ""
  });

  const [result, setResult] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async () => {
    try {
      const response = await fetch("https://diabetes-ml-api-production-156e.up.railway.app/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(formData) // ✅ sends ALL fields
      });

      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));

    } catch (error) {
      setResult("Error connecting to backend");
    }
  };

  return (
    <div style={{
      minHeight: "100vh",
      display: "flex",
      justifyContent: "center",
      alignItems: "center",
      background: "linear-gradient(135deg, #6e8efb, #a777e3)"
    }}>
      <div style={{
        backdropFilter: "blur(20px)",
        background: "rgba(255,255,255,0.15)",
        padding: "30px",
        borderRadius: "20px",
        width: "350px",
        boxShadow: "0 10px 30px rgba(0,0,0,0.2)"
      }}>
        <h1 style={{ textAlign: "center", color: "white" }}>
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
              padding: "10px",
              margin: "8px 0",
              borderRadius: "8px",
              border: "none"
            }}
          />
        ))}

        <button
          onClick={handleSubmit}
          style={{
            width: "100%",
            padding: "12px",
            marginTop: "15px",
            borderRadius: "10px",
            border: "none",
            background: "linear-gradient(45deg, #ff416c, #ff4b2b)",
            color: "white",
            fontWeight: "bold",
            cursor: "pointer"
          }}
        >
          🚀 Predict
        </button>

        <pre style={{
          marginTop: "15px",
          color: "white",
          fontSize: "12px"
        }}>
          {result}
        </pre>
      </div>
    </div>
  );
}

export default App;