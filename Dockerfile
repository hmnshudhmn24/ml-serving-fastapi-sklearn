FROM python:3.11-slim

WORKDIR /app

COPY ./app /app/app
COPY ./model /app/model

RUN pip install fastapi uvicorn scikit-learn joblib

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
