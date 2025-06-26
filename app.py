import streamlit as st 
from joblib import load 
import pandas as pd 

model= load("bia.joblib")

st.title("E-Commerce product delivery Prediction Website")

st.markdown("Predict if the delivery has been done on time or not")

warehouse_map= {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'F': 4}
mode_shipment_map = {'Flight': 0, 'Road': 1, 'Ship': 2}
product_importance_map = {'low': 0, 'medium': 1, 'high': 2}
gender_map = {'F': 0, 'M': 1}

import streamlit as st

with st.form("prediction_form"):
    Warehouse_block = st.selectbox(
        "Warehouse_block",
        ['A', 'B', 'C', 'D', 'F']
    )
    Mode_of_Shipment = st.selectbox(
        "Mode_of_Shipment",
        ['Flight', 'Road', 'Ship']
    )
    Customer_care_calls = st.selectbox(
        "Customer_care_calls",
        ["4", "2", "3", "5", "6", "7"]
    )
    Customer_rating = st.selectbox(
        "Customer_rating",
        ["2", "5", "3", "1", "4"]
    )
    Cost_of_the_Product = st.slider(
        "Cost_of_the_Product",
        0, 500, 1
    )
    Prior_purchases = st.selectbox(
        "Prior_purchases",
        ["3", "2", "4", "6", "5", "7", "10", "8"]
    )
    Product_importance = st.selectbox(
        "Product_importance",
        ['low', 'medium', 'high']
    )
    Gender = st.selectbox(
        "Gender",
        ['F', 'M']
    )
    Discount_offered = st.slider(
        "Discount_offered",
        0, 100, 1
    )
    Weight_in_gms = st.slider(
        "Weight_in_gms",
        0, 5000, 1
    )
    submitted = st.form_submit_button("Predict")

if submitted:
    input_df = pd.DataFrame([{
        "Warehouse_block": Warehouse_block,
        "Mode_of_Shipment": Mode_of_Shipment,
        "Customer_care_calls": Customer_care_calls,
        "Customer_rating": Customer_rating,
        "Cost_of_the_Product": Cost_of_the_Product,
        "Prior_purchases": Prior_purchases,
        "Product_importance": Product_importance,
        "Gender": Gender,
        "Discount_offered": Discount_offered,
        "Weight_in_gms": Weight_in_gms
    }])

    input_df["Warehouse_block"] = input_df["Warehouse_block"].map(warehouse_map)
    input_df["Mode_of_Shipment"] = input_df["Mode_of_Shipment"].map(mode_shipment_map)
    input_df["Product_importance"] = input_df["Product_importance"].map(product_importance_map)
    input_df["Gender"] = input_df["Gender"].map(gender_map)

    try:
        columns = ['Warehouse_block', 'Mode_of_Shipment', 'Customer_care_calls',
                   'Customer_rating', 'Cost_of_the_Product', 'Prior_purchases',
                   'Product_importance', 'Gender', 'Discount_offered', 'Weight_in_gms']
        
        prediction = model.predict(input_df[columns])
        st.header("Prediction Result")
        if prediction[0] == 1:
            st.success("✅ Delivery Reached on Time")
        else:
            st.error("❌ Delivery Not Reached on Time")
    
    except Exception as e:
        st.error(f"Prediction failed: {e}")

    
    
    


