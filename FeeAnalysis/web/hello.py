from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Initialize FastAPI
app = FastAPI(
    title="School Satisfaction Predictor",
    description="Predict school sentiment based on facilities, fees, and performance.",
    version="1.0.0"
)

# @app.get('/')
# def root():
#     return {"message":"Hello from FastAPI"}


# @app.get('/profile')
# def root1():
#     return{"message":"Hello from my profile"}

# @app.get('/name')
# def name():
#     return {"message":"Hello !, My name is Anupama Chaudhary"}



# #Load models and vectorizer
# model= joblib.load('sentiment_model.pkl')
# vectorizer=joblib.load('vectorizer.pkl')
# class ReviewText(BaseModel):
#     text:str

# class Marks(BaseModel):
#     maths: int
#     science: int
#     english: int

# @app.post("/predict")
# def predoct_sentiment(review:ReviewText):
#     review_vector=vectorizer.transform([review.text])
#     prediction=model.predict(review_vector)[0]
#     sentiment="Positive" if prediction==1 else "Negative"
#     return {"sentiment":sentiment}




# Load the trained classifier model
model = joblib.load("school_sentiment_model.pkl")         # Replace with your trained model
scaler = joblib.load("feature_scaler.pkl")                # Optional: if you scaled your data

# Define input schema for numeric features
class SchoolFeatures(BaseModel):
    admission_fee: float
    infra_score: float
    academic_score: float

# Prediction endpoint
@app.post("/predict-sentiment", tags=["Numeric Sentiment Prediction"])
def predict_satisfaction(features: SchoolFeatures):
    # Convert input to array
    X = np.array([[features.admission_fee,
                   features.infra_score,
                   features.academic_score]])

    # Optional: scale the features if you used scaling in training
    X_scaled = scaler.transform(X)

    # Make prediction
    prediction = model.predict(X_scaled)[0]
    sentiment = "Low" if prediction == 1 else "High"

    return {
        "input_features": features.dict(),
        "predicted_sentiment": sentiment
    }
