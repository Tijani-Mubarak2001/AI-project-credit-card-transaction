# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 14:43:29 2022

@author: temp
"""

import numpy as np
import pickle
import streamlit as st
from PIL import Image

loaded_model = pickle.load(open('C:/Users/temp/AI Credit Card Fraud detection proj/trained_fraud_model.sav', 'rb'))


# creating a function for prediction

def transaction_prediction(input_data):
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    result = loaded_model.predict(input_data_reshaped)
    if result[0] == 0:
        return "No Fraud"
    elif result[0] == 1:
        return "Fraud"


def group_members_page():
    st.title("AI CLASS GROUP MEMBERS")

    tijani_img = Image.open('tijani pic.jpeg')
    st.image(tijani_img, caption='Tijani Mubarak', use_column_width=True)
    st.subheader("Name: Tijani Mubarak(Group Leader)")
    st.subheader("Matric Number: 19/2091")
    st.write("""
        Website[![Tijani Mubarak](https://img.shields.io/badge/Author-@TijaniMubarak-gray.svg?colorA=gray&colorB=dodgergreen&logo=react)](https://tijaniportfolio.netlify.app/) Linkedin
        [![Tijani Mubarak](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logoColor=white)](https://www.linkedin.com/in/mubaraktijani/) and Twitter  [![Tijani Mubarak](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=gray)](https://twitter.com/TijaniMubarakA1)
        
        ----
        """)
    ojochunu_img = Image.open('ojochunu pic.jpg')
    st.image(ojochunu_img, caption='Sanni Collins', use_column_width=True)
    st.subheader("Name: Sanni Collins")
    st.subheader("Matric Number: 19/1547")
    st.write("""
        ----
    """)
    boye_img = Image.open('boye pic.jpg')
    st.image(boye_img, caption='Oyelola Adeboye', use_column_width=True)
    st.subheader("Name: Oyelola Adeboye")
    st.subheader("Matric Number: 19/2627")
    st.write("""
            ----
        """)
    fortune_img = Image.open('precious pic.jpg')
    st.image(fortune_img, caption='Precious Fortune', use_column_width=True)
    st.subheader("Name: Precious Fortune")
    st.subheader("Matric Number: 19/2565")
    st.write("""
                ----
            """)

    tunji_img = Image.open('tunji dp.jpg')
    st.image(tunji_img, caption='Ogunsusi Adetunji', use_column_width=True)
    st.subheader("Name: Ogunsusi Adetunji")
    st.subheader("Matric Number: 19/2500")
    st.write("""
                    ----
                """)

def prediction_page():
    cover_img = Image.open('credit_card.jpg')
    st.image(cover_img, caption='Credit Card Transaction', use_column_width=True)

    st.title("Credit Card Fraud Detection Web App")

    # getting the input data from users

    # distance_from_home 	distance_from_last_transaction 	ratio_to_median_purchase_price 	repeat_retailer 	used_chip 	used_pin_number 	online_order

    distance_from_home = st.number_input("Distance of transaction from home in kilometer:", 0.0, 50000.0)
    distance_from_last_transaction = st.number_input("Distance of transaction from location of last transaction in "
                                                     "kilometer:", 0.0, 50000.0)
    ratio_to_median_purchase_price = st.number_input("Median of purchase price:", 0.0, 50000.0)
    retail = st.selectbox("Did this transaction happen from the same retailer? ", ["Yes", "No"])
    if retail == "Yes":
        repeat_retailer = 1;
    else:
        repeat_retailer = 0;

    chip = st.selectbox("Is the transaction through chip (credit card)? ", ["Yes", "No"])
    if chip == "Yes":
        used_chip = 1;
    else:
        used_chip = 0;

    pin_number = st.selectbox("Did the transaction happened by using PIN number? ", ["Yes", "No"])
    if pin_number == "Yes":
        used_pin_number = 1;
    else:
        used_pin_number = 0;

    online_order = st.selectbox("Is this transaction online? ", ["Yes", "No"])
    if online_order == "Yes":
        its_an_online_order = 1;
    else:
        its_an_online_order = 0;
    if st.button("Click to predict Transaction Type!"):
        transaction = transaction_prediction(
            [distance_from_home, distance_from_last_transaction, ratio_to_median_purchase_price, repeat_retailer,
             used_chip, used_pin_number, its_an_online_order])
        if transaction == "No Fraud":
            st.success("This transaction is not a fraudulent one")
        else:
            st.warning("This transaction is a fraudulent one")


def main():
    navigate = st.sidebar.selectbox("Navigate to other page",
                                    ("Credit card transaction detection", "About Group Members"))
    if navigate == "Credit card transaction detection":
        prediction_page()
    elif navigate == "About Group Members":
        group_members_page()


if __name__ == "__main__":
    main()
