# import streamlit as st
# import pandas as pd
# from app.data_loader import load_nutrition_data
# from app.health_filter import recommend_food
# from app.clustering import cluster_foods, get_similar_foods
# from app.meal_planner import meal_plan

# # 📥 Load and process data
# df = load_nutrition_data()
# df = cluster_foods(df)

# # 🎯 App Title
# st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

# # 🔍 Disease Based Recommendation
# st.header("🔍 Disease Based Recommendation")

# conditions = [
#     "obesity",
#     "type 2 diabetes",
#     "high cholesterol (hyperlipidemia)",
#     "hypertension (high blood pressure)",
#     "non-alcoholic fatty liver disease (nafld)",
#     "coronary artery disease (heart disease)",
#     "stroke",
#     "metabolic syndrome",
#     "chronic kidney disease (early stage)",
#     "gastroesophageal reflux disease (gerd)",
#     "fatty liver (alcoholic / non-alcoholic)",
#     "gout",
#     "osteoporosis",
#     "pcos (polycystic ovary syndrome)",
#     "sleep apnea",
#     "fatigue / chronic fatigue syndrome",
#     "depression & anxiety"
# ]

# condition = st.selectbox("Select condition", conditions)

# if st.button("Recommend Foods"):
#     recommendations = recommend_food(df, condition)
#     st.write(recommendations)

# # 🥗 Meal Planner
# st.header("🥗 Meal Plan")
# target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
# meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)

# if st.button("Generate Meal Plan"):
#     plan = meal_plan(df, target_calories=target_cal, meals=meals)
#     st.write(plan)

# # 🤝 Similar Foods using KMeans
# st.header("🤝 Similar Foods (KMeans Clustering)")
# food_input = st.text_input("Enter food name (example: almond)")

# if st.button("Find Similar Foods"):
#     similar = get_similar_foods(df, food_input)
#     st.write(similar)

import streamlit as st
import pandas as pd
import together
from app.data_loader import load_nutrition_data
from app.health_filter import recommend_food
from app.clustering import cluster_foods, get_similar_foods
from app.meal_planner import meal_plan

# 🔑 Together API Key (Replace with your actual key)
TOGETHER_API_KEY = "99e66c0a4c5e6fbb8df660cd818f38490b3e9a59be960d3bd34f1e1d854fc775"
together.api_key = TOGETHER_API_KEY

# 📥 Load and process data
df = load_nutrition_data()
df = cluster_foods(df)

# 🔀 Sidebar navigation
page = st.sidebar.selectbox("Select Page", ["Nutrition Recommendation", "Chatbot"])

if page == "Nutrition Recommendation":
    st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

    # 🔍 Disease Based Recommendation
    st.header("🔍 Disease Based Recommendation")
    conditions = [
        "obesity", "type 2 diabetes", "high cholesterol (hyperlipidemia)",
        "hypertension (high blood pressure)", "non-alcoholic fatty liver disease (nafld)",
        "coronary artery disease (heart disease)", "stroke", "metabolic syndrome",
        "chronic kidney disease (early stage)", "gastroesophageal reflux disease (gerd)",
        "fatty liver (alcoholic / non-alcoholic)", "gout", "osteoporosis",
        "pcos (polycystic ovary syndrome)", "sleep apnea",
        "fatigue / chronic fatigue syndrome", "depression & anxiety"
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

    # 🤝 Similar Foods
    st.header("🤝 Similar Foods (KMeans Clustering)")
    food_input = st.text_input("Enter food name (example: almond)")
    if st.button("Find Similar Foods"):
        similar = get_similar_foods(df, food_input)
        st.write(similar)

elif page == "Chatbot":
    st.title("🤖 Nutrition Chatbot")
    user_question = st.text_input("Ask your nutrition question:")
    if st.button("Ask"):
        # You can adjust the context or make it dynamic
        context = f"Nutrition dataset sample:\n{df.head(10).to_string()}\n"
        prompt = context + "\nUser question: " + user_question + "\nAnswer:"
        response = together.Complete.create(
            model="mistralai/Mixtral-8x7B-Instruct-v0.1",
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
        )
        answer = response['output']['choices'][0]['text'].strip()
        st.write("💬", answer)
