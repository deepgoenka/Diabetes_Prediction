import numpy as np
import pandas as pd
import pickle
import streamlit as st
import warnings
warnings.filterwarnings("ignore")


model = pickle.load(open("C:/Users/User/Downloads/model.sav", 'rb'))

def diabetes_prediction(age, gender, polyuria, polydipsia, wt_loss, weak, polyphagia, gen_thrush, vis_blur, itch, irritability, del_heal, part_pare, mus_stiff, alop, obes):

    # Converting nominal values to 0 or 1
    binary_map_gen = {"Male": 1, "Female": 0}
    gender = binary_map_gen.get(gender, -1)
    binary_map = {"Yes": 1, "No": 0}
    polyuria = binary_map.get(polyuria, -1)
    polydipsia = binary_map.get(polydipsia, -1)
    wt_loss = binary_map.get(wt_loss, -1)
    weak = binary_map.get(weak, -1)
    polyphagia = binary_map.get(polyphagia, -1)
    gen_thrush = binary_map.get(gen_thrush, -1)
    vis_blur = binary_map.get(vis_blur, -1)
    itch = binary_map.get(itch, -1)
    irritability = binary_map.get(irritability, -1)
    del_heal = binary_map.get(del_heal, -1)
    part_pare = binary_map.get(part_pare, -1)
    mus_stiff = binary_map.get(mus_stiff, -1)
    alop = binary_map.get(alop, -1)
    obes = binary_map.get(obes, -1)

    # Converting the list in a DataFrame
    features_df = pd.DataFrame({
        "Age": [age],
        "Gender": [gender],
        "Polyuria": [polyuria],
        "Polydipsia": [polydipsia],
        "sudden weight loss": [wt_loss],
        "weakness": [weak],
        "Polyphagia": [polyphagia],
        "Genital thrush": [gen_thrush],
        "visual blurring": [vis_blur],
        "Itching": [itch],
        "Irritability": [irritability],
        "delayed healing": [del_heal],
        "partial paresis": [part_pare],
        "muscle stiffness": [mus_stiff],
        "Alopecia": [alop],
        "Obesity": [obes]
    })

    # Predicting diabetes based on the features
    prediction = model.predict(features_df)

    # Display the prediction"
    if prediction[0] == 'Positive':
        return "You have Diabetes"
    else:
        return "You do not have Diabetes"


def main():
    st.title("Diabetes Prediction WebPage")

    age = st.text_input("Enter your Age")
    gender = st.text_input("Enter your Gender (Male / Female)")
    polyuria = st.text_input("Do you have Polyuria? (Yes / No)")
    polydipsia = st.text_input("Do you have polydipsia? (Yes / No)")
    wt_loss = st.text_input("Do you have sudden weight loss? (Yes / No)")
    weak = st.text_input("Do you have Weakness? (Yes / No)")
    polyphagia = st.text_input("Do you have Polyphagia? (Yes / No)")
    gen_thrush = st.text_input("Are you having Genital thrush? (Yes / No)")
    vis_blur = st.text_input("Do you have Visual blurring? (Yes / No)")
    itch = st.text_input("Do you have Itching? (Yes / No)")
    irritability = st.text_input("Do you have Irritability? (Yes / No)")
    del_heal = st.text_input("Do you have delayed Healing? (Yes / No)")
    part_pare = st.text_input("Do you have Partial Paresis? (Yes / No)")
    mus_stiff = st.text_input("Do you have Muscle Stiffness? (Yes / No)")
    alop = st.text_input("Do you have Alopecia? (Yes / No)")
    obes = st.text_input("Do you have Obesity? (Yes / No)")

    diagnosis = ''

    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction(age, gender, polyuria, polydipsia, wt_loss, weak, polyphagia, gen_thrush, vis_blur, itch, irritability, del_heal, part_pare, mus_stiff, alop, obes)
    
    st.success(diagnosis)


if __name__ == '__main__':
    main()