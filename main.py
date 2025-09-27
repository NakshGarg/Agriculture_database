import pandas as pd
from fastapi import FastAPI
from typing import Optional

app = FastAPI()

# Load CSVs
users = pd.read_csv("users.csv")
produce = pd.read_csv("produce.csv")
crops = pd.read_csv("crops.csv")
transactions = pd.read_csv("Buyer_Seller_Transactions.csv")
feedback = pd.read_csv("Feedback.csv")
market_rates = pd.read_csv("Market_Rates.csv")
notifications = pd.read_csv("Notifications.csv")
storage = pd.read_csv("StorageFacilities.csv")
weather_alerts = pd.read_csv("Weather_Alerts.csv")
weather_data = pd.read_csv("WeatherData.csv")
crops_produce = pd.read_csv("Crops and Produce.csv")

# ---------- USERS ----------
@app.get("/users")
def get_users():
    return users.to_dict(orient="records")

@app.get("/users/{user_id}")
def get_user(user_id: int):
    filtered = users[users['user_id'] == user_id]
    return filtered.to_dict(orient="records")

# ---------- PRODUCE ----------
@app.get("/produce")
def get_all_produce():
    return produce.to_dict(orient="records")

@app.get("/produce/farmer/{farmer_id}")
def get_produce_by_farmer(farmer_id: int):
    filtered = produce[produce['farmer_id'] == farmer_id]
    return filtered.to_dict(orient="records")

@app.get("/produce/crop/{crop_id}")
def get_produce_by_crop(crop_id: int):
    filtered = produce[produce['crop_id'] == crop_id]
    return filtered.to_dict(orient="records")

# ---------- CROPS ----------
@app.get("/crops")
def get_crops():
    return crops.to_dict(orient="records")

@app.get("/crops/{crop_id}")
def get_crop(crop_id: int):
    filtered = crops[crops['CropID'] == crop_id]
    return filtered.to_dict(orient="records")

# ---------- MARKET RATES ----------
@app.get("/market_rates")
def get_all_market_rates():
    return market_rates.to_dict(orient="records")

@app.get("/market_rates/{crop_id}")
def get_market_rate(crop_id: int):
    filtered = market_rates[market_rates['CropID'] == crop_id]
    return filtered.to_dict(orient="records")

# ---------- TRANSACTIONS ----------
@app.get("/transactions")
def get_all_transactions():
    return transactions.to_dict(orient="records")

@app.get("/transactions/user/{user_id}")
def get_transactions_by_user(user_id: int):
    filtered = transactions[(transactions['buyer_id'] == user_id) | (transactions['seller_id'] == user_id)]
    return filtered.to_dict(orient="records")

# ---------- FEEDBACK ----------
@app.get("/feedback")
def get_all_feedback():
    return feedback.to_dict(orient="records")

@app.get("/feedback/user/{user_id}")
def get_feedback_by_user(user_id: int):
    filtered = feedback[feedback['user_id'] == user_id]
    return filtered.to_dict(orient="records")

# ---------- NOTIFICATIONS ----------
@app.get("/notifications")
def get_all_notifications():
    return notifications.to_dict(orient="records")

@app.get("/notifications/user/{user_id}")
def get_notifications_by_user(user_id: int):
    filtered = notifications[notifications['user_id'] == user_id]
    return filtered.to_dict(orient="records")

# ---------- STORAGE ----------
@app.get("/storage")
def get_all_storage():
    return storage.to_dict(orient="records")

@app.get("/storage/{location}")
def get_storage_by_location(location: str):
    filtered = storage[storage['Location'].str.lower() == location.lower()]
    return filtered.to_dict(orient="records")

# ---------- WEATHER ALERTS ----------
@app.get("/weather_alerts")
def get_all_weather_alerts():
    return weather_alerts.to_dict(orient="records")

@app.get("/weather_alerts/location/{location}")
def get_weather_alerts_by_location(location: str):
    filtered = weather_alerts[weather_alerts['Location'].str.lower() == location.lower()]
    return filtered.to_dict(orient="records")

# ---------- WEATHER DATA ----------
@app.get("/weather_data")
def get_all_weather_data():
    return weather_data.to_dict(orient="records")

@app.get("/weather_data/location/{location}")
def get_weather_data_by_location(location: str):
    filtered = weather_data[weather_data['Location'].str.lower() == location.lower()]
    return filtered.to_dict(orient="records")

# ---------- JOINS / ADVANCED QUERY ----------
@app.get("/farmer_crops/{farmer_id}")
def get_farmer_crops(farmer_id: int):
    merged = produce.merge(crops, left_on='crop_id', right_on='CropID', how='left')
    filtered = merged[merged['farmer_id'] == farmer_id]
    return filtered.to_dict(orient="records")

@app.get("/crop_transactions/{crop_id}")
def get_crop_transactions(crop_id: int):
    merged = transactions.merge(produce, left_on='produce_id', right_on='produce_id', how='left')
    filtered = merged[merged['crop_id'] == crop_id]
    return filtered.to_dict(orient="records")
