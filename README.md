# 🧠 Real-time ML Model Serving with FastAPI + Scikit-learn

This project demonstrates how to serve a trained Scikit-learn model using **FastAPI**. It includes basic authentication, request validation, logging, and is ready for Docker deployment.

## 🚀 Features

- REST API endpoint to serve predictions
- Model: RandomForestClassifier trained on Iris dataset
- Request schema validation with Pydantic
- Basic Bearer Token authentication
- Logging for predictions and errors
- Docker-ready for deployment

## 📦 Requirements

```bash
pip install fastapi uvicorn scikit-learn joblib
```

## 🛠 How to Use

### 1. Train the model

```bash
python train.py
```

### 2. Run the API

```bash
uvicorn app.main:app --reload
```

### 3. Make a Request

Use `curl`, Postman, or any HTTP client:

```bash
curl -X POST http://127.0.0.1:8000/predict \
-H "Content-Type: application/json" \
-H "Authorization: Bearer your-secret-token" \
-d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

## 🐳 Run with Docker

```bash
docker build -t ml-fastapi .
docker run -p 8000:8000 ml-fastapi
```

## 🧾 Endpoints

- `POST /predict` – Get prediction from the trained model

## 🔐 Authentication

- Add a header: `Authorization: Bearer your-secret-token`
