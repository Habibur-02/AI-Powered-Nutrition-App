import pandas as pd

def load_nutrition_data(path="data/nutrition.xlsx"):
    # Read Excel
    df = pd.read_excel(path)

    # Drop Unnamed column if exists
    if 'Unnamed: 0' in df.columns:
        df.drop(columns=['Unnamed: 0'], inplace=True)

    # Fill NaN saturated_fat with 0
    if 'saturated_fat' in df.columns:
        df['saturated_fat'].fillna(0, inplace=True)

    # Identify object columns excluding food name
    object_columns = df.select_dtypes(include=['object']).columns.tolist()
    if object_columns:
        food_col = object_columns[0]
        object_columns = object_columns[1:]  # Remove food name from object columns

    # Function to clean nutrient values
    def clean_value(x):
        if isinstance(x, str):
            return (
                x.replace('mg', '')
                 .replace('mcg', '')
                 .replace('mc', '')
                 .replace('IU', '')
                 .replace('g', '')
                 .strip()
            )
        return x

    # Apply cleaning to all object nutrient columns
    for col in object_columns:
        df[col] = df[col].apply(clean_value)
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Convert to numeric, invalid to NaN

    # Specific clean for vitamin_a and vitamin_d (if present)
    for col in ['vitamin_a', 'vitamin_d']:
        if col in df.columns:
            df[col] = df[col].apply(clean_value)
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Fill NaN with 0 for all numeric columns
    for col in df.columns:
        if col != 'name':  # Assuming 'name' is the food column
            df[col].fillna(0, inplace=True)

    return df
