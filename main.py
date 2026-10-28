
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI(title="Student Performance Prediction API")

model = joblib.load("student_model.pkl")


class StudentData(BaseModel):
    gender: str
    race_ethnicity: str
    parental_education: str
    lunch: str
    test_preparation: str
    reading_score: float
    writing_score: float


@app.get("/")
def home():
    return {"message": "Student Performance API is running"}


@app.post("/predict")
def predict(data: StudentData):
    student = pd.DataFrame([{
        "gender": data.gender,
        "race/ethnicity": data.race_ethnicity,
        "parental level of education": data.parental_education,
        "lunch": data.lunch,
        "test preparation course": data.test_preparation,
        "reading score": data.reading_score,
        "writing score": data.writing_score
    }])

    prediction = model.predict(student)[0]

    return {"predicted_math_score": round(float(prediction), 2)}
