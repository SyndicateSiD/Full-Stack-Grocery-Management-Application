import pandas as pd
import warnings
warnings.filterwarnings("ignore")


df = pd.read_csv('indian_food.csv')

def recommend_food(ingredients_list, num_recommendations=3):
    recommended_foods = df[df.apply(lambda row: all(ingredient in row['ingredients'].lower() for ingredient in ingredients_list.lower().split(',')), axis=1) == True]
    
    if recommended_foods.empty:
        return ["No matching food found."] * num_recommendations
    else:
        recommended_food_sentences = []
        for _, recommended_food in recommended_foods.head(num_recommendations).iterrows():
            recommendation_sentence = f"The recommended food is: {recommended_food['dishes']} \nIngredients: {recommended_food['ingredients']}.\nPreparation time: {recommended_food['prep_time']} minutes.  \nCooking time: {recommended_food['cook_time']} minutes. \nState: {recommended_food['state']}.\n"
            recommended_food_sentences.append(recommendation_sentence)
        return recommended_food_sentences

