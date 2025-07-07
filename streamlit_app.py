import streamlit as st
import pandas as pd
from app.data_loader import load_nutrition_data
from app.health_filter import recommend_food
from app.clustering import cluster_foods, get_similar_foods
from app.meal_planner import meal_plan

# 📥 Load and process data
df = load_nutrition_data()
df = cluster_foods(df)

# 🎯 App Title
st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

# 🔍 Disease Based Recommendation
st.header("🔍 Disease Based Recommendation")

conditions = [
    "obesity",
    "type 2 diabetes",
    "high cholesterol (hyperlipidemia)",
    "hypertension (high blood pressure)",
    "non-alcoholic fatty liver disease (nafld)",
    "coronary artery disease (heart disease)",
    "stroke",
    "metabolic syndrome",
    "chronic kidney disease (early stage)",
    "gastroesophageal reflux disease (gerd)",
    "fatty liver (alcoholic / non-alcoholic)",
    "gout",
    "osteoporosis",
    "pcos (polycystic ovary syndrome)",
    "sleep apnea",
    "fatigue / chronic fatigue syndrome",
    "depression & anxiety"
]

condition = st.selectbox("Select condition", conditions)

if st.button("Recommend Foods"):
    recommendations = recommend_food(df, condition)
    st.write(recommendations)

# 🥗 Meal Planner
st.header("🥗 Meal Plan")
target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)

if st.button("Generate Meal Plan"):
    plan = meal_plan(df, target_calories=target_cal, meals=meals)
    st.write(plan)

# 🤝 Similar Foods using KMeans
st.header("🤝 Similar Foods (KMeans Clustering)")
food_input = st.text_input("Enter food name (example: almond)")

if st.button("Find Similar Foods"):
    similar = get_similar_foods(df, food_input)
    st.write(similar)
