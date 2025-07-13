# # import streamlit as st
# # import pandas as pd
# # from app.data_loader import load_nutrition_data
# # from app.health_filter import recommend_food
# # from app.clustering import cluster_foods, get_similar_foods
# # from app.meal_planner import meal_plan

# # # 📥 Load and process data
# # df = load_nutrition_data()
# # df = cluster_foods(df)

# # # 🎯 App Title
# # st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

# # # 🔍 Disease Based Recommendation
# # st.header("🔍 Disease Based Recommendation")

# # conditions = [
# #     "obesity",
# #     "type 2 diabetes",
# #     "high cholesterol (hyperlipidemia)",
# #     "hypertension (high blood pressure)",
# #     "non-alcoholic fatty liver disease (nafld)",
# #     "coronary artery disease (heart disease)",
# #     "stroke",
# #     "metabolic syndrome",
# #     "chronic kidney disease (early stage)",
# #     "gastroesophageal reflux disease (gerd)",
# #     "fatty liver (alcoholic / non-alcoholic)",
# #     "gout",
# #     "osteoporosis",
# #     "pcos (polycystic ovary syndrome)",
# #     "sleep apnea",
# #     "fatigue / chronic fatigue syndrome",
# #     "depression & anxiety"
# # ]

# # condition = st.selectbox("Select condition", conditions)

# # if st.button("Recommend Foods"):
# #     recommendations = recommend_food(df, condition)
# #     st.write(recommendations)

# # # 🥗 Meal Planner
# # st.header("🥗 Meal Plan")
# # target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
# # meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)

# # if st.button("Generate Meal Plan"):
# #     plan = meal_plan(df, target_calories=target_cal, meals=meals)
# #     st.write(plan)

# # # 🤝 Similar Foods using KMeans
# # st.header("🤝 Similar Foods (KMeans Clustering)")
# # food_input = st.text_input("Enter food name (example: almond)")

# # if st.button("Find Similar Foods"):
# #     similar = get_similar_foods(df, food_input)
# #     st.write(similar)

# import streamlit as st
# import pandas as pd
# import together
# import os
# from dotenv import load_dotenv
# from app.data_loader import load_nutrition_data
# from app.health_filter import recommend_food
# from app.clustering import cluster_foods, get_similar_foods
# from app.meal_planner import meal_plan

# # 🔑 Together API Key (Replace with your actual key)
# load_dotenv()
# TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")
# together.api_key = TOGETHER_API_KEY

# # 📥 Load and process data
# df = load_nutrition_data()
# df = cluster_foods(df)

# # 🔀 Sidebar navigation
# page = st.sidebar.selectbox("Select Page", ["Nutrition Recommendation", "Chatbot"])

# if page == "Nutrition Recommendation":

#     st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

#     # 🔍 Disease Based Recommendation
#     st.header("🔍 Disease Based Recommendation")
#     conditions = [
#         "obesity", "type 2 diabetes", "high cholesterol (hyperlipidemia)",
#         "hypertension (high blood pressure)", "non-alcoholic fatty liver disease (nafld)",
#         "coronary artery disease (heart disease)", "stroke", "metabolic syndrome",
#         "chronic kidney disease (early stage)", "gastroesophageal reflux disease (gerd)",
#         "fatty liver (alcoholic / non-alcoholic)", "gout", "osteoporosis",
#         "pcos (polycystic ovary syndrome)", "sleep apnea",
#         "fatigue / chronic fatigue syndrome", "depression & anxiety"
#     ]
#     condition = st.selectbox("Select condition", conditions)
#     if st.button("Recommend Foods"):
#         recommendations = recommend_food(df, condition)
#         st.write(recommendations)

#     # 🥗 Meal Planner
#     st.header("🥗 Meal Plan")
#     target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
#     meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)
#     if st.button("Generate Meal Plan"):
#         plan = meal_plan(df, target_calories=target_cal, meals=meals)
#         st.write(plan)

#     # 🤝 Similar Foods
#     st.header("🤝 Similar Foods (KMeans Clustering)")
#     food_input = st.text_input("Enter food name (example: almond)")
#     if st.button("Find Similar Foods"):
#         similar = get_similar_foods(df, food_input)
#         st.write(similar)


# elif page == "Chatbot":
        
#         st.title("🤖 Nutrition Chatbot")
#         user_question = st.text_input("Ask your nutrition question:")

#         if st.button("Ask"):
#             # Nutrition ডেটাসেটের ছোট্ট স্যাম্পল কনটেক্সট হিসেবে ব্যবহার করছি
#             context = f"Nutrition dataset sample:\n{df.head(10).to_string()}\n"

#             # ইউজারের প্রশ্নসহ প্রম্পট তৈরি
#             prompt = context + "\nUser question: " + user_question + "\nAnswer:"

#             # Together API কল
#             response = together.Complete.create(
#                 model="mistralai/Mixtral-8x7B-Instruct-v0.1",
#                 prompt=prompt,
#                 max_tokens=150,
#                 temperature=0.7,
#             )

            
#             try:
                
#                 answer = response['output']['choices'][0]['text'].strip()
#             except (KeyError, IndexError, TypeError):
                
#                 answer = "⚠️ Response parsing error. Please try again."

#             st.write("💬", answer)




# # elif page == "Chatbot":
# #     st.title("🤖 Nutrition Chatbot")
# #     user_question = st.text_input("Ask your nutrition question:")
# #     if st.button("Ask"):
# #         # You can adjust the context or make it dynamic
# #         context = f"Nutrition dataset sample:\n{df.head(10).to_string()}\n"
# #         prompt = context + "\nUser question: " + user_question + "\nAnswer:"
# #         response = together.Complete.create(
# #             model="mistralai/Mixtral-8x7B-Instruct-v0.1",
# #             prompt=prompt,
# #             max_tokens=150,
# #             temperature=0.7,
# #         )
# #         answer = response['output']['choices'][0]['text'].strip()
# #         st.write("💬", answer)
# #testing just 

# import streamlit as st
# import pandas as pd
# import openai
# import os
# from dotenv import load_dotenv
# from app.data_loader import load_nutrition_data
# from app.health_filter import recommend_food
# from app.clustering import cluster_foods, get_similar_foods
# from app.meal_planner import meal_plan

# # 🔑 OpenAI API Key (from .env file)
# load_dotenv()
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# openai.api_key = OPENAI_API_KEY

# # 📥 Load and process data
# df = load_nutrition_data()
# df = cluster_foods(df)

# # 🔀 Sidebar navigation
# page = st.sidebar.selectbox("Select Page", ["Nutrition Recommendation", "Chatbot"])

# if page == "Nutrition Recommendation":
#     st.title("🍽️ SmartNutriPlan - AI Powered Nutrition App")

#     # 🔍 Disease Based Recommendation
#     st.header("🔍 Disease Based Recommendation")
#     conditions = [
#         "obesity", "type 2 diabetes", "high cholesterol (hyperlipidemia)",
#         "hypertension (high blood pressure)", "non-alcoholic fatty liver disease (nafld)",
#         "coronary artery disease (heart disease)", "stroke", "metabolic syndrome",
#         "chronic kidney disease (early stage)", "gastroesophageal reflux disease (gerd)",
#         "fatty liver (alcoholic / non-alcoholic)", "gout", "osteoporosis",
#         "pcos (polycystic ovary syndrome)", "sleep apnea",
#         "fatigue / chronic fatigue syndrome", "depression & anxiety"
#     ]
#     condition = st.selectbox("Select condition", conditions)
#     if st.button("Recommend Foods"):
#         recommendations = recommend_food(df, condition)
#         st.write(recommendations)

#     # 🥗 Meal Planner
#     st.header("🥗 Meal Plan")
#     target_cal = st.number_input("Target calories", min_value=500, max_value=4000, value=2000, step=50)
#     meals = st.number_input("Number of meals", min_value=1, max_value=5, value=3)
#     if st.button("Generate Meal Plan"):
#         plan = meal_plan(df, target_calories=target_cal, meals=meals)
#         st.write(plan)

#     # 🤝 Similar Foods
#     st.header("🤝 Similar Foods (KMeans Clustering)")
#     food_input = st.text_input("Enter food name (example: almond)")
#     if st.button("Find Similar Foods"):
#         similar = get_similar_foods(df, food_input)
#         st.write(similar)

# elif page == "Chatbot":
#     st.title("🤖 Nutrition Chatbot")
#     user_question = st.text_input("Ask your nutrition question:")

#     if st.button("Ask"):
#         # Nutrition dataset context
#         context = f"Nutrition dataset sample:\n{df.head(10).to_string()}\n"
        
#         # Create the prompt for OpenAI
#         messages = [
#             {"role": "system", "content": "You are a nutrition expert. Answer questions based on the provided context and your knowledge."},
#             {"role": "user", "content": context + "\nUser question: " + user_question}
#         ]

#         try:
#             # OpenAI API call
#             response = openai.ChatCompletion.create(
#                 model="gpt-3.5-turbo",
#                 messages=messages,
#                 max_tokens=300,
#                 temperature=0.7
#             )
            
#             # Extract the answer
#             answer = response['choices'][0]['message']['content'].strip()
#             st.write("💬", answer)
            
#         except Exception as e:
#             st.error(f"⚠️ Error getting response: {str(e)}")

import streamlit as st
import pandas as pd
import google.generativeai as genai
import os
from dotenv import load_dotenv
from app.data_loader import load_nutrition_data
from app.health_filter import recommend_food
from app.clustering import cluster_foods, get_similar_foods
from app.meal_planner import meal_plan

# 🔑 Google Gemini API Key (from .env file)
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(
    api_key=GEMINI_API_KEY,
    transport='rest'  # Important addition
)
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
    st.title("🤖 Nutrition Chatbot (Powered by Gemini)")
    user_question = st.text_input("Ask your nutrition question:")

    if st.button("Ask"):
        # Nutrition dataset context
        context = f"""
        Nutrition dataset sample:
        {df.head(10).to_string()}
        
        You are a certified nutrition expert. Provide accurate, science-backed answers about:
        - Food recommendations
        - Meal planning
        - Nutrient information
        - Dietary advice for medical conditions
        
        Answer concisely and cite sources when possible.
        """
        
        try:
            
            model = genai.GenerativeModel('gemini-1.0-pro')  
            
          
            response = model.generate_content(
                f"{context}\n\nQuestion: {user_question}",
                generation_config=genai.types.GenerationConfig(
                    max_output_tokens=1000,
                    temperature=0.7
                )
            )
            
            
            st.write("💬", response.text)
            
        except Exception as e:
            st.error(f"⚠️ Error getting response: {str(e)}")
            st.info("Note: Gemini has a free tier but may have rate limits")
