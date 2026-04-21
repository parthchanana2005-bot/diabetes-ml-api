import React, { useState } from "react";

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
    diabetes_risk_score: ""
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
      const response = await fetch("https://diabetes-ml-api-production-15e6.up.railway.app/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(
          Object.fromEntries(
            Object.entries(formData).map(([k, v]) => [k, Number(v)])
          )
        )
      });

      const data = await response.json();
      setResult(JSON.stringify(data, null, 2));
    } catch (error) {
      console.error(error);
      setResult("Error connecting to backend");
    }
  };

  return (
    <div style={{ textAlign: "center", padding: "20px" }}>
      <h1>Diabetes Predictor</h1>

      {Object.keys(formData).map((key) => (
        <div key={key} style={{ margin: "5px" }}>
          <input
            name={key}
            placeholder={key}
            value={formData[key]}
            onChange={handleChange}
            style={{ padding: "8px", width: "250px" }}
          />
        </div>
      ))}

      <br />
      <button onClick={handleSubmit} style={{ padding: "10px 20px" }}>
        Predict
      </button>

      <pre style={{ marginTop: "20px" }}>{result}</pre>
    </div>
  );
}

export default App;